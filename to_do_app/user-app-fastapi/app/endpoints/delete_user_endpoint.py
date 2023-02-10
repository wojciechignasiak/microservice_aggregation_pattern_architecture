import logging
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from app.crud_operations.delete_user import delete_user


router = APIRouter()


@router.delete("/delete")
async def delete_user_endpoint(user_id: str):
    try:
        await delete_user(user_id)
        return JSONResponse(status_code=200, content={"message": "User Removed"})
    except Exception as e:
        logging.warning(str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})