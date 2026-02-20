from fastapi import FastAPI, HTTPException
from app.password_generator import password_engine

app = FastAPI()

@app.get("/")
async def start_page():
    return { "passwords_generated" : 12345}

@app.get("/generate/")
async def generate(k:int):
    try:
        result = password_engine(k)
        return {"result" : result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
