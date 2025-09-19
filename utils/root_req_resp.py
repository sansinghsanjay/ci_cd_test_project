# python imports
from pydantic import BaseModel

# root endpoint - Request model
class RootRequestModel(BaseModel):
    fastapi_access_key: str

# root endpoint - Response model
class RootResponseModel(BaseModel):
    response: str
