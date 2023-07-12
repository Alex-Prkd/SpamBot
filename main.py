from pyrogram import idle

from app import app
from bot import bot


if __name__ == '__main__':
    app.start()
    bot.start()
    print("BOT STARTED!")
    idle()
    app.stop()
    bot.stop()

