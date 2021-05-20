from telegram.ext import Updater, CommandHandler
from config import API_TOKEN
import logging
from uuid import uuid4


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

def put(update, context):
    """Usage: /put value"""
    # Generate ID and separate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    value = update.message.text.partition(' ')[2]

    # Store value
    context.user_data[key] = value
    # Send the key to the user
    update.message.reply_text(key)

def get(update, context):
    """Usage: /get uuid"""
    # Seperate ID from command
    key = context.args[0]

    # Load value and send it to the user
    value = context.user_data.get(key, 'Not found')
    update.message.reply_text(value)

def main():
    start_handler= CommandHandler('start', start_command)
    dp.add_handler(CommandHandler('put', put))
    dp.add_handler(CommandHandler('get', get))
    dp.add_handler(start_handler)

    updater.start_polling()

