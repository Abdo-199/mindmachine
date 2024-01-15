from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from fileSystemHandler import FileSystemHandler
from ldap3 import Server, Connection
from Neural_Search.Qdrant import Qdrant
from dataDefinitions import *
from datetime import datetime
from typing import List
from databaseHandler import DatabaseHandler
import config
import logHandler

class API:
    """
    Represents the API class.

    This class sets up the FastAPI instance, routers, database handler, statistics handler,
    file system handler, logging handler, and routes for the API.

    Attributes:
        app (FastAPI): The FastAPI instance.
        router (APIRouter): The APIRouter instance.
        qdClient (Qdrant): The Qdrant client.
        DatabaseHandler (DatabaseHandler): The database handler.
        file_system_handler (FileSystemHandler): The file system handler.
        api_logging_handler (logHandler.LogHandler): The logging handler.
        logger (Logger): The logger instance.

    Methods:
        setup_routes: Sets up the routes for the API.
    """

    def __init__(self) -> None:
        """
        Initializes the API class.

        This method sets up the FastAPI instance, routers, database handler, statistics handler,
        file system handler, logging handler, and routes for the API.

        Args:
            None

        Returns:
            None
        """
        self.app = FastAPI(root_path="/api")
        self.router = APIRouter()
        self.qdClient = Qdrant()
        self.DatabaseHandler = DatabaseHandler(config.data_directory, config.database_name)
        self.file_system_handler = FileSystemHandler(self.qdClient)
        self.api_logging_handler = logHandler.LogHandler(name="API")
        self.logger = self.api_logging_handler.get_logger()
        self.setup_routes()
        self.app.include_router(self.router)

    def setup_routes(self):
        """
        Sets up the routes for the API.

        Args:
            None

        Returns:
            None
        """

        #validate HTW Credentials
        @self.router.post("/login")
        async def validate_credentials(request: LoginRequestModel) -> LoginResponseModel:

            user = self.DatabaseHandler.get_user(request.username)
            if user is None:
                self.DatabaseHandler.add_user(request.username, False)
                user = self.DatabaseHandler.get_user(request.username)
            
            ldap_server = Server(config.ldap_server)
            base_dn = config.base_dn
            username = f'cn={request.username},ou=idmusers,' + base_dn
 
            conn = Connection(ldap_server, user=username, password=request.password, auto_bind=False)
            conn.start_tls()

            if conn.bind():
                is_admin = self.DatabaseHandler.check_for_Admin(user)
                if is_admin:
                    self.DatabaseHandler.update_last_login(request.username)
                    self.logger.info(f"User {request.username} logged in as admin")
                    return LoginResponseModel(isAuthenticated=True, isAdmin=True)
                else:
                    self.DatabaseHandler.update_last_login(request.username)
                    self.logger.info(f"User {request.username} logged in as user")
                    return LoginResponseModel(isAuthenticated=True, isAdmin=False)
                       
            self.logger.warn(f"User {request.username} failed to log in")       
            return LoginResponseModel(isAuthenticated=False, isAdmin=False)
        
        #search
        @self.router.get("/search")
        async def search(user_id: str, query: str):
            try:

                # Perform the search using Qdrant
                results = self.qdClient.search(user_id, query)

                self.DatabaseHandler.log_search(user_id, query) 
                self.logger.info(f"User {user_id} searched for {query}")
                return results
            except Exception as e:
                self.logger.error(f"User {user_id} failed to search for {query}")
                raise HTTPException(status_code=500, detail=str(e))
        
        #upload document for user id to the file system and qdrant
        @self.router.post("/upload/{user_id}")
        async def upload_document(user_id, files: list[UploadFile] = File(...)):
            status_return = self.file_system_handler.upload(user_id, files)
            self.logger.info(f"User {user_id} uploaded {len(files)} files: {status_return}")
            return status_return

        #Sends a pdf file to the Website for the viewer
        @self.router.get("/document")
        async def get_document(user_id :str, document_name :str):  # (user_id: str, document_name: str):
            filepath = self.file_system_handler.get_document_path(user_id, document_name)
            if not filepath:
                self.logger.error(f"User {user_id} failed to download {document_name}")
                raise HTTPException(status_code=404, detail="File not found")
            self.logger.info(f"User {user_id} downloaded {document_name}")
            return FileResponse(path=filepath, filename=document_name, media_type="application/pdf")

        #delete document
        @self.router.delete("/deleteDocument/{user_id}/{document_id}")
        async def delete_document(user_id, document_id):
            self.file_system_handler.delete_document(user_id, document_id)
            self.logger.info(f"User {user_id} deleted {document_id}")
            return True
        
        #send file structure
        @self.router.get("/filestructure/{user_id}")
        async def get_file_structure(user_id):
            self.logger.info(f"User {user_id} requested file structure")
            return self.file_system_handler.get_fs_for_user(user_id)
        
        #edit document name
        @self.router.put("/editDocumentName/{user_id}")
        async def edit_document_name(user_id, request: RenameFileModel):
            self.logger.info(f"User {user_id} renamed {request.old_name} to {request.new_name}")
            self.file_system_handler.edit_document_name(user_id, request.old_name, request.new_name)
            self.qdClient.rename_doc(user_id, request.old_name, request.new_name)
            return True
        
        #edit document name
        @self.router.head("/revectorize")
        async def revectorize():
            self.qdClient.revectorize_all()
            self.logger.info(f"Revectorized all documents")
            return True
        
        #get used disk space
        @self.router.get("/diskusage")
        async def get_disk_usage():
            disk_usage = self.DatabaseHandler.get_admin_settings().max_disk_space
            disk_usage = self.file_system_handler.convert_bytes_to_gigabyte(disk_usage)
            return disk_usage
        
        #change disk space limit globally DEPRECATED
        @self.router.put("/diskusage")
        async def change_disk_usage(disk_usage: float):
            self.DatabaseHandler.update_admin_settings(max_disk_space = disk_usage)
            return True
        
        #gets the storage capacity of all users
        @self.router.get("/diskusage/user")
        async def get_disk_usage(inBytes: str):
            disk_usage = self.DatabaseHandler.get_admin_settings().user_max_disk_space
            if inBytes == "false":
                disk_usage = self.file_system_handler.convert_bytes_to_gigabyte(disk_usage)
            return disk_usage
        
        #change disk space limit for user
        @self.router.put("/diskusage/user")
        async def change_disk_usage(disk_usage: float):
            self.DatabaseHandler.update_admin_settings(user_max_disk_space = disk_usage)
            return True
        
        #get storage for all users
        @self.router.get("/storage_usage")
        async def get_storage_info():
            total_size = self.file_system_handler.get_total_file_size_for_all_users()
            return total_size
        
        #get storage for one specific user in bytes
        @self.router.get("/storage_usage/{user_id}")
        async def get_storage_info(user_id):
            total_size = self.file_system_handler.get_file_size_for_user(user_id, True)
            return total_size
        
        # get statistics
        @self.router.get("/statistics")
        async def get_statistics():
            activeUsers = self.DatabaseHandler.get_active_users()
            statistics = self.DatabaseHandler.get_all_users()

            for user in statistics:
                user.used_storage = self.file_system_handler.get_file_size_for_user(user.user_id)
                
            return {"statistics": statistics, "activeUsers": activeUsers}
        
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
        
        @self.router.get("/logfile")
        async def get_log_file():
            return FileResponse(path=self.api_logging_handler.get_log_file(), filename="log.txt", media_type="text/plain")
        
        @self.router.get("/logs")
        async def get_log_json():
            return self.api_logging_handler.get_log_json()