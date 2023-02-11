import os
from beanie import init_beanie
import motor.motor_asyncio
from app.schemas.task_schema import Task

mongo_username = os.environ.get("MONGO_USERNAME")
mongo_password = os.environ.get("MONGO_PASSWORD")

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{mongo_username}:{mongo_password}@mongo:27017/"
    )
    await init_beanie(database=client["to_do_app"], document_models=[Task])