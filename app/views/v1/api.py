from fastapi import APIRouter
from app.views.v1.endpoints import users


endpoint_router = APIRouter()


endpoint_router.include_router(users.router, prefix='/users', tags=['users'])