from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    if_offer: Optional[bool] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q" : q}


    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id" : item_id}