import telebot
from datetime import datetime

bot = telebot.TeleBot('token')

start = datetime.now()

ends = datetime.now()

workspeed = format(ends - start)