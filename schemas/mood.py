from datetime import datetime

from pydantic import BaseModel, Field
from sqlmodel import SQLModel


class Mood(SQLModel):
    id: str | None = None
    mood: str
    date: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}

class MoodCreate(SQLModel):
    mood: str
    date: str

class MoodListResponse:
    total: int
    items: list[Mood]