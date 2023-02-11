from app.postgres_db.session_maker import session_maker
from app.exceptions.database_error import DatabaseError
from app.models.database_model import User


async def get_tasks_assigned_to_user(user_id: str):
    try:
        session = session_maker()
        user = session.query(User).filter(User.id==user_id).first()
        if user:            
            return user.task_id
    except Exception as e:
        raise DatabaseError(f"get_tasks_assigned_to_user: {str(e)}")