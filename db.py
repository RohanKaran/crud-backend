import os
from model import *
import motor.motor_asyncio
from dotenv import dotenv_values

config = dotenv_values(".env")
DATABASE_URI = config.get("DATABASE_URI")
if os.getenv("DATABASE_URI"):
    DATABASE_URI = os.getenv("DATABASE_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
database = client.todoList
collection = database.todo


async def fetch_one_todo(nanoid):
    document = await collection.find_one({"nanoid": nanoid})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(ToDo(**document))
    return todos


async def create_todo(todo):
    document = todo
    await collection.insert_one(document)
    return document


async def update_todo(nanoid, title, desc):
    await collection.update_one({"nanoid": nanoid}, {"$set": {"title": title, "description": desc}})
    document = await collection.find_one({"nanoid": nanoid})
    return document


async def remove_todo(nanoid):
    await collection.delete_one({"nanoid": nanoid})
    return True
