from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    genre: str | None = None
    user_id: UUID
    created_at: datetime