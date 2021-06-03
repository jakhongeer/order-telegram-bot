from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters)
from AuthConfig.keys import API_TOKEN
import logging
from errror_handler import error_handler
import html
import json
import logging
import traceback
from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler

from telegram.ext import InlineQueryHandler

from telegram import InlineQueryResultArticle, InputTextMessageContent

# It gives you when and why things don't work as expected.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)



def start_command(update, context):
    """When user sends start command do these"""
    # For sending a photo to user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('assets/hello_world.png', 'rb'))
    # For sending a message
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello buddy👋 Welcome to our 'theteam' bot.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def unknown(update, context):
    """Defines unknown commands and report them to user
    It should be added last part of bot. Otherwise it may be ignored the commands which are written after this"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")



def main():
    updater = Updater(token=API_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start_command)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # caps_handler = CommandHandler('caps', caps)
    # dispatcher.add_handler(caps_handler)
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)



    # ...and the error handler
    dispatcher.add_error_handler(error_handler)

    updater.start_polling()
