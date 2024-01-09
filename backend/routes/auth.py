from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Annotated
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import config
from ldap3 import Server, Connection
from databaseHandler import DatabaseHandler



class Token(BaseModel):
    access_token: str
    token_type: str

auth_router = APIRouter(prefix='/auth',tags=['auth'])

class AuthAPI:
    def __init__(self, databaseHandler: DatabaseHandler):
        self.databaseHandler = databaseHandler
        self.setup_routes()
    
    __SECRET_KEY = 'M/DMRk2MTErpMl6PQayoya7KrGKcks2yytzXeDOvJ8rEGUDKwf9qimZ1+j5w831DKZaew0WoZP76ol8lvJjAvQ=='
    __ALGORITHM = 'HS256'
    __oath2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

    def authenticate_user(self, user_id: str, password: str):
        
        ldap_server = Server(config.ldap_server)
        base_dn = config.base_dn
        username = f'cn={user_id},ou=idmusers,' + base_dn

        conn = Connection(ldap_server, user=username, password=password, auto_bind=False)
        conn.start_tls()

        if not conn.bind():
            return False
        user = self.databaseHandler.get_user(user_id)
        if user is None:
            self.databaseHandler.add_user(user_id, False)
            user = self.databaseHandler.get_user(user_id)
        return user

    def create_access_token(self, user_id: str, is_admin: bool, expires_delta: timedelta):
        encode = {'sub': user_id, 'is_admin': is_admin}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, AuthAPI.__SECRET_KEY, AuthAPI.__ALGORITHM)

    async def get_current_user(token: Annotated[str, Depends(__oath2_bearer)]):
        try:
            payload = jwt.decode(token, AuthAPI.__SECRET_KEY, algorithms=[AuthAPI.__ALGORITHM])
            user_id: int = payload.get('sub')
            is_admin: str = payload.get('is_admin')
            if user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                    detail='Could not validate credentials')
        
            return {'user_id': user_id, 'is_admin': is_admin}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail='Could not validate credentials')
        
    def setup_routes(self):
        @auth_router.post("/token", response_model=Token)
        async def login_for_access_token(form_data : Annotated[OAuth2PasswordRequestForm, Depends()]):
            user = self.authenticate_user(form_data.username, form_data.password)
            if not user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                        detail='Could not validate credentials')
            timeout = self.databaseHandler.get_admin_settings().logout_timer
            token = self.create_access_token(user.user_id, user.is_admin, timedelta(minutes=timeout))
            return {'access_token': token, 'token_type': 'bearer'}
