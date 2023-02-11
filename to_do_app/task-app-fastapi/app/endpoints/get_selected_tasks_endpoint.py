import logging
from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud_operations.get_selected_tasks import get_selected_tasks


router = APIRouter()


@router.get("/selected")
async def get_selected_tasks_endpoint(tasks_ids: list | None = Query(default=None)):
    try:
        tasks = await get_selected_tasks(tasks_ids)
        return JSONResponse(status_code=200, content=jsonable_encoder(tasks))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})