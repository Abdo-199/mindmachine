from fastapi import FastAPI, APIRouter
from fileSystemHandler import FileSystemHandler
from statisticsHandler import StatisticsHandler
from ldap3 import Server, Connection
from dataDefinitions import *

class API:

    def __init__(self, dataBase) -> None:
        self.app = FastAPI()
        self.db = dataBase
        self.router = APIRouter()
        self.stats = StatisticsHandler(self.db)
        self.fs = FileSystemHandler("/")

        self.setup_routes()
        self.app.include_router(self.router)

    def setup_routes(self):

        #validate HTW Credentials
        @self.router.post("/login")
        async def validate_credentials(request: LoginModel):

            ldap_server = Server('ldap://login-dc-01.login.htw-berlin.de')
            base_dn = 'dc=login,dc=htw-berlin,dc=de'
            username = f'cn={request.username},ou=idmusers,' + base_dn
 
            conn = Connection(ldap_server, user=username, password=request.password, auto_bind=False)
            conn.start_tls()

            if conn.bind():
                print("LDAP authentication successful")
                return {"isAuthenticated": True, "isAdmin": True}
          
            print("LDAP authentication failed")
            return {"isAuthenticated": False, "isAdmin": False}
        
        #search
        @self.router.get("/search/{query}")
        async def search(query):
            return True
        
        #upload document for user id
        @self.router.post("/upload/{user_id}")
        async def upload_document(user_id):
            return True

        #get document
        @self.router.get("/document/{document_id}")
        async def get_document(document_id):
            return True

        #delete document
        @self.router.delete("/document/{document_id}")
        async def delete_document(document_id):
            return True
        
        #send file structure
        @self.router.get("/filestructure/{user_id}")
        async def get_file_structure(user_id):
            return True
        
        #edit document name
        @self.router.put("/document/{document_id}")
        async def edit_document_name(document_id):
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

        

