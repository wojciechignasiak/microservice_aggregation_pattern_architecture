import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.user_model import UserModel
from app.crud_operations.create_user import create_user


router = APIRouter()


@router.post("/add")
async def create_user_endpoint(new_user: UserModel):
    try:
        new_user = await create_user(new_user)
        return JSONResponse(status_code=200, content=jsonable_encoder(new_user))
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})
