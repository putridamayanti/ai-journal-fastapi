import uuid
from datetime import datetime
from typing import Any, Sequence

from fastapi import Depends
from sqlmodel import select
from database.database import SessionDep
from model.diary import Diary
from schemas.diary import Diary as DiarySchema, DiaryCreate
from schemas.params import DefaultListParams


def create_diary(session: SessionDep, request: DiaryCreate) -> DiarySchema:
    diary = Diary.model_validate(request)
    diary.id = str(uuid.uuid4())
    diary.created_at = datetime.now()
    diary.updated_at = datetime.now()

    session.add(diary)
    session.commit()
    session.refresh(diary)
    return diary

def list_diaries(
        session: SessionDep,
        params: DefaultListParams = Depends(DefaultListParams),
) -> Sequence[Any]:
    result = session.exec(select(Diary)).all()
    return result