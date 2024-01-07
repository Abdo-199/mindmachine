from pydantic import BaseModel

class LoginRequestModel(BaseModel):
    username: str
    password: str

class LoginResponseModel(BaseModel):
    isAuthenticated: bool
    isAdmin: bool
    access_token: str = None
    token_type: str = None


class RenameFileModel(BaseModel):
    old_name: str
    new_name: str

class SearchQueryModel(BaseModel):
    user_id: str
    query: str

class GetDocumentModel(BaseModel):
    user_id: str
    document_name: str