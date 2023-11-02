import telebot
from telebot import types

bot = telebot.TeleBot('6808276515:AAFV7_ztOXHZJ9XVzQ8N7OQPMk7srsfQELc')

keyboard = types.ReplyKeyboardMarkup()

button = types.KeyboardButton('Играть')

keyboard.add(button)

@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
    # print(message)
    bot.send_message(message.chat.id, 'How are you?', reply_markup=keyboard)
    bot.register_next_step_handler(message, func)

def func(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, 'Начнем игру')
    else:
        bot.send_message(message.chat.id, 'Пока')

@bot.message_handler(content_types=['sticker'])
def echo_all(message):
    bot.send_message(message.chat.id, message.text)
    print(message.sticker.file_id)
    bot.reply_to(message, message.sticker.file_id)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEKqnJlQ6GI6Qpa-oCMux40AzyTdFAYEQAC-wADVp29ClYO2zPbysnmMwQ')

bot.polling()
# monkeytype
