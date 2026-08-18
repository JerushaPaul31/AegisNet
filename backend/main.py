from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "AegisNet backend is running"}

# We need AegisNet to receive the threat reports -> 