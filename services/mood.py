from sqlalchemy import select

from database.database import SessionDep
from schemas.mood import Mood

def create_mood(session: SessionDep, mood: Mood):
    session.add(mood)
    session.commit()
    session.refresh(mood)
    return mood

def get_mood(session: SessionDep, mood_id: str):
    result = session.get(Mood, mood_id)
    return result

def list_moods(session: SessionDep):
    result = session.exec(select(Mood))
    return result.fetchall()
