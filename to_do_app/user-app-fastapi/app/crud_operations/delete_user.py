from app.exceptions.database_error import DatabaseError
from app.schemas.user_schema import User
from app.rabbitmq_publisher.rabbitmq_publisher import rabbitmq_publisher
from bson import ObjectId

async def delete_user(user_id: str):
    try:
        await User.find_one(User.id == ObjectId(user_id)).delete()
        await rabbitmq_publisher("delete_user", str(user_id))
    except Exception as e:
        raise DatabaseError(f"delete_user: {str(e)}")