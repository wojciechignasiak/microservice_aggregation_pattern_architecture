from fastapi import FastAPI
from app.mongo_connector.connector import init_db

from app.endpoints import (
    create_task_endpoint,
    get_task_endpoint,
    get_all_tasks_endpoint,
    delete_task_endpoint,
    get_selected_tasks_endpoint
)


def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/task/openapi.json", docs_url="/task/docs")
    application.include_router(create_task_endpoint.router, prefix="/task", tags=["task"])
    application.include_router(get_task_endpoint.router, prefix="/task", tags=["task"])
    application.include_router(get_selected_tasks_endpoint.router, prefix="/task", tags=["task"])
    application.include_router(get_all_tasks_endpoint.router, prefix="/task", tags=["task"])
    application.include_router(delete_task_endpoint.router, prefix="/task", tags=["task"])

    return application


app = create_application()


@app.on_event("startup")
async def start_db():
    await init_db()
    print("Connected to MongoDB...")
    print("Task collection initialized...")
    