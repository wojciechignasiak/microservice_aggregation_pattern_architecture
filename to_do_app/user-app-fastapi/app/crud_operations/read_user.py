from app.exceptions.database_error import DatabaseError
from app.schemas.user_schema import User
from bson import ObjectId

async def read_user(user_id: str):
    try:
        user = await User.find_one(User.id == ObjectId(user_id))
        return user
    except Exception as e:
        raise DatabaseError(f"read_user: {str(e)}")