from datetime import datetime

from pydantic import BaseModel, Field

class Mood(BaseModel):
    id: str | None = None
    mood: str
    date: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}