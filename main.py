from telegram.ext import Updater, CommandHandler
from config import API_TOKEN
import logging


updater = Updater(token=API_TOKEN, use_context=True)

dp = updater.dispatcher

#It gives you when and why things don't work as expected.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,
                    level=logging.INFO)

# when user sends start command do these
def start_command(update, context):
    # For sending a photo to user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('assets/hello_world.png', 'rb'))
    # For sending a message
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello buddy👋 Welcome to our 'theteam' bot." )
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Tilni tanlang:\nВыберите язык: \nChoose the language:")

    context.bot.send_message(chat_id=update.effective_chat.id, text="Click OK to continue:")


def main():
    start_handler= CommandHandler('start', start_command)
    dp.add_handler(start_handler)

    updater.start_polling()

