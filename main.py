from telegram import Bot
import os
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))


chad_id = os.getenv('chad_id')

text = 'срочно'

bot.send_message(chad_id, text)