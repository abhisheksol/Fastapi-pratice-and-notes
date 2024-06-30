from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello abhishek"}

@app.post("/items/")
async def create_item(item: Item):
    return item
