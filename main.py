import telebot
import datetime
import os
import random


API_TOKEN = os.environ.get('TELEBOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

aneks = []
with open('data.txt') as file:
    aneks = file.read().split("===")
start_message = ''

with open('start_message.txt') as file:
    start_message = file.read()


to_add = set()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, start_message)


@bot.message_handler(commands=['anek'])
def echo_all(message):
    bot.reply_to(message, aneks[random.randint(0, len(aneks)) - 1])
    # logging
    print(datetime.datetime.now(), message.from_user.id, (message.text + " " * 20)[:20],
          message.from_user.username, sep='\t')


@bot.message_handler(commands=['add'])
def echo_all(message):
    bot.reply_to(message, 'Отправь свой анек.')
    to_add.add(message.from_user.id)
    # logging
    print(datetime.datetime.now(), message.from_user.id, (message.text + " " * 20)[:20],
          message.from_user.username, sep='\t')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.from_user.id in to_add:
        aneks.append(message.text)
        to_add.remove(message.from_user.id)
        bot.reply_to(message, 'Анек успешно добавлен.')
    else:
        bot.reply_to(message, 'Нет такой команды.')
        # logging
        print(datetime.datetime.now(), message.from_user.id, (message.text + " " * 20)[:20],
              message.from_user.username, sep='\t')


bot.infinity_polling()
