import httpx
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

async def verify_captcha(token: str) -> bool:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": SECRET_KEY,
                "response": token
            }
        )
        result = response.json()
        return result.get("success", False)