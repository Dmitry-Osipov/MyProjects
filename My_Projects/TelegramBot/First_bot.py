import random, telebot
from telebot import types
from secrets import bot_token


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    photo = open(r'C:\Users\dimao\OneDrive\Изображения\Обучение\Prikolnye_kartinki_s_nadpisyami_Privet_6_06131518.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='Random number')
    keyboard_2 = types.KeyboardButton(text='Password all elements')
    keyboard_3 = types.KeyboardButton(text='Password letters only')
    keyboard_4 = types.KeyboardButton(text='Password digits and signs only')
    markup.add(keyboard, keyboard_2, keyboard_3, keyboard_4)
    inline_markup = types.InlineKeyboardMarkup(row_width=True)
    inline_keyboard = types.InlineKeyboardButton("Currency conversion", url="https://cash.rbc.ru/converter.html?from=USD&to=RUR&sum=5&date=&rate=cbrf")
    inline_keyboard_2 = types.InlineKeyboardButton("Contact me", callback_data=1)
    inline_markup.add(inline_keyboard, inline_keyboard_2)
    bot.send_photo(chat_id, photo=photo)
    bot.send_message(chat_id, f'Hello, {first_name}!', reply_markup=markup)
    bot.send_message(chat_id, "Check this if you need", reply_markup=inline_markup)


@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Random number':
            bot.send_message(chat_id, f'Random number: {random.randint(1, 1000)}')
        elif message.text == 'Password all elements':
            password = ''
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            digits = '1234567890'
            signs = '_!?@#$%&-'
            sumlist = alphabet + alphabet2 + digits + signs
            for i in range(1, 25):
                password += random.choice(sumlist)
            bot.send_message(chat_id, password)
        elif message.text == 'Password letters only':
            password = ''
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            sumlist = alphabet + alphabet2
            for i in range(1, 25):
                password += random.choice(sumlist)
            bot.send_message(chat_id, password)
        elif message.text == 'Password digits and signs only':
            password = ''
            digits = '1234567890'
            signs = '_!?@#$%&-'
            sumlist = digits + signs
            for i in range(1, 25):
                password += random.choice(sumlist)
            bot.send_message(chat_id, password)


@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    chat_id = call.message.chat.id
    if call.message:
        if call.data == '1':
            bot.send_message(chat_id, 'My Telegram: @The_Real_DO')


bot.polling(none_stop=True)