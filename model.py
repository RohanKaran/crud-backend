from pydantic import BaseModel, validator
from fastapi import HTTPException


class ToDo(BaseModel):
    nanoid: str
    title: str
    description: str
    addedDT: str
    updatedDT: str

    @validator('title')
    def empty_title(cls, title):
        if len(title) <= 0:
            raise HTTPException(400, "Something went wrong")
        return title
