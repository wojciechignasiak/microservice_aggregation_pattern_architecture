from app.postgres_db.session_maker import session_maker
from app.exceptions.database_error import DatabaseError
from app.models.database_model import User, Task


async def assign_task_to_user(user_id: str, task_id: str):
    try:
        session = session_maker()
        user = session.query(User).filter(User.id==user_id).first()
        task = session.query(Task).filter(Task.id==task_id).first()
        user.task_id.append(task)
        session.add(user)
        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        raise DatabaseError(f"assign_task_to_user: {str(e)}")