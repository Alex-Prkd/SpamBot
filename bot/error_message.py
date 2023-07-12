import config


def error_link_chat(link):
    from bot import bot
    bot.send_message(chat_id=config.InfoID.ADMIN_ID, text=f"Произошла ошибка при отправке поста в чат: t.me/{link}.\n"
                                                          f"Чат исключен из списка рассылки.")


def error_send_channel(link):
    from bot import bot
    bot.send_message(chat_id=config.InfoID.ADMIN_ID, text=f"Произошла ошибка при отправке поста в: t.me/{link}.\n"
                                                          f"Канал исключен из списка рассылки.")