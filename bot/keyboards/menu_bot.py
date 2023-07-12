from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


class StartMenu:
    menu = ReplyKeyboardMarkup(keyboard=[
        ["Изменить время рассылки ⏲"],
        ["Пауза ⏸"],
        ["Возобновить ▶️"],
        ["Информация ℹ️"],
        ["Добавить чат для рассылки ➕"],
        ["Список чатов 📄"]
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


class RemoveChat:
    def __init__(self, id, link):
        self.id = str(id)
        self.link = link
        self.remove = [[InlineKeyboardButton(text="Удалить", callback_data=f"remove_{self.id}_{self.link}")]]
        self.button = InlineKeyboardMarkup(self.remove)