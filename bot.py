from ctypes import resize


import telebot
from telebot import types
import config



url = "https://api.openweathermap.org/data/2.5/weather"
bot = telebot.TeleBot(config.TOKEN)

api_weather='6393c79d9a5de74eadcf04f7558edd96'

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 =  types.KeyboardButton('Валюты')
    button2 = types.KeyboardButton('Ближайший банк')
    button3 = types.KeyboardButton('Справочный телефон')
    button4 = types.KeyboardButton('Наш сайт')
    markup.add(button1, button2, button3,button4)
    bot.send_message(message.chat.id, 'Привет {0.first_name} Я ваш ассистент !'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.chat.type == 'private':
        if message.text == 'Валюты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Доллар')
            button2 = types.KeyboardButton('Рубль')
            back = types.KeyboardButton('Назад')
            markup.add(button1, button2, back)
            bot.send_message(message.chat.id, 'Выберите валюту: ', reply_markup=markup)
        elif message.text == 'Ближайший банк':
            markup= types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_location(message.from_user.id,42.876761, 74.588814,)
        elif message.text == 'Справочный телефон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_contact(message.chat.id,"0312610613", 'DemirBank')
        elif message.text == 'Наш сайт':
            bot.send_message(message.chat.id,'https://demirbank.kg/ru')
           
        if message.text == 'Доллар':
            markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Покупка')
            button2 = types.KeyboardButton('Продажа')
            back = types.KeyboardButton('Назад')
            markup.add(button1,button2,back)
            bot.send_message(message.chat.id,'Что хотите сделать' ,reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 =  types.KeyboardButton('Валюты')
            button2 = types.KeyboardButton('Ближайший банк')
            button3 = types.KeyboardButton('Справочный телефон')
            button4 = types.KeyboardButton('Наш сайт')
            markup.add(button1, button2, button3,button4)
            bot.send_message(message.chat.id, 'Дальше:', reply_markup=markup)
        elif message.text == 'Покупка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
'USD: 94 \n '           
'EUR: 105\n'
'RUB: 0,830\n'
'KZT: 0,1502\n'
'CNY: 12,50\n'
'Средний курс в Бишкеке\n')
        elif message.text == 'Продажа':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
'USD: 97 \n'
'EUR: 108 \n'
'RUB: 1,12 \n'
'KZT: 0,2 \n'
'CNY: 20,00\n'
'Средний курс в Бишкеке \n') 
        elif message.text == 'Рубль':
            markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Покупка')
            button2 = types.KeyboardButton('Продажа')
            back = types.KeyboardButton('Назад')
            markup.add(button1,button2,back)
            bot.send_message(message.chat.id, 'Что хотите сделать:', reply_markup=markup)
        elif message.text == 'Покупка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
'USD: 94 \n '           
'EUR: 105 \n'
'RUB: 0,830\n'
'KZT: 0,1502\n'
'CNY: 12,50  \n'
'Средний курс в Бишкеке\n')
        elif message.text == 'Продажа':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
'USD: 97 \n'
'EUR: 108 \n'
'RUB: 1,12 \n'
'KZT: 0,2   \n'
'CNY: 20,00  \n'
'Средний курс в Бишкеке \n') 
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Купить')
            button2 = types.KeyboardButton('Продать')
            back = types.KeyboardButton('Назад')
            markup.add(button1,button2,back)
            bot.send_message(message.chat.id,'Главное меню')


bot.polling(non_stop=True)


