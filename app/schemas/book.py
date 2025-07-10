from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str | None = None