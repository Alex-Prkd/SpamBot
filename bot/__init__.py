import os

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler


import config
from bot.handlers_bot.handlers import start_bot, edit_schedule_post, edit_schedule_minute, choice_minutes, choice_hours, \
    edit_schedule_hour, pause_sending, resume_sending, info_schedule, get_link_chat, get_all_chats, add_chat, \
    remove_chat, send_log_file, info_del_chat, change_account, send_json_env, save_new_env, send_instruction
from filters.filter import filter_minute, filter_hour, admin, request_json_file, check_env_file, \
    send_change_instruction

bot = Client(name=f"{config.InfoID.NAME}Bot",
             api_id=config.SettingsBot.API_ID,
             api_hash=config.SettingsBot.API_HASH,
             bot_token=config.SettingsBot.BOT_TOKEN
             )

bot.add_handler(MessageHandler(start_bot, (filters.command("start") | filters.regex("Назад")) & admin))
bot.add_handler(MessageHandler(edit_schedule_post, filters.regex("Изменить") & admin))
bot.add_handler(MessageHandler(choice_minutes, filters.regex("Минуты") & admin))
bot.add_handler(MessageHandler(choice_hours, filters.regex("Часы") & admin))
bot.add_handler(MessageHandler(pause_sending, filters.regex("Пауза") & admin))
bot.add_handler(MessageHandler(resume_sending, filters.regex("Возобновить") & admin))
bot.add_handler(MessageHandler(info_schedule, filters.regex("Информация") & admin))
bot.add_handler(MessageHandler(get_link_chat, filters.regex("Добавить чат") & admin))
bot.add_handler(MessageHandler(add_chat, filters.command("AddChat") & admin))
bot.add_handler(MessageHandler(info_del_chat, filters.regex("Удалить чат") & admin))
bot.add_handler(MessageHandler(remove_chat, filters.command("Del") & admin))
bot.add_handler(MessageHandler(get_all_chats, filters.regex("Список чатов") & admin))
bot.add_handler(MessageHandler(send_log_file, filters.regex("Журнал ошибок") & admin))
bot.add_handler(MessageHandler(change_account, filters.regex("Смена аккаунта") & admin))
bot.add_handler(MessageHandler(save_new_env, check_env_file))

bot.add_handler(CallbackQueryHandler(edit_schedule_minute, filter_minute))
bot.add_handler(CallbackQueryHandler(edit_schedule_hour, filter_hour))
bot.add_handler(CallbackQueryHandler(send_json_env, request_json_file))
bot.add_handler(CallbackQueryHandler(send_instruction, send_change_instruction))






