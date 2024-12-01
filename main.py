from contextlib import asynccontextmanager

from fastapi import FastAPI
from database import delete_tables, create_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    print("Очистка базы")
    await create_tables()
    print("Создание базы")
    yield
    print("Выключение ")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
