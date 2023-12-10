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



class API:

    def __init__(self) -> None:
        self.app = FastAPI()
        self.router = APIRouter()
        self.qdClient = Qdrant()
        self.stats = StatisticsHandler(self.qdClient)
        self.file_system_handler = FileSystemHandler(self.qdClient)
        self.setup_routes()
        self.app.include_router(self.router)

    def setup_routes(self):

        #validate HTW Credentials
        @self.router.post("/login")
        async def validate_credentials(request: LoginRequestModel) -> LoginResponseModel:

            ldap_server = Server(config.ldap_server)
            base_dn = config.base_dn
            username = f'cn={request.username},ou=idmusers,' + base_dn
 
            conn = Connection(ldap_server, user=username, password=request.password, auto_bind=False)
            conn.start_tls()

            if conn.bind():
                return LoginResponseModel(isAuthenticated=True, isAdmin=True)
          
            return LoginResponseModel(isAuthenticated=False, isAdmin=False)
        
        #search
        @self.router.get("/search")
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
        
        #upload document for user id to the file system and qdrant
        @self.router.post("/upload/{user_id}")
        async def upload_document(user_id, files: list[UploadFile] = File(...)):
            self.file_system_handler.upload(user_id, files)
            return True

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