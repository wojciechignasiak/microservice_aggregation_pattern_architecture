from beanie import Document, Indexed


class User(Document):
    email: Indexed(str, unique=True)
    nickname: str
    

    class Settings:
        name = "user"

    class Config:
        schema_extra = {
            "example": {
                "email": "jan_kowalski@poczta.com",
                "nickname": "jkowalski"
            }
        }