import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud_operations.get_tasks_assigned_to_user import get_tasks_assigned_to_user
from app.other_apps_urls.task_app_fastapi.get_selected_tasks_url import get_selected_tasks_url


router = APIRouter()


@router.get("/get_tasks_assigned_to_user")
async def get_tasks_assigned_to_user_endpoint(user_id: str):
    try:
        tasks_ids = await get_tasks_assigned_to_user(user_id)
        tasks_ids = jsonable_encoder(tasks_ids)
        tasks = await get_selected_tasks_url(tasks_ids)
        return JSONResponse(status_code=200, content=jsonable_encoder(tasks))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})