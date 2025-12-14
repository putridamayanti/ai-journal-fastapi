from pydantic import BaseModel
from datetime import datetime

from sqlmodel import SQLModel


class Diary(BaseModel):
    id: str | None = None
    title: str | None = None
    content: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}


class DiaryCreate(SQLModel):
    title: str | None = None
    content: str