from fastapi import FastAPI, HTTPException
from app.password_generator import password_engine
from app.counter import get_count_manager, increment_count_manager
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.captcha import verify_captcha


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://finite-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordRequest(BaseModel):
    length: int
    captcha_token: str

@app.get("/")
async def start_page():
    return { "passwords_generated" : get_count_manager()}

@app.post("/generate")
@increment_count_manager()
async def generate(data: PasswordRequest):
    try:
        password = password_engine(data.length)
        captcha_valid = await verify_captcha(data.captcha_token)

        if not captcha_valid:
            return {"status": "robot"}

        return {"status": "human", "password": password}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
