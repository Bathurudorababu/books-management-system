from fastapi import FastAPI
from app.routes import auth, books
from app.database import create_indexes

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(books.router, prefix="/books", tags=["Books"])
