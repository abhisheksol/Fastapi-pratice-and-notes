from fastapi import FastAPI

app=FastAPI()

@app.get("/{name}")
def home(name:str):
    return f"Ur name is {name}"