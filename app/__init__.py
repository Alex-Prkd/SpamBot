from filters.filter import saved_messages, filter_buyer
from pyrogram import Client
from pyrogram.handlers import MessageHandler

import config
from app.handlers.hanlders import my_function, response_buyer

app = Client(name=config.InfoID.NAME,
             api_id=config.ApiTelegram.API_ID,
             api_hash=config.ApiTelegram.API_HASH,
             phone_number=config.InfoID.PHONE
             )


app.add_handler(MessageHandler(my_function, saved_messages))
app.add_handler(MessageHandler(response_buyer, filter_buyer), group=1)

