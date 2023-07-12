from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler


import config
from bot.handlers_bot.handlers import start_bot, edit_schedule_post, edit_schedule_minute, choice_minutes, choice_hours, \
    edit_schedule_hour, pause_sending, resume_sending, info_schedule, get_link_chat, get_all_chats, add_chat, \
    remove_chat
from filters.filter import filter_minute, filter_hour, admin, filter_remove_chat

bot = Client(name="SellerBot",
                 api_id=config.ApiTelegram.API_ID,
                 api_hash=config.ApiTelegram.API_HASH,
                 bot_token=config.SettingsBot.BOT_TOKEN)

bot.add_handler(MessageHandler(start_bot, (filters.command("start") | filters.regex("Назад")) & admin))
bot.add_handler(MessageHandler(edit_schedule_post, filters.regex("Изменить") & admin))
bot.add_handler(MessageHandler(choice_minutes, filters.regex("Минуты") & admin))
bot.add_handler(MessageHandler(choice_hours, filters.regex("Часы") & admin))
bot.add_handler(MessageHandler(pause_sending, filters.regex("Пауза") & admin))
bot.add_handler(MessageHandler(resume_sending, filters.regex("Возобновить") & admin))
bot.add_handler(MessageHandler(info_schedule, filters.regex("Информация") & admin))
bot.add_handler(MessageHandler(get_link_chat, filters.regex("Добавить чат") & admin))
bot.add_handler(MessageHandler(add_chat, filters.command("AddChat") & admin))
bot.add_handler(MessageHandler(get_all_chats, filters.regex("Список чатов") & admin))

bot.add_handler(CallbackQueryHandler(edit_schedule_minute, filter_minute))
bot.add_handler(CallbackQueryHandler(edit_schedule_hour, filter_hour))
bot.add_handler(CallbackQueryHandler(remove_chat, filter_remove_chat))




