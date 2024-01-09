from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    name: str
    is_active: bool
    

class UserCreate(BaseModel):
    name: str
    