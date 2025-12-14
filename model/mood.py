from sqlalchemy import Column, String, DateTime
from datetime import datetime

from database.database import Base


class Mood(Base):
    __tablename__ = "moods"

    id = Column(String, primary_key=True, index=True)
    mood = Column(String, nullable=False)
    date = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

