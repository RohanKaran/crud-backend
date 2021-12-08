from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import *
from model import ToDo


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return "Hi!"


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/get-todo/{title}", response_model=ToDo)
async def get_todo_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo item with this title: {title}")


@app.post("/api/add-todo", response_model=ToDo)
async def post_todo(todo: ToDo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.put("/api/update-todo/{title}", response_model=ToDo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo item with this title: {title}")


@app.delete("/api/delete-todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo item with this title: {title}")
