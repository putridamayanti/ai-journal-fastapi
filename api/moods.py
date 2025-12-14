import uuid
from datetime import datetime

from fastapi import APIRouter

import services.mood
from database.database import SessionDep
from schemas.mood import Mood

router = APIRouter()

@router.post("/", tags=["moods"])
def create_mood(session: SessionDep, mood: Mood):
    mood.id = str(uuid.uuid4())
    mood.created_at = datetime.now()
    mood.updated_at = datetime.now()

    result = services.mood.create_mood(session, mood)

    return {
        "message": "Mood created successfully",
        "data": result
    }

@router.get("/", tags=["moods"])
def list_moods(session: SessionDep):
    moods = services.mood.list_moods(session)
    return {
        "message": "Moods retrieved successfully",
        "data": moods
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