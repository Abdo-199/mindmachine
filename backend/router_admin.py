from router_user import UserRouter
from Neural_Search.Helper_Modules.Qdrant import Qdrant
from fileSystemHandler import FileSystemHandler

class AdminRouter(UserRouter):
    def __init__(self, qd_client: Qdrant, file_system_handler: FileSystemHandler):
        super().__init__(qd_client, file_system_handler)
        self.setup_admin_routes()

    def setup_admin_routes(self):
        @self.get("/diskusage")
        async def get_disk_usage():
            return True

        @self.put("/diskusage")
        async def change_disk_usage():
            return True

        @self.get("/statistics")
        async def get_statistics():
            return True

        @self.get("/autologout")
        async def get_auto_logout():
            return True

        @self.put("/autologout")
        async def set_auto_logout():
            return True

        @self.get("/searchhistory/{user_id}")
        async def get_search_history(user_id):
            return True
