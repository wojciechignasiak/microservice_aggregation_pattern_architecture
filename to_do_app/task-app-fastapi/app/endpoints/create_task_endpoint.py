import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.task_model import TaskModel
from app.crud_operations.create_task import create_task


router = APIRouter()


@router.post("/add")
async def create_task_endpoint(new_task: TaskModel):
    try:
        task = await create_task(new_task)
        return JSONResponse(status_code=200, content=jsonable_encoder(task))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})
