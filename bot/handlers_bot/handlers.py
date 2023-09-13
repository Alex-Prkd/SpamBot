from pyrogram.types import Message, CallbackQuery
from sqlalchemy import exc

import db
from bot.keyboards.menu_bot import StartMenu, MenuSchedule, ListMinutes, ListHours
from db.commands.reader import all_chats
from db.commands.write import write_new_chat, delete_chat
from schedule_post import sending_post


def start_bot(_, message: Message):
    keyboard = StartMenu().menu
    message.reply("Главное меню", reply_markup=keyboard)


def edit_schedule_post(_, message: Message):
    keyboards = MenuSchedule().menu
    message.reply("Выберите вариант: ", reply_markup=keyboards)


def choice_minutes(_, message: Message):
    keyboards = ListMinutes.menu
    message.reply("Выберите интервал", reply_markup=keyboards)


def choice_hours(_, message: Message):
    keyboards = ListHours.menu
    message.reply("Выберите интервал", reply_markup=keyboards)


def pause_sending(_, message: Message):
    message.reply("Рассылка на паузе")
    sending_post.pause_schedule()


def resume_sending(_, message: Message):
    message.reply("Рассылка включенна")
    sending_post.resume_schedule()


def edit_schedule_minute(_, callback_query: CallbackQuery):
    """"""
    minute = int(callback_query.data.split("_")[0])
    sending_post.edit_schedule_minute(interval=minute)
    callback_query.answer(f"Инетрвал изменён на {minute} минут.")


def edit_schedule_hour(_, callback_query: CallbackQuery):
    """"""
    hour = int(callback_query.data.split("_")[0])
    sending_post.edit_schedule_hour(interval=hour)
    callback_query.answer(f"Инетрвал изменён на {hour} час(ов).")


def info_schedule(_, message: Message):
    info = str(sending_post.info_schedule()).split(sep=" ")  # Список с инфо-ей о рассылке
    interval = info[2][9:16]
    next_run = info[-2]
    message.reply(text=f"Интервал рассылки: {interval}\n"
                       f"Ближайшая: {next_run}")


def get_link_chat(_, message: Message):
    message.reply(text="ВАЖНО! \nВаш аккаунт должен быть участником добавляемого чата!")
    message.reply(text=f"Отправьте сообщение в формате:\n"
                       f"/AddChat\n"
                       f"'Ссылка чата (пр. https://t.me/QWERTY) '")


def info_del_chat(_, message: Message):
    message.reply(text="Отправьте сообщение в формате:\n"
                       f"/Del\n"
                       f"'Ссылка чата (пр. https://t.me/QWERTY) '")


def add_chat(_, message: Message):
    try:
        text = message.text.split(sep="\n")     # ["/AddChat", "https://QWERTY"]
        link_chat = text[1].split("https://t.me/")[1]   # ["QWERTY"]
        write_new_chat(session_maker=db.session_maker,
                       link_chat=str(link_chat))
        message.reply(text=f"Чат t.me/{link_chat} - добавлен в список рассылки.")
    except IndexError:
        message.reply(text="Ошибка ввода!\n"
                           "Проверьте введённые данные и попробуйте снова.")
    except exc.IntegrityError:
        message.reply(text=f"Ошибка!\nЧат уже в списке!")


def get_all_chats(_, message: Message):
    result = all_chats(session_maker=db.session_maker)
    if len(result) != 0:
        chats = ""
        for chat in result:
            chats += f"https://t.me/{chat.link}\n"
        message.reply(text=chats)
    else:
        message.reply(text="Список чатов пуст.")


def remove_chat(_, message: Message):
    data = message.text.split("\n")     # (Del, https://t.me/qwerty)
    link_chat = data[1].split("/")[3]   # qwerty

    delete_chat(session_maker=db.session_maker,
                name_chat=link_chat)
    message.reply(text=f"Чат https://t.me/{link_chat} удалён.")


def send_log_file(_, message: Message):
    message.reply_document(document="log.log")