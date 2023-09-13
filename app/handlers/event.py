import logging
from time import sleep

from pyrogram import Client
from pyrogram.errors import MessageIdInvalid, UsernameNotOccupied, ChatAdminRequired, UserBannedInChannel, BadRequest, \
    PersistentTimestampInvalid
from pyrogram.errors.exceptions import flood_420, forbidden_403

import config
from bot.error_message import error_link_chat, error_send_channel
from db.commands.reader import get_post, all_chats
from db.commands.write import edit_time_post, delete_post, delete_chat

logging.basicConfig(level=logging.ERROR, filename="log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.error(f"Журнал ошибок:\n\n\n")


def send_post(client: Client, session_maker):
    post = get_post(session_maker)
    chats = all_chats(session_maker=session_maker)

    if len(chats) != 0:
        for chat in chats:
            sleep(3)
            try:
                client.forward_messages(chat_id=chat.link,
                                        from_chat_id=config.InfoID.ADMIN_ID,
                                        message_ids=post.message_id)
            except UsernameNotOccupied as err:
                # Некорректная ссылка чата.
                # Приходит уведомление, чат удаляется из базы.
                logging.error(f"{err}\nНекорректная ссылка: {chat.link}\n")
                error_link_chat(chat.link)
                delete_chat(session_maker=session_maker,
                            name_chat=chat.link)
            except MessageIdInvalid:
                # Сообщение удаленно из избранного.
                # Удаляется сообщение из бд.
                # Заново вызывается send_post,
                # чтобы переслать след-ий пост.

                delete_post(session_maker, post)
                send_post(client, session_maker)
            except AttributeError:
                # В базе нет сообщений.
                break
            except ChatAdminRequired as err:
                # Попытка отправить сообщение в канал.
                logging.error(f"{err}\nПопытка отправить сообщение в канал: {chat.link}\n")
                delete_chat(session_maker=session_maker,
                            name_chat=chat.link)
                error_send_channel(link=chat.link)
            except flood_420.SlowmodeWait:
                # Бан в чате на n секунд, после окончания присылается пост
                continue
            except forbidden_403.ChatWriteForbidden as err:
                # Вы не можете писать в этом чате, т.к. не состоите в нём
                logging.error(f"{err}\nВы не можете писать в этом чате. Проверьте состоите ли вы в нём. {chat.link}\n")
                error_link_chat(chat.link)
                delete_chat(session_maker=session_maker,
                            name_chat=chat.link)
            except KeyError as err:
                # Если добавили в чс/удалили из чата.
                logging.error(f"{err}\nОшибка ключа, отправка невозможна. Проверьте состоите ли вы в чате. {chat.link}\n")
                delete_chat(session_maker=session_maker,
                            name_chat=chat.link)
                error_send_channel(link=chat.link)
            except UserBannedInChannel as err:
                logging.error(f"{err}\n Бан от телеграма проверьте аккаунт в @Spambot: {chat.link}\n")
            except forbidden_403.Forbidden:
                continue
            except PersistentTimestampInvalid:
                # Большое кол-во чатов. С тайм-аутом между чатами, не успевает разослать спам в чаты, до новой рассылки
                continue
            except BadRequest as err:
                logging.error(f"{err}\nОшибка запроса {chat.link}\n")
                delete_chat(session_maker=session_maker,
                            name_chat=chat.link)
            except flood_420.FloodWait:
                # Тайм-аут между рассылкой сообщений.
                continue
            edit_time_post(session_maker, post.message_id)

