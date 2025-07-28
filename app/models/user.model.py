
from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class User(Document):  
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"  
