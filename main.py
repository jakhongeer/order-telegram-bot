from telegram.ext import *
from responses import sampleresponses
from config import Api_Token

print("Lezzz go!!..")

def start_command(update, context):
    update.message.reply_text("Type something to get started..")
    context.bot.send_photo(chat_id=chat_id, photo='https://telegra.ph/Hello-world-05-16-17')


def help_command(update, context):
    update.message.reply_text("greet with bot (hi, hello)\nask 'who are you?'\nask a time ('time')")






def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sampleresponses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}!")


def main():
    updater = Updater(Api_Token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()

