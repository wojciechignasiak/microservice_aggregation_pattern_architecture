from app.exceptions.database_error import DatabaseError
from app.schemas.user_schema import User
from beanie.operators import In
from bson import ObjectId

async def read_selected_users(users_ids: list):
    try:
        list_of_objects_ids = [ObjectId(x) for x in users_ids]
        users = await User.find(In(User.id, list_of_objects_ids)).to_list()
        return users
    except Exception as e:
        raise DatabaseError(f"read_selected_users: {str(e)}")