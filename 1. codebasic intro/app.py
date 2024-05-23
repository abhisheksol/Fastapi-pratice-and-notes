from fastapi import FastAPI

app=FastAPI()

fooditem={
    "indian":["samosa","panipur","kachori"],
    "american":["burger","chips","pizza"],
    "japan":["suishe","fish","doracake"],
}

@app.get('/')
async def hello():
    return "welcome to Fast api"

@app.get('/{country}')
async def food(country:str):
    return fooditem.get(country)

@app.get('/item/{id}/{name}')
async def item(id:int,name:str):
    return f"this is ur item id:{id} :{name}"