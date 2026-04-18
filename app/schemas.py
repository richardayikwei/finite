from pydantic import BaseModel


class PasswordRequest(BaseModel):
    length: int
    captcha_token: str