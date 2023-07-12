from time import sleep

from pyrogram import Client
from pyrogram.errors import MessageIdInvalid, UsernameNotOccupied, ChatAdminRequired
from pyrogram.errors.exceptions import flood_420, forbidden_403

import config
from bot.error_message import error_link_chat, error_send_channel
from db.commands.reader import get_post, all_chats
from db.commands.write import edit_time_post, delete_post, delete_chat


def send_post(client: Client, session_maker):
    post = get_post(session_maker)
    chats = all_chats(session_maker=session_maker)

    if len(chats) != 0:
        for id, chat in enumerate(chats):
            try:
                sleep(2)
                client.forward_messages(chat_id=chat.link,
                                        from_chat_id=config.InfoID.ADMIN_ID,
                                        message_ids=post.message_id)
                if id == 0:
                    # При отправке в первый чат, обновляется время последней рассылки.
                    edit_time_post(session_maker, post.message_id)

            except UsernameNotOccupied:
                # Некорректная ссылка чата.
                # Приходит уведомление, чат удаляется из базы.

                error_link_chat(chat.link)
                delete_chat(session_maker=session_maker,
                            chat_id=chat.id)
            except MessageIdInvalid:
                # Сообщение удаленно из избранного.
                # Удаляется сообщение из бд.
                # Заново вызывается send_post,
                # чтобы переслать след-ий пост.

                delete_post(session_maker, post)
                send_post(client, session_maker)
            except AttributeError:
                # В базе нет сообщений.
                pass
            except ChatAdminRequired:
                # Попытка отправить сообщение в канал.
                delete_chat(session_maker=session_maker,
                            chat_id=chat.id)
                error_send_channel(link=chat.link)
            except flood_420.SlowmodeWait:
                # Бан в чате на n секунд, после окончания присылается пост
                pass
            except forbidden_403.ChatWriteForbidden:
                # Нет прав отправлять сообщения в чате, добавили в бан
                pass

