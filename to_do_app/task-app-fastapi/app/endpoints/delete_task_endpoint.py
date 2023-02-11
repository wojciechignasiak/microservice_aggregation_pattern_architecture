import logging
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from app.crud_operations.delete_task import delete_task


router = APIRouter()


@router.delete("/delete")
async def delete_task_endpoint(task_id: str):
    try:
        await delete_task(task_id)
        return JSONResponse(status_code=200, content={"message": "Task removed"})
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})