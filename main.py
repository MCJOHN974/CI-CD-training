import telebot
import datetime
import time

API_TOKEN = '5016711953:AAE8o4lJCsKtIk2R2J5bh5_KhxPjrkh5C1Q'


bot = telebot.TeleBot(API_TOKEN)
for i in range(100):
    bot.send_message(580878176, "Ты пидор")
    time.sleep(3)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

    # logging
    print(datetime.datetime.now(), message.from_user.id, (message.text + " " * 20)[:20],
          message.from_user.username, sep='\t')


bot.infinity_polling()
