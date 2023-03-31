from pymongo import MongoClient
from config import MONGODB_URI


client = MongoClient(MONGODB_URI)
db = client["database"]
db_conversations = db["conversations"]
db_users = db["users"]

