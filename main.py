from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters)
from AuthConfig.keys import API_TOKEN
import logging

#It gives you when and why things don't work as expected.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,
                    level=logging.DEBUG)


# when user sends start command do these
def start_command(update, context):
    # For sending a photo to user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('assets/hello_world.png', 'rb'))
    # For sending a message
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello buddy👋 Welcome to our 'theteam' bot." )



#echoes all text messages to users.
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text.lower())

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)



def main():
    updater = Updater(token=API_TOKEN, use_context=True)

    dp = updater.dispatcher

    start_handler= CommandHandler('start', start_command)
    dp.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)

    caps_handler = CommandHandler('caps', caps)
    dp.add_handler(caps_handler)


    updater.start_polling()

