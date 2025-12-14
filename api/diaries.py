from fastapi import APIRouter
from database.database import SessionDep
from libs.ai_model import generate_title
from schemas.diary import Diary, DiaryCreate

import services.diary

router = APIRouter()

@router.get("/")
def list_diaries(session: SessionDep):
    result = services.diary.list_diaries(session)
    return {
        "message": "Hello World",
        "data": result
    }

@router.post("/", response_model=Diary)
def create_diary(session: SessionDep, diary: DiaryCreate):
    title = generate_title(diary.content)
    diary.title = title

    diary = services.diary.create_diary(session, diary)

    return diary