from fastapi import FastAPI
from app.views.v1 import api
from app.config.settings import settings


app = FastAPI()


app.include_router(api.endpoint_router, prefix=settings.API_V1)
