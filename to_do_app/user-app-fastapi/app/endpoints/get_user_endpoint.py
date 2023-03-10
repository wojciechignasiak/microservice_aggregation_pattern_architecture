import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.crud_operations.get_user import get_user
router = APIRouter()


@router.get("/single")
async def get_user_endpoint(user_id: str):
    try:
        user = await get_user(user_id)
        return JSONResponse(status_code=200, content=jsonable_encoder(user))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})