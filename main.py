from time import sleep

from pyrogram import idle

import config
from app import app
from bot import bot


if __name__ == '__main__':
    app.start()
    bot.start()
    print("BOT STARTED!")
    idle()
    app.stop()
    bot.stop()

