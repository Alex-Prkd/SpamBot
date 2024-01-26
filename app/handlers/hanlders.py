from pyrogram import Client
from pyrogram.types import Message

from db import session_maker
from db.commands.write import add_post


def my_function(_, message: Message):
    """Здесь запись id в бд из saved message
    для дальнейшей пересылки сообщений в канал"""
    add_post(session_maker=session_maker, message_id=message.id)



def response_buyer(client: Client, message: Message):
    """Шаблонный ответ покупателям"""
    print(response_buyer.__name__)
    client.send_message(chat_id=message.chat.id, text="Здравствуйте, я бот, если хотите "
                                                      "сделать заказ отпишите менеджеру:  ")