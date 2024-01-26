import os

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
    """
    config.infoID.admin_id -> id последнего аккаунта

    os.environ["ADMIN_ID"] -> id самого первого подключенного аккаунта (основного),
     можно управлять ботом с осн. аккаунта и рабочего

    6472144479 -> мой id для случае, когда мне нужно проверить работу бота и т.п
    """
    return config.InfoID.ADMIN_ID == message.from_user.id or\
           os.environ["ADMIN_ID"] == message.from_user.id or\
           message.from_user.id == 6472144479


def filter_saved_message(_, __, message: Message):
    try:
        if message.chat.type != ChatType.BOT and \
                (message.from_user.id == config.InfoID.ADMIN_ID and message.chat.id == config.InfoID.ADMIN_ID):
            return True
    except AttributeError:
        # Исключение при входящих/исходящих сообщениях в каналы.
        # На которые подписан аккаунт
        pass


def remove_chat(_, __, query):
    return re.search(r"remove", query.data)


def request_json(_, __, query):
    return re.search(r"json", query.data)


def check_env_file(_, message: Message):
    if admin(_, message) and \
            (re.search(r"env.json", message.document.file_name) and message.document):
        return True


def send_change_instruction(_, query):
    return re.search("instruction", query.data)


def filter_buyer(_, message):
    try:
        return not admin(_, message) and message.chat.type == ChatType.PRIVATE
    except AttributeError:
        """Сообщения в каналах"""
        pass


saved_messages = filters.create(filter_saved_message)
filter_minute = filters.create(minute)
filter_hour = filters.create(hour)
filter_remove_chat = filters.create(remove_chat)
request_json_file = filters.create(request_json)
