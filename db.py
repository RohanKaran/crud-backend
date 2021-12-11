import os
from model import *
import motor.motor_asyncio
from dotenv import dotenv_values

DATABASE_URI = "mongodb+srv://crud-app:12345crud@crud-app.ydmdq.mongodb.net/todoList?retryWrites=true&w=majority"
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


async def update_todo(nanoid, data):
    await collection.update_one({"nanoid": nanoid}, {"$set": data})
    document = await collection.find_one({"nanoid": nanoid})
    return document


async def remove_todo(nanoid):
    await collection.delete_one({"nanoid": nanoid})
    return True
