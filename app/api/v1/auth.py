from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.user import UserIn, UserOut, UserCreate, UserUpdate
from typing import Optional
from app.core.database import db_users
from app.core.config import SECRET_KEY, ALGORITHM
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.models.exceptions import CustomNotFoundException
import logging

logger = logging.getLogger(__name__)

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
        raise CustomNotFoundException("Invalid token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    decoded = decode_jwt_token(token)
    logging.info(f"User {decoded['username']} authenticated")
    return decoded


# Function to authenticate user
def authenticate_user(username: str, password: str) -> Optional[UserOut]:
    user = db_users.find_one(username)
    if user and verify_password(password, user["password"]):
        logging.info(f"User {username} authenticated")
        return UserOut(**user)
    logging.info(f"User {username} not found")
    return None


# Function to add a user to the database
def add_user(user: UserCreate) -> UserOut:
    if db_users.find_one(user.username):
        raise CustomNotFoundException("User already exists")

    hashed_password = get_password_hash(user.password)
    new_user = {"username": user.username, "password": hashed_password}
    db_users.insert(new_user)
    logging.info(f"New user created: {user.username} and pending validation")
    return UserOut(**new_user)


# Function to remove a user from the database
def remove_user(username: str) -> UserOut:
    user = db_users.find_one(username)
    if not user:
        raise CustomNotFoundException("User not found")

    db_users.delete(username)
    logging.info(f"User deleted: {username}")
    return UserOut(**user)


# Function to update a user in the database
def update_user(username: str, updated_user: UserUpdate) -> UserOut:
    user = db_users.find_one(username)
    if not user:
        raise CustomNotFoundException("User not found")

    if updated_user.password:
        hashed_password = get_password_hash(updated_user.password)
        user["password"] = hashed_password

    db_users.update_one({'username': username}, {"$set": {'status': "validated"}})
    logging.info(f"New user validated: {username}")
    return UserOut(**user)


@auth_router.post("/token")
async def generate_token(user: UserIn):
    user_in_db = authenticate_user(user.username, user.password)
    if user_in_db is None:
        logger.warning(f"Failed login attempt for user {user.username}")
        raise CustomNotFoundException("Invalid username or password")
    token = create_jwt_token({"sub": user_in_db.username})
    return {"access_token": token, "token_type": "bearer"}


@auth_router.get("/users/me", response_model=UserOut)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["sub"]}


@auth_router.get("/secure_data")
async def get_secure_data(current_user: dict = Depends(get_current_user)):
    return {"data": "This is secure data available only for authenticated users."}


@auth_router.post("/users/add", response_model=UserOut)
async def create_user(user: UserCreate):
    return add_user(user)


@auth_router.delete("/users/remove/{username}", response_model=UserOut)
async def delete_user(username: str, current_user: dict = Depends(get_current_user)):
    # Add any necessary authorization checks here
    return remove_user(username)


@auth_router.put("/users/update/{username}", response_model=UserOut)
async def update_user_info(username: str, updated_user: UserUpdate, current_user: dict = Depends(get_current_user)):
    # Add any necessary authorization checks here
    return update_user(username, updated_user)


@auth_router.get("/validate_email")
async def validate_email(username: str):
    user = db_users.find_one(username)
    if not user:
        logger.warning(f"Failed validation attempt for user {username} (user not found)")
        raise CustomNotFoundException("User not found")
    if user["status"] == "validated":
        logger.warning(f"Failed validation attempt for user {username} (already validated)")
        raise CustomNotFoundException("User already validated")
    user["status"] = "validated"
    db_users.update(username, user)
    logger.info(f"User {username} validated")
    return {"message": "Email validated"}
