from app.models.database_model import Task
from app.postgres_db.session_maker import session_maker

def create_task(task_id: str):
    try:
        session = session_maker()
        new_task = Task(id=task_id)
        session.add(new_task)
        session.commit()
        session.close()
        return True
    except:
        session.rollback()
        return False