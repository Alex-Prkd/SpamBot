import logging

from pyrogram import idle

from app import app
from bot import bot


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    app.start()
    bot.start()
    print("BOT STARTED!")
    idle()
    print("BOT STOPPED!")
    try:
        bot.log_out()
    except Exception as err:
        print(err)
        print(type(err).__name__)


