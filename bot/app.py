import telebot
from token_1 import my_token

bot = telebot.TeleBot(my_token)


@bot.message_handler(commands=['start'])
def wlecome_To(message):
    bot.send_message(message.chat.id, 'hello world')


bot.infinity_polling()
