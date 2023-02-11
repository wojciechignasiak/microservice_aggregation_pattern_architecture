from app.exceptions.database_error import DatabaseError
from app.schemas.task_schema import Task
from beanie.operators import In
from bson import ObjectId

async def get_selected_tasks(tasks_ids: list):
    try:
        list_of_objects_ids = [ObjectId(x) for x in tasks_ids]
        users = await Task.find(In(Task.id, list_of_objects_ids)).to_list()
        return users
    except Exception as e:
        raise DatabaseError(f"get_selected_tasks: {str(e)}")