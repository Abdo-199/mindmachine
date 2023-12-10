# user_router.py
from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse
from fileSystemHandler import FileSystemHandler
from statisticsHandler import StatisticsHandler
from ldap3 import Server, Connection
from Neural_Search.Helper_Modules.Qdrant import Qdrant
from dataDefinitions import *
from database import log_search
from typing import List
import config

class UserRouter(APIRouter):
    def __init__(self, qd_client: Qdrant, file_system_handler: FileSystemHandler):
        super().__init__()
        self.qdClient = qd_client
        self.file_system_handler = file_system_handler
        self.setup_routes()

    def setup_routes(self):
        @self.post("/login")
        async def validate_credentials(request: LoginRequestModel) -> LoginResponseModel:
            ldap_server = Server(config.ldap_server)
            base_dn = config.base_dn
            username = f'cn={request.username},ou=idmusers,' + base_dn
 
            conn = Connection(ldap_server, user=username, password=request.password, auto_bind=False)
            conn.start_tls()

            if conn.bind():
                return LoginResponseModel(isAuthenticated=True, isAdmin=True)
          
            return LoginResponseModel(isAuthenticated=False, isAdmin=False)

        @self.get("/search")
        async def search(user_id: str, query: str):
            try:

                # Perform the search using Qdrant
                results = self.qdClient.search(user_id, query)

                # TODO: return wert/objekt mit frontend abstimmen

                # TODO: Automate the table creation
                # Log the search in the database
                # log_search(student_number, query) 

                return results
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
            pass

        @self.post("/upload/{user_id}")
        async def upload_document(user_id, files: list[UploadFile] = File(...)):
            self.file_system_handler.upload(user_id, files)
            return True

        @self.get("/document")
        async def get_document(user_id: str, document_name: str):
            # ... Get document logic ...
            pass

        @self.delete("/deleteDocument/{user_id}/{document_id}")
        async def delete_document(user_id, document_id):
            self.file_system_handler.delete_document(user_id, document_id)
            return True

        @self.get("/filestructure/{user_id}")
        async def get_file_structure(user_id):
            return self.file_system_handler.get_fs_for_user(user_id)

        @self.put("/editDocumentName/{user_id}")
        async def edit_document_name(user_id, request: RenameFileModel):
            self.file_system_handler.edit_document_name(user_id, request.old_name, request.new_name)
            return True
