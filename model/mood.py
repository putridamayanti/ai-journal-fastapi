from sqlalchemy import Column, String, DateTime
from datetime import datetime

from sqlmodel import SQLModel, Field


class Mood(SQLModel, table=True):
    __tablename__ = "moods"

    id: str | None = Field(default=None, primary_key=True)
    mood: str = Field(default=None, nullable=False)
    date: datetime = Field(default=None, nullable=False)
    created_at: datetime = Field(default=None, nullable=False)
    updated_at: datetime = Field(default=None, nullable=False)