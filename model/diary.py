from datetime import datetime

from sqlmodel import SQLModel, Field


class Diary(SQLModel, table=True):
    __tablename__ = "diaries"

    id: str | None = Field(default=None, primary_key=True)
    title: str = Field(default=None, nullable=False)
    content: str = Field(default=None, nullable=False)
    created_at: datetime = Field(default=None, nullable=False)
    updated_at: datetime = Field(default=None, nullable=False)