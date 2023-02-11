import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud_operations.read_task import read_task
router = APIRouter()


@router.get("/single")
async def get_task_endpoint(id: str):
    try:
        task = await read_task(id)
        return JSONResponse(status_code=200, content=jsonable_encoder(task))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})