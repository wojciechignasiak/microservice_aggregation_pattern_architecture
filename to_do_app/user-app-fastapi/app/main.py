from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.mongo_connector.connector import init_db
from app.endpoints import (
    create_user_endpoint,
    delete_user_endpoint,
    get_all_users_endpoint
)


def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/user/openapi.json", docs_url="/user/docs")

    application.include_router(create_user_endpoint.router, prefix="/user", tags=["user"])
    application.include_router(delete_user_endpoint.router, prefix="/user", tags=["user"])
    application.include_router(get_all_users_endpoint.router, prefix="/user", tags=["user"])
    
    return application


app = create_application()

@app.on_event("startup")
async def start_db():
    await init_db()
    print("Connected to MongoDB...")
    print("User collection initialized")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)