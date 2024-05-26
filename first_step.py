from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def hello():
    return "hello welcome"

@app.get("/fetch-data")
async def fetch_data():
    url = "https://abhi-beige.vercel.app/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()  # Assuming the response is in JSON format
    return data
