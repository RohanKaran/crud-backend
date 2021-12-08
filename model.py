from pydantic import BaseModel, validator
from fastapi import HTTPException


class ToDo(BaseModel):
    title: str
    description: str

    @validator('title')
    def empty_title(cls, title):
        t = title.strip()
        if len(t) <= 0:
            raise HTTPException(400, "Something went wrong")
        return t
