from typing import Any

from fastapi import Depends
from sqlalchemy import Sequence
from sqlmodel import select, func

from database.database import SessionDep
from model.mood import Mood
from schemas.mood import Mood as MoodSchema
from schemas.params import DefaultListParams


def create_mood(session: SessionDep, request: MoodSchema):
    mood = Mood.model_validate(request)
    session.add(mood)
    session.commit()
    session.refresh(mood)
    return mood

def get_mood(session: SessionDep, mood_id: str):
    result = session.get(Mood, mood_id)
    return result

def list_moods(
    session: SessionDep,
    params: DefaultListParams = Depends()
) -> Sequence[Any]:
    statement = select(Mood)

    if params.order_by != "":
        column = params.order_by.lower()
        if params.order == "desc":
            statement = statement.order_by(getattr(Mood, column).desc())
        else:
            statement = statement.order_by(getattr(Mood, column).asc())

    result = session.exec(statement).all()

    count_statement = select(func.count()).select_from(statement.subquery())
    total_items = session.exec(count_statement).one()

    return result, total_items
