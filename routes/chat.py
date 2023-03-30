import os
import uuid

from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List
from openai import ChatCompletion
import pickle
from models.tokenizer import Tokenizer
from models.openai_engines import TEXT_MODELS, CODE_MODELS, DOCUMENTS_MODELS, CHAT_MODELS

# Create a router
chat_router = APIRouter()

# Create a tokenizer
encoder = Tokenizer("cl100k_base")


# Create a model
class ChatPrompt(BaseModel):
    message: str


class Conversation(BaseModel):
    conversation: List[dict] = [
        {"role": "system", "content": "You are an expert in AI."},
        {"role": "assistant", "content": "Hello, how can I help you?"},
    ]


conversation = Conversation()


@chat_router.get("/conversation")
async def get_conversation():
    return conversation.conversation, 200


@chat_router.post("/conversation")
async def post_conversation(request: Request, prompt: ChatPrompt):
    print(prompt.message)
    conversation.conversation.append(
        {"role": "user", "content": prompt.message}
    )
    response = ChatCompletion.create(
        model="gpt-4",
        messages=conversation.conversation
    )
    print(response.choices[0].message.content)
    conversation.conversation.append(
        {"role": "assistant", "content": response.choices[0].message.content}
    )
    return conversation.conversation, 200


@chat_router.get("/new_conversation")
async def new_conversation():
    global conversation
    conversation = Conversation()
    return conversation.conversation, 200


@chat_router.post("/new_conversation")
async def new_conversation(request: Request):
    global conversation
    data = await request.json()
    print(data)
    conversation = Conversation(
        conversation=data
    )
    return conversation.conversation, 200


@chat_router.post("/save_conversation")
async def save_conversation(request: Request):
    global conversation
    try:
        data = await request.json()
        chat_id = data["id"]
    except Exception as e:
        print(e)
        chat_id = str(uuid.uuid4())
    ids = []
    with open(f"conversation_{chat_id}.pickle", "wb") as f:
        pickle.dump(conversation.conversation, f)
    if os.path.exists("ids.pickle"):
        with open("ids.pickle", "rb") as f:
            ids = pickle.load(f)
    else:
        ids = chat_id
        with open("ids.pickle", "wb") as f:
            pickle.dump(ids, f)
    print(ids)
    return "messages updated.", chat_id, conversation.conversation, 200


@chat_router.get("/load_conversations")
async def load_conversations():
    ids = []
    for file in os.listdir():
        if file.startswith("conversation_"):
            ids.append(file.split("_")[1].split(".")[0])
    print(ids)
    return ids, 200


@chat_router.get("/load_conversation_by_index/{index}")
async def get_conversation_index(index: int):
    files = []
    for file in os.listdir():
        if file.startswith("conversation_"):
            files.append(file)
    if index >= len(files):
        return "Index out of range.", 400
    file = files[index]
    with open(file, "rb") as f:
        conversation.conversation = pickle.load(f)
        return conversation.conversation[index], 200


@chat_router.get("/load_conversation_by_id/{chat_id}")
async def get_conversation_id(chat_id: str):
    with open(f"conversation_{chat_id}.pickle", "rb") as f:
        conversation.conversation = pickle.load(f)
        return conversation.conversation, 200


@chat_router.get("/chat_models")
async def get_chat_models():
    return CHAT_MODELS, 200


@chat_router.get("/text_models")
async def get_models():
    return TEXT_MODELS, 200


@chat_router.get("/code_models")
async def get_models():
    return CODE_MODELS, 200


@chat_router.get("/document_models")
async def get_models():
    return DOCUMENTS_MODELS, 200


@chat_router.get("/models")
async def get_models():
    return TEXT_MODELS, CODE_MODELS, DOCUMENTS_MODELS, CHAT_MODELS, 200


@chat_router.post("/tiktoken")
async def tiktoken(request: Request):
    data = await request.json()
    print(data)
    print(encoder.encode(data["text"]))
    d = {
        "text": data["text"],
        "tokens": encoder.encode(data["text"]),
        "num_tokens": len(encoder.encode(data["text"]))
    }
    chunks = []
    for i in range(0, len(d["tokens"])):
        chunks.append(encoder.decode_single_token(d["tokens"][i]))
    d["tokens"] = zip(chunks, encoder.encode(data["text"]))
    print(d)
    return d, 200
