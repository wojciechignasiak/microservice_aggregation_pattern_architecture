from fastapi import FastAPI
from app.postgres_db.db_connect_and_init import db_connect_and_init
from app.endpoints import (
    assign_task_to_user_endpoint,
    get_tasks_assigned_to_user_endpoint
    )


def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/aggregation/openapi.json", docs_url="/aggregation/docs")
    application.include_router(assign_task_to_user_endpoint.router, prefix="/aggregation", tags=["aggregation"])
    application.include_router(get_tasks_assigned_to_user_endpoint.router, prefix="/aggregation", tags=["aggregation"])
    return application


app = create_application()

@app.on_event("startup")
async def start_db():
    db_connect_and_init()