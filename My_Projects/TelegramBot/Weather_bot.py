import datetime, requests, math, telebot
from telebot import types
from secrets import bot_token_weather
from secrets import weather_api


bot = telebot.TeleBot(bot_token_weather)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='Тула')
    keyboard_2 = types.KeyboardButton(text='Новомосковск')
    keyboard_3 = types.KeyboardButton(text='Кимовск')
    keyboard_4 = types.KeyboardButton(text='Киреевск')
    keyboard_5 = types.KeyboardButton(text='Ясногорск')
    keyboard_6 = types.KeyboardButton(text='Москва')
    markup.add(keyboard, keyboard_2, keyboard_3, keyboard_4, keyboard_5, keyboard_6)
    bot.send_message(chat_id, f'Привет, {first_name}! Я чат-бот, который выводит погоду в нужных городах. Нажми на кнопку - получишь результат', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    if message.text == 'Москва':
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid={weather_api}')
        data = response.json()
        city = data['name']
        cur_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Морось \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, я не понимаю, что там за погода...'

        bot.send_message(chat_id, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_temp}°C {wd}\n'
                            f'Влажность: {humidity}%\nДавление: {math.ceil(pressure/1.333)} мм.рт.ст.\nВетер: {wind} м/с\n'
                            f'Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\nПродолжительность дня: {length_of_day}\n'
                            f'Хорошего дня!😸'
                            )
    elif message.text == 'Новомосковск':
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=новомосковск&lang=ru&units=metric&appid={weather_api}')
        data = response.json()
        city = data['name']
        cur_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Морось \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, я не понимаю, что там за погода...'

        bot.send_message(chat_id, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_temp}°C {wd}\n'
                            f'Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст.\nВетер: {wind} м/с\n'
                            f'Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\nПродолжительность дня: {length_of_day}\n'
                            f'Хорошего дня😸!'
                            )
    elif message.text == 'Ясногорск':
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=ясногорск&lang=ru&units=metric&appid={weather_api}')
        data = response.json()
        city = data['name']
        cur_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Морось \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, я не понимаю, что там за погода...'

        bot.send_message(chat_id, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_temp}°C {wd}\n'
                            f'Влажность: {humidity}%\nДавление: {math.ceil(pressure/1.333)} мм.рт.ст.\nВетер: {wind} м/с\n'
                            f'Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\nПродолжительность дня: {length_of_day}\n'
                            f'Хорошего дня😸!'
                            )
    elif message.text == 'Киреевск':
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=киреевск&lang=ru&units=metric&appid={weather_api}')
        data = response.json()
        city = data['name']
        cur_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Морось \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, я не понимаю, что там за погода...'

        bot.send_message(chat_id, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_temp}°C {wd}\n'
                            f'Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст.\nВетер: {wind} м/с\n'
                            f'Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\nПродолжительность дня: {length_of_day}\n'
                            f'Хорошего дня!😸'
                            )
    elif message.text == 'Тула':
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=тула&lang=ru&units=metric&appid={weather_api}')
        data = response.json()
        city = data['name']
        cur_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Морось \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, я не понимаю, что там за погода...'

        bot.send_message(chat_id, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_temp}°C {wd}\n'
                            f'Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст.\nВетер: {wind} м/с\n'
                            f'Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\nПродолжительность дня: {length_of_day}\n'
                            f'Хорошего дня!😸'
                            )
    elif message.text == 'Кимовск':
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=кимовск&lang=ru&units=metric&appid={weather_api}')
        data = response.json()
        city = data['name']
        cur_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        code_to_smile = {
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U00002601',
            'Rain': 'Дождь \U00002614',
            'Drizzle': 'Морось \U00002614',
            'Thunderstorm': 'Гроза \U000026A1',
            'Snow': 'Снег \U0001F328',
            'Mist': 'Туман \U0001F32B'
        }

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, я не понимаю, что там за погода...'

        bot.send_message(chat_id, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_temp}°C {wd}\n'
                            f'Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст.\nВетер: {wind} м/с\n'
                            f'Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\nПродолжительность дня: {length_of_day}\n'
                            f'Хорошего дня😸!'
                            )


bot.polling(none_stop=True)