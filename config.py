import openai
import os
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

api_key = os.getenv("FERNET_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

SECRET_KEY = os.getenv("FERNET_KEY")
ALGORITHM = "HS256"
