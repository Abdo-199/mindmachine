from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fileSystemHandler import FileSystemHandler
from statisticsHandler import StatisticsHandler
from ldap3 import Server, Connection
from qdrant import QDrant
from dataDefinitions import *
from database import log_search
from typing import List


class VectorModel(BaseModel):

    pass


class API:

    def __init__(self, dataBase) -> None:
        self.app = FastAPI()
        self.db = dataBase
        self.router = APIRouter()
        self.stats = StatisticsHandler(self.db)
        self.file_system_handler = FileSystemHandler()

        self.setup_routes()
        self.app.include_router(self.router)

    def setup_routes(self):

        #validate HTW Credentials
        @self.router.post("/login")
        async def validate_credentials(request: LoginRequestModel) -> LoginResponseModel:

            ldap_server = Server('ldap://login-dc-01.login.htw-berlin.de')
            base_dn = 'dc=login,dc=htw-berlin,dc=de'
            username = f'cn={request.username},ou=idmusers,' + base_dn
 
            conn = Connection(ldap_server, user=username, password=request.password, auto_bind=False)
            conn.start_tls()

            if conn.bind():
                return LoginResponseModel(isAuthenticated=True, isAdmin=True)
          
            return LoginResponseModel(isAuthenticated=False, isAdmin=False)
        
        #search
        @self.router.get("/search/{query}")
        async def search(query):
            return True
        
        #upload document for user id
        @self.router.post("/upload/{user_id}")
        async def upload_document(user_id, files: list[UploadFile] = File(...)):
            self.file_system_handler.upload(user_id, files)
            return True

        #get document
        @self.router.get("/document/{document_id}")
        async def get_document(document_id):
            return True

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
            return True
        

        #get used disk space
        @self.router.get("/diskusage")
        async def get_disk_usage():
            return True
        
        #change disk space limit
        @self.router.put("/diskusage")
        async def change_disk_usage():
            return True
        
        # get statistics
        @self.router.get("/statistics")
        async def get_statistics():
            return True
        
        # get and set auto-logout time
        @self.router.get("/autologout")
        async def get_auto_logout():
            return True
        
        @self.router.put("/autologout")
        async def set_auto_logout():
            return True
        
        #get search history of user
        @self.router.get("/searchhistory/{user_id}")
        async def get_search_history(user_id):
            return True

        @self.router.post("/search")
        async def search(query: str, student_number: int):
            try:
                # Perform the search using Qdrant
                results = QDrant().search_vectors(collection_name="your_collection", query_vector=query)

                # Log the search in the database
                log_search(student_number, query)

                return results
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.post("/create_collection/{collection_name}")
        async def create_collection(collection_name: str):
            try:
                qdrant_client = QDrant()
                qdrant_client.create_collection(collection_name)
                return {"message": "Collection created successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.post("/add_vectors/{collection_name}")
        async def add_vectors(collection_name: str, vectors: List[VectorModel]):
            try:
                qdrant_client = QDrant()
                qdrant_client.add_vectors(collection_name, vectors)
                return {"message": "Vectors added successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.delete("/delete_vectors/{collection_name}")
        async def delete_vectors(collection_name: str, vector_ids: List[int]):
            try:
                qdrant_client = QDrant()
                qdrant_client.delete_vectors(collection_name, vector_ids)
                return {"message": "Vectors deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.post("/add_text/{collection_name}/{vector_id}")
        async def add_text(collection_name: str, vector_id: int, text: str):
            try:
                qdrant_client = QDrant()
                qdrant_client.add_text_as_vector(collection_name, text, vector_id)
                return {"message": "Text added as vector successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        

