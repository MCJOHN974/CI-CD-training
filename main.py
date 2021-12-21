import sys

import telebot
import datetime
import os


API_TOKEN = os.environ.get('TELEBOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    if message.text == API_TOKEN:
        sys.exit("SIGINT from telegram messages")
    # logging
    print(datetime.datetime.now(), message.from_user.id, (message.text + " " * 20)[:20],
          message.from_user.username, sep='\t')


bot.infinity_polling()
