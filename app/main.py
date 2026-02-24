from fastapi import FastAPI, HTTPException
from app.password_generator import password_engine
from app.counter import get_count_manager, increment_count_manager

app = FastAPI()

@app.get("/")
async def start_page():
    return { "passwords_generated" : get_count_manager()}

@app.get("/generate/")
@increment_count_manager()
async def generate(k:int | float):
    try:
        result = password_engine(k)
        return {"result" : result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
