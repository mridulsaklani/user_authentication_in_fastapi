from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import logging

from app.models.user_model import User

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

async def init_db():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
        await init_beanie(database=db, document_models=[User])
        print("MongoDB connected successfully")
    except Exception as e:
        logging.error("MongoDB connection failed")
        logging.exception(e)
        raise

