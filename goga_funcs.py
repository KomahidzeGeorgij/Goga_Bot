import telebot
from random import choice

def hello_user(bot, message):
    bot.send_message(message.chat.id, 'Привет! Меня зовут Гога, я тг бот, чем я могу помочь?')

def answer(bot, message):
    variations = ["Отлично!", "Плохо((", "Нормально"]
    variation = choice(variations)
    bot.send_message(message.chat.id, variation)
