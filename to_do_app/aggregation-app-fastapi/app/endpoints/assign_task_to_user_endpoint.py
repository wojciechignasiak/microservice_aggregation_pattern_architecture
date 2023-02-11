import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.crud_operations.assign_task_to_user import assign_task_to_user


router = APIRouter()


@router.put("/assign_task_to_user")
async def assign_task_to_user_endpoint(user_id: str, task_id: str):
    try:
        await assign_task_to_user(user_id, task_id)
        return JSONResponse(status_code=200, content={"message": "Task assigned to user"})
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})