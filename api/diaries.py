from fastapi import APIRouter

from database.database import SessionDep
from libs.ai_model import generate_title
from libs.pagination import build_list_pagination_response
from schemas.diary import Diary, DiaryCreate

import services.diary
from schemas.params import DefaultListParams

router = APIRouter()

@router.get("/")
def list_diaries(
        session: SessionDep,
        offset: int = 0,
        limit: int = 100,
        search: str | None = None,
        order_by: str | None = "desc",
        order: str | None = "created_at",
):
    params = DefaultListParams(
        offset=offset,
        limit=limit,
        search=search,
        order_by=order_by,
        order=order
    )

    diaries, total = services.diary.list_diaries(session, params)

    result = build_list_pagination_response(
        items=diaries,
        total_items=total,
        offset=params.offset,
        limit=params.limit
    )

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