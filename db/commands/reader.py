from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from db.models import Message, Chat


def get_post(session_maker: sessionmaker):
    with session_maker.begin() as session:
        post = session.scalar(select(Message).order_by(Message.time_update))
        return post


def all_chats(session_maker: sessionmaker):
    with session_maker.begin() as session:
        chats = session.scalars(select(Chat))
        return chats.all()