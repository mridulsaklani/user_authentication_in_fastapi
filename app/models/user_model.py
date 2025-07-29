from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class User(Document):  
    username: str = Field(..., min_length=3, max_length=30)
    email_hash: str = Field(..., )
    email: str =Field(...)
    password: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"  
