from fastapi import APIRouter

from api.diaries import router as diaries_router

api_router = APIRouter()
api_router.include_router(diaries_router, prefix="/diaries", tags=["diaries"])
# api_router.include_router(moods.router, prefix="/moods", tags=["moods"])