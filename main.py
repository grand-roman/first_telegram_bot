import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

updater = Updater(token=os.getenv('TOKEN'))

def say_hi(bot, update):
    bot.message.reply_text('Привет')

def wake_up(bot, update):
    bot.message.reply_text('Спасибо, что включили меня')

updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()