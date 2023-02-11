from app.exceptions.database_error import DatabaseError
from app.schemas.task_schema import Task
from bson import ObjectId
from app.rabbitmq_publisher.rabbitmq_publisher import rabbitmq_publisher

async def delete_task(task_id: str):
    try:
        await Task.find_one(Task.id == ObjectId(task_id)).delete()
        await rabbitmq_publisher("delete_task", str(task_id))
    except Exception as e:
        raise DatabaseError(f"delete_task: {str(e)}")