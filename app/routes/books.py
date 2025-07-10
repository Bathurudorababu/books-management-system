from fastapi import APIRouter, HTTPException, Depends, Query
from app.schemas import book as schemas
from app.utils import *
from app.database import book_collection
from uuid import uuid4
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_book(book: schemas.BookCreate, user: dict = Depends(validate_token)):
    book_doc = {
        "id": str(uuid4()),
        "title": book.title,
        "author": book.author,
        "genre": book.genre or "",
        "user_id": user["id"],
        "created_at": datetime.utcnow()
    }
    # print(user)
    await book_collection.insert_one(book_doc)
    return {"message": "Book successfully created"}

@router.get("/")
async def list_books(genre: str = Query(None),user: dict = Depends(validate_token)):
    query = {"genre": genre} if genre else {}
    books = await book_collection.find(query).to_list(100)
    for book in books:
        book["_id"] = str(book["_id"])
    return books

@router.get("/{book_id}")
async def get_book(book_id: str, user: dict = Depends(validate_token)):
    book = await book_collection.find_one({"id": book_id})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book["_id"] = str(book["_id"])
    return book


@router.delete("/{book_id}")
async def delete_book(book_id: str, user: dict = Depends(validate_token)):
    book = await book_collection.find_one({"id": book_id})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book["user_id"] != user["id"]:
        raise HTTPException(status_code=403, detail="You are not allowed to delete this book")
    await book_collection.delete_one({"id": book_id})
    return {"message": "Book successfully deleted",
            "book_id":book_id}
