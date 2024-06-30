from fastapi import FastAPI
from schemas import Blog  # Ensure this matches the actual location and name of schemas.py
import models
from database import  engine

models.Base.metadata.create_all(engine)
app = FastAPI()

@app.get('/')
async def hello():
    return {"message": "Abhishek is a good boy"}

@app.post('/blog')
async def create_blog(req: Blog):
    return req
