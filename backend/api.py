from fastapi import FastAPI
from fileSystemHandler import FileSystemHandler
from Neural_Search.Helper_Modules.Qdrant import Qdrant
from dataDefinitions import *
from router_user import UserRouter
from router_admin import AdminRouter




class API:

    def __init__(self) -> None:
        self.app = FastAPI()
        self.qdClient = Qdrant()
        self.file_system_handler = FileSystemHandler(self.qdClient)

        # Initialize and include User and Admin routers
        user_router = UserRouter(self.qdClient, self.file_system_handler)
        admin_router = AdminRouter(self.qdClient, self.file_system_handler)

        self.app.include_router(user_router, prefix="/user")
        self.app.include_router(admin_router, prefix="/admin")