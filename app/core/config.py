import openai
import os

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

api_key = os.getenv("FERNET_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

SECRET_KEY = os.getenv("FERNET_KEY")
ALGORITHM = "HS256"

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:5000")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 5000)

CORS_ORIGINS: list[str] = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

ACCESS_TOKEN_EXPIRE_MINUTES = 30

SMTP_CONFIG = {
    "sender_email": "carltardifdesign@gmail.com",
    "host": "smtp.gmail.com",
    "port": 587,
    "username": "carltardifdesign@gmail.com",
    "password": os.getenv("SMTP_PASSWORD")
}

ALLOWED_EXTENSIONS = {'py', 'js', 'jsx', 'bat', 'ts', 'tsx', 'csv', 'css', 'html'}
