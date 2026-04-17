from fastapi import APIRouter
from fastapi import HTTPException
from app.password_generator import password_engine
from app.counter import get_count_manager, increment_count_manager
from app.schemas import PasswordRequest
from app.captcha import verify_captcha

router = APIRouter()


@router.get("/count")
async def start_page():
    return { "passwords_generated" : get_count_manager()}

@router.post("/generate")
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