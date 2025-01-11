from fastapi import FastAPI
from config.config_bd import engine, Base
from contextlib import asynccontextmanager


# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)


def fake_answer_to_everything_ml_model(x: float):
   return x * 42




ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
   ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
   yield
   ml_models.clear()




app = FastAPI(lifespan=lifespan)


# app.include_router(author_router.router)
# app.include_router()
# app.include_router()
