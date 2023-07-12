from pyrogram.types import Message

from db import session_maker
from db.commands.write import add_post


def my_function(_, message: Message):
    """Здесь запись id в бд из saved message
    для дальнейшей пересылки сообщений в канал"""
    add_post(session_maker=session_maker, message_id=message.id)
