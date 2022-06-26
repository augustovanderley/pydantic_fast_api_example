from typing import Union

from fastapi import FastAPI
from item_model import Item


app = FastAPI()

database = []

@app.post("/api/item/create")
def read_root(data: Item):
    database.append(data.dict())
    raise Exception()
    return database


# http://127.0.0.1:8000/items/5?q=somequery
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}