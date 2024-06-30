from fastapi import FastAPI
app=FastAPI()


fooditem={
    "indian":["samosa","panipur","kachori"],
    "american":["burger","chips","pizza"],
    "japan":["suishe","fish","doracake"],
}

@app.get('/')
async def hello():
    return "welcome back abhishek after 1 months to fastapi"

@app.get('/{country}')
async def select_coun(country:str):
    return fooditem.get(country)