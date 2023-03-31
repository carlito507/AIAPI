from datetime import datetime
from typing import List, Dict, Optional
from uuid import uuid4
from app.core.database import db_conversations
from app.models.exceptions import CustomNotFoundException


class Message:
    def __init__(self, content: str) -> None:
        self.content = content


class Conversation:
    def __init__(self, conversation: Optional[List[Dict[str, str]]] = None, name: Optional[str] = None) -> None:
        if conversation is None:
            conversation = [{"role": "system", "content": "Welcome!"}]
        if name is None:
            name = str(uuid4())
        self.name = name
        self.created = datetime.timestamp(datetime.now())
        self.conversation = conversation

    def get_data(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "date_created": datetime.fromtimestamp(self.created).strftime("%A %d %B %Y, %H:%M:%S:%f"),
            "conversation": str(self.conversation)
        }

    def add_message(self, message: Message) -> str:
        self.conversation.append({"role": "user", "content": message.content})
        res = {"role": "assistant", "content": "I'm here to help."}
        self.conversation.append(res)

        return res["content"]

    def save_conversation(self) -> str:
        exists = db_conversations.find_one({"name": self.name})

        if exists is None:
            db_conversations.insert_one({
                "name": self.name,
                "timestamp": self.created,
                "conversation": str(self.conversation)
            })
            return f"{self.name} added to database."
        else:
            new_values = {"$set": {"conversation": str(self.conversation)}}
            db_conversations.update_one({"name": self.name}, new_values)

        return f"{self.name} has been updated."

    def load_conversation(self, name: Optional[str] = None) -> str:
        if name is None:
            arr = []
            conversations = db_conversations.find()
            for conversation in conversations:
                arr.append(conversation["name"])
            return f"conversations:\n{str(arr)}"

        exists = db_conversations.find_one({"name": name})
        if exists is None:
            raise CustomNotFoundException(f"Conversation {name} does not exist.")

        self.name = exists["name"]
        self.created = exists["timestamp"]
        self.conversation = exists["conversation"]

        return f"{name} loaded."

    @staticmethod
    def delete_conversation(name: str) -> str:
        exists = db_conversations.find_one({"name": name})

        if exists is None:
            raise CustomNotFoundException(f"Conversation {name} does not exist.")

        db_conversations.delete_one({"name": name})
        return f"{name} deleted."

