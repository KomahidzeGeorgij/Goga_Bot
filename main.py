import telebot
from goga_funcs import *

key = '6751558513:AAHVvPojlzhV7aDl-YnFPIPY9XQg0_lnET4'
bot = telebot.TeleBot(key)


@bot.message_handler(commands=['start'])
def handle_start(message):
    hello_user(bot, message)


@bot.message_handler(func=lambda message: message.text.lower() == 'как дела?')
def handle_answer(message):
    answer(bot, message)


if __name__ == "__main__":
    bot.polling(none_stop=True)
