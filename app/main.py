from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Order matters

@app.get("/users/me")
async def get_current_user():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

# Predefined values
class LanguageGroup(str, Enum):
    nilotes = "kalenjin"
    bantu = "kikuyu"
    cushites = "borana"

@app.get("/languages/{name}")
async def get_lang(name: LanguageGroup):
    return name.name

class Weekday(str, Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

@app.get("/days/{name}")
async def get_lang(name: Weekday):
    return name.name

