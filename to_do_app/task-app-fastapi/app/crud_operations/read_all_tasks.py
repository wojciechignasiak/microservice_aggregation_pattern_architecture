from app.exceptions.database_error import DatabaseError
from app.schemas.task_schema import Task
from fastapi.encoders import jsonable_encoder

async def read_all_tasks():
    try:
        tasks = Task.find()
        tasks_list = []
        async for result in tasks:
            tasks_list.append(jsonable_encoder(result))
        return tasks_list
    except Exception as e:
        raise DatabaseError(f"read_all_tasks: {str(e)}")