from fastapi import Depends, FastAPI
from schemas import Blog  # Ensure this matches the actual location and name of schemas.py
from sqlalchemy.orm import Session
import models
from database import  SessionLocal,engine

models.Base.metadata.create_all(engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/')
async def hello():
    return {"message": "Abhishek is a good boy"}


@app.get('/all')
async def get_all_blog(db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
async def get_all_blog(id:int, db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    return blog

@app.post('/blog')
async def create_blog(req: Blog,db: Session = Depends(get_db)):
    new_blog=models.Blog(title=req.title,body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/delete/{id}')
async def delete(id:int,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return db.query(models.Blog).all()