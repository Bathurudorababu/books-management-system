from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)

db = client["books_management"]

user_collection = db["users"]
token_collection = db["tokens"]

book_collection = db["books"]