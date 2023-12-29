from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from fileSystemHandler import FileSystemHandler
from statisticsHandler import StatisticsHandler
from ldap3 import Server, Connection
from Neural_Search.Qdrant import Qdrant
from dataDefinitions import *
from datetime import datetime
from typing import List
from databaseHandler import DatabaseHandler
import config

class API:

    def __init__(self) -> None:
        self.app = FastAPI(root_path="/api")
        self.router = APIRouter()
        self.qdClient = Qdrant()
        self.DatabaseHandler = DatabaseHandler(config.data_directory, config.database_name)
        self.stats = StatisticsHandler(self.qdClient)
        self.file_system_handler = FileSystemHandler(self.qdClient)
        self.setup_routes()
        self.app.include_router(self.router)

    def setup_routes(self):

        #validate HTW Credentials
        @self.router.post("/login")
        async def validate_credentials(request: LoginRequestModel) -> LoginResponseModel:

            user = self.DatabaseHandler.get_user(request.username )
            if user is None:
                self.DatabaseHandler.add_user(request.username, "Where to get name?", "Where to get E-Mail?", False)
                user = self.DatabaseHandler.get_user(request.username)
            
            ldap_server = Server(config.ldap_server)
            base_dn = config.base_dn
            username = f'cn={request.username},ou=idmusers,' + base_dn
 
            conn = Connection(ldap_server, user=username, password=request.password, auto_bind=False)
            conn.start_tls()

            if conn.bind():
                is_admin = self.DatabaseHandler.check_for_Admin(user)
                if is_admin:
                    return LoginResponseModel(isAuthenticated=True, isAdmin=True)
                else:
                    return LoginResponseModel(isAuthenticated=True, isAdmin=False)
                       
            return LoginResponseModel(isAuthenticated=False, isAdmin=False)
        
        #search
        @self.router.get("/search")
        async def search(user_id: str, query: str):
            try:

                # Perform the search using Qdrant
                results = self.qdClient.search(user_id, query)

                self.DatabaseHandler.log_search(user_id, query) 

                return results
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        #upload document for user id to the file system and qdrant
        @self.router.post("/upload/{user_id}")
        async def upload_document(user_id, files: list[UploadFile] = File(...)):
            status_return = self.file_system_handler.upload(user_id, files)
            return status_return

        #Sends a pdf file to the Website for the viewer
        @self.router.get("/document")
        async def get_document(user_id :str, document_name :str):  # (user_id: str, document_name: str):
            filepath = self.file_system_handler.get_document_path(user_id, document_name)
            if not filepath:
                raise HTTPException(status_code=404, detail="File not found")
            return FileResponse(path=filepath, filename=document_name, media_type="application/pdf")

        #delete document
        @self.router.delete("/deleteDocument/{user_id}/{document_id}")
        async def delete_document(user_id, document_id):
            self.file_system_handler.delete_document(user_id, document_id)
            return True
        
        #send file structure
        @self.router.get("/filestructure/{user_id}")
        async def get_file_structure(user_id):
            return self.file_system_handler.get_fs_for_user(user_id)
        
        #edit document name
        @self.router.put("/editDocumentName/{user_id}")
        async def edit_document_name(user_id, request: RenameFileModel):
            self.file_system_handler.edit_document_name(user_id, request.old_name, request.new_name)
            self.qdClient.rename_doc(user_id, request.old_name, request.new_name)
            return True
        
        #edit document name
        @self.router.head("/revectorize")
        async def revectorize():
            self.qdClient.revectorize_all()
            return True
        
        #get used disk space
        @self.router.get("/diskusage")
        async def get_disk_usage():
            disk_usage = self.DatabaseHandler.get_admin_settings().max_disk_space
            return disk_usage
        
        #change disk space limit
        @self.router.put("/diskusage")
        async def change_disk_usage(disk_usage: float):
            self.DatabaseHandler.update_admin_settings(max_disk_space = disk_usage)
            return True
        
        #get storage
        @self.router.get("/storage_usage")
        async def get_storage_info():
            total_size = self.file_system_handler.get_total_file_size_for_all_users()
            return total_size
        

        #get storage per user
        @self.router.get("/storage_usage/{user_id}")
        async def get_storage_info(user_id):
            total_size = self.file_system_handler.get_file_size_for_user(user_id)
            return total_size

        # get statistics
        @self.router.get("/statistics")
        async def get_statistics():
            return True
        
        # get and set auto-logout time
        @self.router.get("/autologout")
        async def get_auto_logout():
            settings = self.DatabaseHandler.get_admin_settings().logout_timer
            return settings
        
        @self.router.put("/autologout")
        async def set_auto_logout(logout_timer: float):
            self.DatabaseHandler.update_admin_settings(logout_timer = logout_timer)
            return True
        
        #get search history of user
        @self.router.get("/searchhistory/{user_id}")
        async def get_search_history(user_id):
            raw_search_history = self.DatabaseHandler.get_search_history(user_id)
            search_history = []
            for search in raw_search_history:
                search_history.append({'query': search.search_query, 'date': search.timestamp})
            return search_history
        
        @self.router.get("/getnumberofaskedquestions")
        async def get_number_of_asked_questions(given_timestamp:datetime = datetime(2000, 1, 1)):
            return self.DatabaseHandler.get_number_of_asked_questions(given_timestamp)
