import uuid
from datetime import datetime

from fastapi import APIRouter

import services.mood
from database.database import SessionDep
from libs.pagination import build_list_pagination_response
from schemas.mood import Mood, MoodCreate
from schemas.params import DefaultListParams

router = APIRouter()

@router.post("/", tags=["moods"])
def create_mood(session: SessionDep, mood: Mood):
    mood.id = str(uuid.uuid4())
    mood.created_at = datetime.now()
    mood.updated_at = datetime.now()

    mood = services.mood.create_mood(session, mood)

    return {
        "message": "Mood created successfully",
        "data": mood
    }

@router.get("/", tags=["moods"])
def list_moods(
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
    print(params)
    moods, total_items = services.mood.list_moods(session, params)

    result = build_list_pagination_response(
        items=moods,
        total_items=total_items,
        offset=params.offset,
        limit=params.limit
    )

    return {
        "message": "Moods retrieved successfully",
        "data": result
    }

@router.get("/{mood_id}", tags=["moods"])
def get_mood(session: SessionDep, mood_id: str):
    mood = services.mood.get_mood(session, mood_id)
    if not mood:
        return {
            "message": "Mood not found",
            "data": None
        }
    return {
        "message": "Mood retrieved successfully",
        "data": mood
    }