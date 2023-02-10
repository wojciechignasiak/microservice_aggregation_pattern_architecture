from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserModel(BaseModel):
    id: Optional[str]
    email: EmailStr = Field(...)
    nickname: str = Field(...)
    


    class Config:
        schema_extra = {
            "example": {
                "id": "",
                "email": "jan_kowalski@poczta.com",
                "nickname": "jkowalski"
            }
        }
