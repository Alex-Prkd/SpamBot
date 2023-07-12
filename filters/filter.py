from pyrogram import filters

import re

from pyrogram.enums import ChatType
from pyrogram.types import Message

import config


def minute(_, __, query):
    return re.search(r"min", query.data)


def hour(_, __, query):
    return re.search(r"hour", query.data)


def admin(_, message: Message):
    return config.InfoID.ADMIN_ID == message.from_user.id


def filter_saved_message(_, __, message: Message):
    try:
        if message.chat.type != ChatType.BOT and\
                (message.from_user.id == config.InfoID.ADMIN_ID and message.chat.id == config.InfoID.ADMIN_ID):
            return True
    except AttributeError:
        # Исключение при входящих сообщениях в каналы.
        # На которые подписан аккаунт
        pass


def remove_chat(_, __, query):
    return re.search(r"remove", query.data)


saved_messages = filters.create(filter_saved_message)
filter_minute = filters.create(minute)
filter_hour = filters.create(hour)
filter_remove_chat = filters.create(remove_chat)
