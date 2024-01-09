from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import FileResponse
from Neural_Search.Qdrant import Qdrant
from databaseHandler import DatabaseHandler
from fileSystemHandler import FileSystemHandler
from routes.users import UserAPI
from statisticsHandler import StatisticsHandler
from starlette import status
from datetime import datetime

admin_router = APIRouter(prefix='/admin', tags=['admin'])

class AdminAPI():
    def __init__(self, file_system_handler: FileSystemHandler, databaseHandler: DatabaseHandler):
        self.DatabaseHandler = databaseHandler
        self.file_system_handler = file_system_handler
        
        self.setup_admin_routes()
        

    def check_admin_authorization(self, user: UserAPI.user_dependency):
        """
        Checks if the user is authenticated and an admin.
        
        Args:
        user: The user object to check.

        Raises:
        HTTPException: If the user is not authenticated or not an admin.
        """
        if not user or not user.get('is_admin'):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Authentication failed"
            )
        
    def setup_admin_routes(self):

        #get used disk space
        @admin_router.get("/diskusage", status_code=status.HTTP_200_OK)
        async def get_disk_usage():
            disk_usage = self.DatabaseHandler.get_admin_settings().max_disk_space
            disk_usage = self.file_system_handler.convert_bytes_to_gigabyte(disk_usage)
            return disk_usage
        
        #change disk space limit
        @admin_router.put("/diskusage", status_code=status.HTTP_204_NO_CONTENT)
        async def change_disk_usage(admin: UserAPI.user_dependency, disk_usage: float):
            self.check_admin_authorization(admin)
            self.DatabaseHandler.update_admin_settings(max_disk_space = disk_usage)
        
          
        #gets the storage capacity of all users
        @admin_router.get("/diskusage/user", status_code=status.HTTP_200_OK)
        async def get_disk_usage(admin: UserAPI.user_dependency):
            self.check_admin_authorization(admin)
            disk_usage = self.DatabaseHandler.get_admin_settings().user_max_disk_space
            disk_usage = self.file_system_handler.convert_bytes_to_gigabyte(disk_usage)
            return disk_usage
        
        #change disk space limit for user
        @admin_router.put("/diskusage/user", status_code=status.HTTP_204_NO_CONTENT)
        async def change_disk_usage(admin: UserAPI.user_dependency, disk_usage: float):
            self.check_admin_authorization(admin)
            self.DatabaseHandler.update_admin_settings(user_max_disk_space = disk_usage)
            return True
        
        #get storage for all users
        @admin_router.get("/storage_usage", status_code=status.HTTP_200_OK)
        async def get_storage_info(admin: UserAPI.user_dependency):
            self.check_admin_authorization(admin)
            total_size = self.file_system_handler.get_total_file_size_for_all_users()
            return total_size
        

        #get storage for one specific user
        @admin_router.get("/storage_usage/{user_id}", status_code=status.HTTP_200_OK)
        async def get_storage_info(admin: UserAPI.user_dependency, user_id):
            self.check_admin_authorization(admin)
            total_size = self.file_system_handler.get_file_size_for_user(user_id)
            return total_size

        # get statistics
        @admin_router.get("/statistics", status_code=status.HTTP_200_OK)
        async def get_statistics(admin: UserAPI.user_dependency):
            self.check_admin_authorization(admin)
            activeUsers = self.DatabaseHandler.get_active_users()
            statistics = self.DatabaseHandler.get_all_users()

            for user in statistics:
                user.used_storage = self.file_system_handler.get_file_size_for_user(user.user_id)
                
            return {"statistics": statistics, "activeUsers": activeUsers}
        
        
        @admin_router.put("/autologout",status_code=status.HTTP_204_NO_CONTENT)
        async def set_auto_logout(admin: UserAPI.user_dependency,logout_timer: float):
            self.check_admin_authorization(admin)
            self.DatabaseHandler.update_admin_settings(logout_timer = logout_timer)
            return True
        
        #get search history of user
        @admin_router.get("/searchhistory/{user_id}", status_code=status.HTTP_200_OK)
        async def get_search_history(admin: UserAPI.user_dependency, user_id):
            self.check_admin_authorization(admin)
            raw_search_history = self.DatabaseHandler.get_search_history(user_id)
            search_history = []
            for search in raw_search_history:
                search_history.append({'query': search.search_query, 'date': search.timestamp})
            return search_history
        
        @admin_router.get("/getnumberofaskedquestions", status_code=status.HTTP_200_OK)
        async def get_number_of_asked_questions(admin: UserAPI.user_dependency, given_timestamp:datetime = datetime(2000, 1, 1)):
            self.check_admin_authorization(admin)
            return self.DatabaseHandler.get_number_of_asked_questions(given_timestamp)
        
        @admin_router.get("/logfile", status_code=status.HTTP_200_OK)
        async def get_log_file(admin: UserAPI.user_dependency):
            self.check_admin_authorization(admin)
            return FileResponse(path=self.logger.get_log_file(), filename="log.txt", media_type="text/plain")
        
        @admin_router.get("/logs", status_code=status.HTTP_200_OK)
        async def get_log_json(admin: UserAPI.user_dependency):
            self.check_admin_authorization(admin)
            return self.logger.get_log_json()

        

        