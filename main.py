from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import *
from model import ToDo
from UpdateModel import UpdateToDo

app = FastAPI()

origins = ["https://rohankaran.github.io"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hi!"}


@app.get("/api/get-todo")
async def get_todo():
    response = await fetch_all_todos()
    if not response: raise HTTPException(404)
    return response


@app.get("/api/get-todo/{nanoid}", response_model=ToDo)
async def get_todo_id(nanoid):
    todo = await fetch_one_todo(nanoid)
    if todo:
        return todo
    raise HTTPException(400, "Bad request" )


@app.post("/api/add-todo", response_model=ToDo)
async def post_todo(todo: ToDo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.put("/api/update-todo/{nanoid}", response_model=ToDo)
async def put_todo(nanoid: str, updatetodo: UpdateToDo):
    response = await update_todo(nanoid, updatetodo.dict())
    if response:
        return response
    raise HTTPException(404, 'wrong')


@app.delete("/api/delete-todo/{nanoid}")
async def delete_todo(nanoid):
    response = await remove_todo(nanoid)
    if response:
        return response
    raise HTTPException(404)
