from fastapi import FastAPI
from app.rabbitmq_consumer.rabbitmq_consumer import rabbitmq_consumer
import asyncio



def create_application() -> FastAPI:
    application = FastAPI()
    return application


app = create_application()

@app.on_event("startup")
async def start_db():
    loop = asyncio.get_running_loop()
    await asyncio.ensure_future(await rabbitmq_consumer(loop))



