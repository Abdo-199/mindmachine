from pydantic import BaseModel

class LoginRequestModel(BaseModel):
    username: str
    password: str

class LoginResponseModel(BaseModel):
    isAuthenticated: bool
    isAdmin: bool


class RenameFileModel(BaseModel):
    old_name: str
    new_name: str