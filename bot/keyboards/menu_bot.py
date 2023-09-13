from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


class StartMenu:
    menu = ReplyKeyboardMarkup(keyboard=[
        ["Изменить время рассылки ⏲"],
        ["Пауза ⏸"],
        ["Возобновить ▶️"],
        ["Информация ℹ️"],
        ["Добавить чат для рассылки ➕"],
        ["Удалить чат ➖"],
        ["Список чатов 📄"],
        ["Журнал ошибок 🗒"]
    ],
        resize_keyboard=True
    )


class MenuSchedule:
    menu = ReplyKeyboardMarkup(keyboard=[["Минуты"],
                                         ["Часы"],
                                         ["Назад"]],
                               resize_keyboard=True)


class ListMinutes:
    minutes = [[InlineKeyboardButton(text=str(minute * 10), callback_data=f"{minute * 10}_min")
                for minute in range(1, 6)]]
    menu = InlineKeyboardMarkup(minutes)


class ListHours:
    hours = [[InlineKeyboardButton(text=str(hour), callback_data=f"{hour}_hour")
              for hour in range(1, 9)]]

    menu = InlineKeyboardMarkup(hours)