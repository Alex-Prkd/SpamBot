from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import BASE


def added_engine(url: str):
    engine = create_engine(url=url, echo=True)
    BASE.metadata.create_all(engine)
    return engine


def create_session(engine):
    session = sessionmaker(bind=engine, expire_on_commit=False)
    return session



