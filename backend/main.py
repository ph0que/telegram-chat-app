from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List
import uvicorn

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Message(BaseModel):
    id: int
    text: str
    fromMe: bool
    timestamp: str

class MessageCreate(BaseModel):
    text: str
    fromMe: bool = True

# In-memory storage
messages: List[Message] = [
    Message(id=1, text="Hello! How are you?", fromMe=False, timestamp="2024-12-15T01:00:00"),
    Message(id=2, text="I'm doing great, thanks!", fromMe=True, timestamp="2024-12-15T01:01:00"),
    Message(id=3, text="What have you been up to?", fromMe=False, timestamp="2024-12-15T01:02:00"),
]
message_id_counter = 4

@app.get("/")
def read_root():
    return {"message": "Telegram Chat API is running"}

@app.get("/messages", response_model=List[Message])
def get_messages():
    """Get all messages"""
    return messages

@app.post("/messages", response_model=Message)
def create_message(message_data: MessageCreate):
    """Create a new message"""
    global message_id_counter
    
    new_message = Message(
        id=message_id_counter,
        text=message_data.text,
        fromMe=message_data.fromMe,
        timestamp=datetime.now().isoformat()
    )
    
    messages.append(new_message)
    message_id_counter += 1
    
    return new_message

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
