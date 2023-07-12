import datetime

from sqlalchemy.orm import sessionmaker


from db.models import Message, Chat


def add_post(session_maker: sessionmaker, message_id):
    with session_maker.begin() as session:
        msg = Message(message_id=message_id)
        session.add(msg)
        session.commit()


def edit_time_post(session_maker: sessionmaker, message_id):
    with session_maker.begin() as session:
        post = session.get(Message, message_id)
        post.time_update = datetime.datetime.now()
        session.commit()


def delete_post(session_maker: sessionmaker, post):
    with session_maker.begin() as session:
        session.delete(post)
        session.commit()


def write_new_chat(session_maker: sessionmaker, link_chat: str):
    with session_maker.begin() as session:
        new_chat = Chat()
        new_chat.link = link_chat
        session.add(new_chat)
        session.commit()


def delete_chat(session_maker: sessionmaker,
                chat_id):
    with session_maker.begin() as session:
        chat = session.get(Chat, chat_id)
        session.delete(chat)
        session.commit()