from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException, Depends
from fastapi.responses import FileResponse
from dataDefinitions import RenameFileModel
from databaseHandler import DatabaseHandler
from fileSystemHandler import FileSystemHandler
from Neural_Search.Qdrant import Qdrant
from typing import Annotated
from starlette import status
from .auth import AuthAPI
import config

user_router = APIRouter(prefix='/user', tags=['user'])

class UserAPI:
    def __init__(self, qdClient: Qdrant, file_system_handler: FileSystemHandler ,databaseHandler: DatabaseHandler):
        self.router = APIRouter(prefix='/user', tags=['user'])
        self.qdClient = qdClient
        self.DatabaseHandler = databaseHandler
        self.file_system_handler = file_system_handler
        self.setup_routes()
        
    user_dependency = Annotated[dict, Depends(AuthAPI.get_current_user)]

    def check_user_authentication(self, user: user_dependency):
        """
        Checks if the user is authenticated.
        
        Args:
        user: The user object to check.

        Raises:
        HTTPException: If the user is not authenticated.
        """
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Authentication failed"
            )

    def setup_routes(self):
        @user_router.get("/search", status_code=status.HTTP_200_OK)
        async def search(user: UserAPI.user_dependency, query: str):
            self.check_user_authentication(user)
            try:
                # Perform the search using Qdrant
                results = self.qdClient.search(user.get('user_id'), query)

                self.DatabaseHandler.log_search(user.get('user_id'), query) 

                return results
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        #upload document for user id to the file system and qdrant
        @user_router.post("/upload", status_code=status.HTTP_201_CREATED)
        async def upload_document(user: UserAPI.user_dependency, files: list[UploadFile] = File(...)):
            self.check_user_authentication(user)
            status_return = self.file_system_handler.upload(user.get('user_id'), files)
            return status_return

        #Sends a pdf file to the Website for the viewer
        @user_router.get("/document/{document_name}",status_code=status.HTTP_200_OK)
        async def get_document(user: UserAPI.user_dependency, document_name :str):  # (user_id: str, document_name: str):
            self.check_user_authentication(user)
            filepath = self.file_system_handler.get_document_path(user.get('user_id'), document_name)
            if not filepath:
                raise HTTPException(status_code=404, detail="File not found")
            return FileResponse(path=filepath, filename=document_name, media_type="application/pdf")

        #delete document
        @user_router.delete("/deleteDocument/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_document(user: UserAPI.user_dependency, document_id):
            self.check_user_authentication(user)
            self.file_system_handler.delete_document(user.get('user_id'), document_id)
            return True
        
        #send file structure
        @user_router.get("/filestructure", status_code=status.HTTP_200_OK)
        async def get_file_structure(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            return self.file_system_handler.get_fs_for_user(user.get('user_id'))
        
        #edit document name
        @user_router.put("/editDocumentName", status_code=status.HTTP_204_NO_CONTENT)
        async def edit_document_name(user: UserAPI.user_dependency, request: RenameFileModel):
            self.check_user_authentication(user)
            self.file_system_handler.edit_document_name(user.get('user_id'), request.old_name, request.new_name)
            self.qdClient.rename_doc(user.get('user_id'), request.old_name, request.new_name)
            return True
        
        #edit document name
        @user_router.head("/revectorize", status_code=status.HTTP_200_OK)
        async def revectorize(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            self.qdClient.revectorize_all()
            return True
        
        # get and set auto-logout time
        @user_router.get("/autologout", status_code=status.HTTP_200_OK)
        async def get_auto_logout(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            settings = self.DatabaseHandler.get_admin_settings().logout_timer
            return settings
