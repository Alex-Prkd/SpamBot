from filters.filter import saved_messages
from pyrogram import Client
from pyrogram.handlers import MessageHandler

import config
from app.handlers.hanlders import my_function

app = Client(name="Nikita",
             api_id=config.ApiTelegram.API_ID,
             api_hash=config.ApiTelegram.API_HASH,
             phone_number=config.InfoID.PHONE
             )


app.add_handler(MessageHandler(my_function, saved_messages))

