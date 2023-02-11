from app.exceptions.database_error import DatabaseError
from app.schemas.task_schema import Task
from bson import ObjectId

async def read_task(task_id: str):
    try:
        task = await Task.find_one(Task.id == ObjectId(task_id))
        return task
    except Exception as e:
        raise DatabaseError(f"get_task: {str(e)}")