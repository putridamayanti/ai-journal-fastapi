from fastapi import APIRouter

from api.diaries import router as diaries_router
from api.moods import router as moods_router
from api.questions import router as questions_router

api_router = APIRouter()
api_router.include_router(diaries_router, prefix="/diaries", tags=["diaries"])
api_router.include_router(moods_router, prefix="/moods", tags=["moods"])
api_router.include_router(questions_router, prefix="/questions", tags=["questions"])