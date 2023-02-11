from app.models.database_model import Task
from app.postgres_db.session_maker import session_maker


def delete_task(task_id: str):
    try:
        session = session_maker()
        deleted_task = session.query(Task).filter(Task.id==task_id).first()
        if deleted_task:
            session.delete(deleted_task)
            session.commit()
            return True
        return True
    except:
        session.rollback()
        return False