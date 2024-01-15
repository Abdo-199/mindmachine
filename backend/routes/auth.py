from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Annotated
from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import config
from ldap3 import Server, Connection
from databaseHandler import DatabaseHandler
import os

from logHandler import LogHandler

class Token(BaseModel):
    """
    Represents an access token.
    """
    access_token: str
    token_type: str
    is_admin: bool

auth_router = APIRouter(prefix='/auth',tags=['auth'])

class AuthAPI:
    """
    Represents the authentication API.
    """
    def __init__(self, databaseHandler: DatabaseHandler):
        """
        Initializes an instance of AuthAPI.

        Parameters:
        - databaseHandler (DatabaseHandler): The database handler object.

        Returns:
        - None
        """
        self.databaseHandler = databaseHandler
        self.setup_routes()
        self.logger = LogHandler(name="API").get_logger()
    
    __SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback_secret")
    __ALGORITHM = 'HS256'
    __oath2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

    def authenticate_user(self, user_id: str, password: str):
        """
        Authenticates a user by connecting to an LDAP server and checking the provided credentials.

        Args:
            user_id (str): The user ID or username.
            password (str): The user's password.

        Returns:
            User: The authenticated user object if the credentials are valid, else False.
        """
        
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
        """
        Creates an access token for the given user.

        Args:
            user_id (str): The ID of the user.
            is_admin (bool): Indicates whether the user is an admin or not.
            expires_delta (timedelta): The expiration time for the access token.

        Returns:
            str: The generated access token.
        """
        encode = {'sub': user_id, 'is_admin': is_admin}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, AuthAPI.__SECRET_KEY, AuthAPI.__ALGORITHM)

    async def get_current_user(token: Annotated[str, Depends(__oath2_bearer)]):
        """
        Retrieves the current user based on the provided token.

        Args:
            token (str): The JWT token used for authentication.

        Returns:
            dict: A dictionary containing the user_id and is_admin status of the current user.

        Raises:
            HTTPException: If the token is invalid or the credentials cannot be validated.
        """
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
        """
        Sets up the routes for authentication.

        This method defines the route for generating access tokens
        based on the provided credentials. It also logs the user's
        login activity and updates the last login timestamp in the database.

        Returns:
            None
        """
        @auth_router.post("/token", response_model=Token)
        async def get_access_token(form_data : Annotated[OAuth2PasswordRequestForm, Depends()]):
            user = self.authenticate_user(form_data.username, form_data.password)
            if not user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                        detail='Could not validate credentials')
            if user.is_admin:
                self.databaseHandler.update_last_login(user.user_id)
                self.logger.info(f"User {user.user_id} logged in as admin")
            else:
                self.databaseHandler.update_last_login(user.user_id)
                self.logger.info(f"User {user.user_id} logged in as user")
            
            timeout = self.databaseHandler.get_admin_settings().logout_timer
            token = self.create_access_token(user.user_id, user.is_admin, timedelta(minutes=timeout))
            return {'access_token': token, 'token_type': 'bearer', 'is_admin': user.is_admin}
