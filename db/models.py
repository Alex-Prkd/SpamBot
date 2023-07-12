import datetime

from sqlalchemy import Column, DateTime, BigInteger, String, Integer
from sqlalchemy.orm import declarative_base

BASE = declarative_base()



class Message(BASE):
    __tablename__ = "messages"

    message_id = Column(BigInteger, primary_key=True, unique=True)
    time_update = Column(DateTime, default=datetime.datetime.now)
    time_register = Column(DateTime, default=datetime.datetime.now)


class Chat(BASE):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
