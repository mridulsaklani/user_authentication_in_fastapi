# app/db.py

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os


load_dotenv()  

MONGO_URI = os.getenv("MONGO_URI")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    
    db = client.get_default_database()

    try:
       await init_beanie(database=db, document_models=[])
       print("Mongo db connected bc")
    except:
        raise Exception:
    
    
