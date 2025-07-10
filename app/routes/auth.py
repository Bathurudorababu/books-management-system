from fastapi import APIRouter, HTTPException, Depends,status
from uuid import uuid4
from datetime import datetime, timedelta
from app.schemas import user as schemas
from app.utils import hash_password, verify_password, create_access_token, validate_token
from app.database import user_collection, token_collection 

router = APIRouter()

@router.post("/signup")
async def signup(user: schemas.UserCreate):

    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    
    hashed_pw = hash_password(user.password)
    user_dict = {
        "id": str(uuid4()),  
        "email": user.email,
        "fullname":user.fullname,
        "hashed_password": hashed_pw,
        "created_at": datetime.utcnow()
    }

    try:
        await user_collection.insert_one(user_dict)
        return {"message": "User successfully created"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/login")
async def login(user: schemas.UserLogin):
    db_user = await user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": db_user["id"], "email": db_user["email"]})

    await token_collection.insert_one({
        "token": access_token,
        "user_id": db_user["id"],
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(hours=8)
    })

    # print("User ID:", db_user["id"])
    # print("Access Token Payload:", jwt.decode(access_token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")]))


    return {
        "message":"User successfully Logged-In",
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
async def get_me(current_user: dict = Depends(validate_token)):
    return current_user