from app.exceptions.database_error import DatabaseError
from app.schemas.user_schema import User
from fastapi.encoders import jsonable_encoder

async def read_all_users():
    try:
        users = User.find()
        users_list = []
        async for result in users:
            users_list.append(jsonable_encoder(result))
        return users_list
    except Exception as e:
        raise DatabaseError(f"read_all_users: {str(e)}")