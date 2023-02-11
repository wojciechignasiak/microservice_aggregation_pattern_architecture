import logging
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud_operations.read_all_tasks import read_all_tasks


router = APIRouter()


@router.get("/all")
async def get_all_tasks_endpoint():
    try:
        tasks = await read_all_tasks()
        return JSONResponse(status_code=200, content=jsonable_encoder(tasks))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})


