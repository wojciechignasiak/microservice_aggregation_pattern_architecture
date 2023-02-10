from app.models.user_model import UserModel
from app.schemas.user_schema import User
from app.exceptions.database_error import DatabaseError
from app.rabbitmq_publisher.rabbitmq_publisher import rabbitmq_publisher


async def create_user(new_user: UserModel):
    try:
        new_user = User(email = new_user.email, nickname = new_user.nickname)
        await new_user.insert()
        await rabbitmq_publisher("create_user", str(new_user.id))
        return new_user
    except Exception as e:
        raise DatabaseError(f"create_user: {str(e)}")
        