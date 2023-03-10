import logging
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.crud_operations.get_all_users import get_all_users


router = APIRouter()


@router.get("/all")
async def get_all_users_endpoint():
    try:
        users = await get_all_users()
        return JSONResponse(status_code=200, content=jsonable_encoder(users))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})


