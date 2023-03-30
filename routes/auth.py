from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models.user import UserIn, UserOut, UserCreate, UserUpdate, UserRemove
from typing import Optional, List
from database import db_users
from config import SECRET_KEY, ALGORITHM
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from slowapi import Limiter
from slowapi.util import get_remote_address

# Create a router
auth_router = APIRouter()

# Set up OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing using Bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    decoded = decode_jwt_token(token)
    return decoded


# Function to authenticate user
def authenticate_user(username: str, password: str) -> Optional[UserOut]:
    user = db_users.find_one(username)
    if user and verify_password(password, user["password"]):
        return UserOut(**user)
    return None


@auth_router.post("/token")
async def generate_token(user: UserIn):
    user_in_db = authenticate_user(user.username, user.password)
    if user_in_db is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    token = create_jwt_token({"sub": user_in_db.username})
    return {"access_token": token, "token_type": "bearer"}


@auth_router.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["sub"]}


@auth_router.get("/secure_data")
async def get_secure_data(current_user: dict = Depends(get_current_user)):
    return {"data": "This is secure data available only for authenticated users."}


# Function to add a user to the database
def add_user(user: UserCreate) -> UserOut:
    if db_users.find_one(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    hashed_password = get_password_hash(user.password)
    new_user = {"username": user.username, "password": hashed_password}
    db_users.insert(new_user)
    return UserOut(**new_user)


# Function to remove a user from the database
def remove_user(username: str) -> UserOut:
    user = db_users.find_one(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db_users.delete(username)
    return UserOut(**user)


@auth_router.post("/users/add", response_model=UserOut)
async def create_user(user: UserCreate):
    return add_user(user)


@auth_router.delete("/users/remove/{username}", response_model=UserOut)
async def delete_user(username: str, current_user: dict = Depends(get_current_user)):
    # Add any necessary authorization checks here
    return remove_user(username)


# Function to update a user in the database
def update_user(username: str, updated_user: UserUpdate) -> UserOut:
    user = db_users.find_one(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if updated_user.password:
        hashed_password = get_password_hash(updated_user.password)
        user["password"] = hashed_password

    db_users.update(username, user)
    return UserOut(**user)


@auth_router.put("/users/update/{username}", response_model=UserOut)
async def update_user_info(username: str, updated_user: UserUpdate, current_user: dict = Depends(get_current_user)):
    # Add any necessary authorization checks here
    return update_user(username, updated_user)