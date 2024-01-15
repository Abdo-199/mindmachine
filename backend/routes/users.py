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
from logHandler import LogHandler

user_router = APIRouter(tags=['user'])

class UserAPI:
    """
    Represents the User API class.

    This class handles the routes and functionality related to user operations.

    Attributes:
        qdClient (Qdrant): The Qdrant client.
        file_system_handler (FileSystemHandler): The file system handler.
        databaseHandler (DatabaseHandler): The database handler.
    """
    def __init__(self, qdClient: Qdrant, file_system_handler: FileSystemHandler ,databaseHandler: DatabaseHandler):
        """
        Initializes the Users API class.

        Args:
            qdClient (Qdrant): The Qdrant client.
            file_system_handler (FileSystemHandler): The file system handler.
            databaseHandler (DatabaseHandler): The database handler.
        """
        self.qdClient = qdClient
        self.DatabaseHandler = databaseHandler
        self.logger = LogHandler(name="API").get_logger()

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
        """
        Sets up the routes for the User API.

        This method defines various routes for handling user-related operations such as searching, uploading documents,
        downloading documents, deleting documents, retrieving file structure, editing document names, revectorizing documents,
        retrieving storage information, retrieving search history, retrieving disk usage, and retrieving auto-logout settings.

        Each route is defined as an asynchronous function using the FastAPI framework's decorator syntax.

        Returns:
            None
        """
        @user_router.get("/search", status_code=status.HTTP_200_OK)
        async def search(user: UserAPI.user_dependency, query: str):
            self.check_user_authentication(user)
            try:
                # Perform the search using Qdrant
                results = self.qdClient.search(user.get('user_id'), query)
                self.DatabaseHandler.log_search(user.get('user_id'), query) 
                self.logger.info(f"User {user.get('user_id')} searched for {query}")
                return results
            except Exception as e:
                self.logger.info(f"User {user.get('user_id')} failed to search for {query}")
                raise HTTPException(status_code=500, detail=str(e))
        
        #upload document for user id to the file system and qdrant
        @user_router.post("/upload", status_code=status.HTTP_201_CREATED)
        async def upload_document(user: UserAPI.user_dependency, files: list[UploadFile] = File(...)):
            self.check_user_authentication(user)
            status_return = self.file_system_handler.upload(user.get('user_id'), files)
            self.logger.info(f"User {user.get('user_id')} uploaded {len(files)} files: {status_return}")
            return status_return

        #Sends a pdf file to the Website for the viewer
        @user_router.get("/document",status_code=status.HTTP_200_OK)
        async def get_document(user: UserAPI.user_dependency, document_name :str):  # (user_id: str, document_name: str):
            self.check_user_authentication(user)
            filepath = self.file_system_handler.get_document_path(user.get('user_id'), document_name)
            if not filepath:
                self.logger.error(f"User {user.get('user_id')} failed to download {document_name}")
                raise HTTPException(status_code=404, detail="File not found")
            self.logger.info(f"User {user.get('user_id')} downloaded {document_name}")
            return FileResponse(path=filepath, filename=document_name, media_type="application/pdf")

        #delete document
        @user_router.delete("/deleteDocument/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete_document(user: UserAPI.user_dependency, document_id):
            self.check_user_authentication(user)
            self.logger.info(f"User {user.get('user_id')} deleted {document_id}")
            self.file_system_handler.delete_document(user.get('user_id'), document_id)
            return True
        
        #send file structure
        @user_router.get("/filestructure", status_code=status.HTTP_200_OK)
        async def get_file_structure(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            self.logger.info(f"User {user.get('user_id')} requested file structure")
            return self.file_system_handler.get_fs_for_user(user.get('user_id'))
        
        #edit document name
        @user_router.put("/editDocumentName", status_code=status.HTTP_204_NO_CONTENT)
        async def edit_document_name(user: UserAPI.user_dependency, request: RenameFileModel):
            self.check_user_authentication(user)
            self.file_system_handler.edit_document_name(user.get('user_id'), request.old_name, request.new_name)
            self.qdClient.rename_doc(user.get('user_id'), request.old_name, request.new_name)
            self.logger.info(f"User {user.get('user_id')} renamed {request.old_name} to {request.new_name}")
            return True
        
        #edit document name
        @user_router.head("/revectorize", status_code=status.HTTP_200_OK)
        async def revectorize(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            self.qdClient.revectorize_all()
            self.logger.info(f"Revectorized all documents")
            return True
        
        #get storage for one specific user
        @user_router.get("/current_storage_usage", status_code=status.HTTP_200_OK)
        async def get_storage_info(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            total_size = self.file_system_handler.get_file_size_for_user(user.get('user_id'), inBytes=True)
            return total_size

        #get search history of user
        @user_router.get("/searchhistory", status_code=status.HTTP_200_OK)
        async def get_search_history(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            raw_search_history = self.DatabaseHandler.get_search_history(user.get('user_id'))
            search_history = []
            for search in raw_search_history:
                search_history.append({'query': search.search_query, 'date': search.timestamp})
            return search_history
        
        #gets the storage capacity of all users
        @user_router.get("/diskusage/user", status_code=status.HTTP_200_OK)
        async def get_disk_usage(user: UserAPI.user_dependency, inBytes: str):
            self.check_user_authentication(user)
            disk_usage = self.DatabaseHandler.get_admin_settings().user_max_disk_space
            if inBytes == "false":
                disk_usage = self.file_system_handler.convert_bytes_to_gigabyte(disk_usage)
            return disk_usage

        # get and set auto-logout time
        @user_router.get("/autologout", status_code=status.HTTP_200_OK)
        async def get_auto_logout(user: UserAPI.user_dependency):
            self.check_user_authentication(user)
            settings = self.DatabaseHandler.get_admin_settings().logout_timer
            return settings
