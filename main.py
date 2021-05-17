from telegram.ext import Updater, CommandHandler
from config import API_TOKEN
import logging


updater = Updater(token=API_TOKEN, use_context=True)

dp = updater.dispatcher

#It gives you when and why things don't work as expected.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,
                    level=logging.DEBUG)

def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salom men botman. Ko'p ishingizni men orqali avtomatlashtirishingiz mumkin!" )

def main():
    start_handler= CommandHandler('start', start_command)
    dp.add_handler(start_handler)

    updater.start_polling()

main()