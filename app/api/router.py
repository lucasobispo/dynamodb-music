from fastapi.routing import APIRouter

from app.api import echo,dynamoDB

api_router = APIRouter()

api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dynamoDB.router, prefix="/buscarDado", tags=["dynamoDB"])
