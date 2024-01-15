from api import API
from fastapi.middleware.cors import CORSMiddleware
import logHandler
from databaseHandler import DatabaseHandler
import config
from Neural_Search.Qdrant import Qdrant
from fileSystemHandler import FileSystemHandler
from routes.users import UserAPI, user_router
from routes.admin import AdminAPI, admin_router
from routes.auth import AuthAPI,auth_router

# api = API()
# app = api.app
from fastapi import FastAPI

app = FastAPI(root_path="/api")
qdClient = Qdrant()
databaseHandler = DatabaseHandler(config.data_directory, config.database_name)
file_system_handler = FileSystemHandler(qdClient)
auth_mng = AuthAPI(databaseHandler)
user_mng = UserAPI(qdClient,file_system_handler, databaseHandler)
admin_mng = AdminAPI(file_system_handler, databaseHandler)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(admin_router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    pass
    
    

if __name__ == '__main__':
    logger = logHandler.LogHandler(name="main").get_logger()
    logger.info("Application invoked")
    logger.info("Starting FastAPI server")    
    # start uvicorn server to host the FastAPI app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    main()