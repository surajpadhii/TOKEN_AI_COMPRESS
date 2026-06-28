from pydantic import BaseModel


class APIKeyCreate(BaseModel):
    client_name: str
    plan: str = "Free"


class APIKeyResponse(BaseModel):
    id: int
    client_name: str
    api_key: str
    plan: str
    active: bool

    class Config:
        from_attributes = True