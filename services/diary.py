import uuid
from datetime import datetime
from typing import Any, Sequence

from fastapi import Depends
from sqlmodel import select, func
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
        params: DefaultListParams = Depends(),
) -> Sequence[Any]:
    statement = select(Diary)

    if params.search:
        statement = statement.where(Diary.title.contains(params.search))

    if params.order_by != "":
        column = params.order_by.lower()
        if params.order == "desc":
            statement = statement.order_by(getattr(Diary, column).desc())
        else:
            statement = statement.order_by(getattr(Diary, column).asc())

    if params.order_by != "" and params.order == "desc":
        statement = statement.order_by(
            params.order == "asc" and Diary.created_at.asc() or Diary.created_at.desc()
        )
    else:
        statement = statement.order_by(Diary.created_at.desc())

    if params.limit > 0:
        statement = statement.limit(params.limit)

    if params.offset > 0:
        statement = statement.offset(params.offset)

    result = session.exec(statement).all()

    count_statement = select(func.count()).select_from(statement.subquery())
    total_items = session.exec(count_statement).one()

    return result, total_items