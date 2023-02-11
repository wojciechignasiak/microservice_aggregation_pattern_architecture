from app.models.task_model import TaskModel
from app.schemas.task_schema import Task
from app.exceptions.database_error import DatabaseError
from app.rabbitmq_publisher.rabbitmq_publisher import rabbitmq_publisher

async def create_task(new_task: TaskModel):
    try:
        new_task = Task(
            name = new_task.name,
            description = new_task.description,
            )
        await new_task.insert()
        if new_task:
            await rabbitmq_publisher("create_task", str(new_task.id))
        return new_task
    except Exception as e:
        raise DatabaseError(f"create_task: {str(e)}")
        