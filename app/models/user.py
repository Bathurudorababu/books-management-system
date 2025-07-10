from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class User(BaseModel):
    id: UUID
    fullname: str
    email: EmailStr
    hashed_password: str
    created_at: datetime