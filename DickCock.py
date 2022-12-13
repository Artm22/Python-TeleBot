
import telebot
from telebot import types # для указание типов
from geopy import geocoders


API_TOKEN_YAN = 'bb2204f7-cc09-48ae-93a3-1cb99f4fd502'
API_TOKEN_ACC = 'knDAAJ3RCBHkXV8UCudHbPvwM1xIO83E'
API_TOKEN_BOT = '5825989518:AAHz6VaQ4IEAfsRNAwu4bryZKW-Ox4YPSCY'


bot = telebot.TeleBot(API_TOKEN_BOT)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Дать ему задание")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text = "Привет, {0.first_name}! Я тестовый бот на напоминания, погоду и события!!".format(message.from_user), reply_markup = markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет!!)")

    elif(message.text == "Дать ему задание"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton("Поставить напоминание")
        btn2 = types.KeyboardButton("Узнать погоду")
        btn3 = types.KeyboardButton("Узнать событие числом этого дня")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text = "Что мне сделать", reply_markup = markup)

    elif (message.text == "Узнать событие числом этого дня"):
        bot.send_message(message.chat.id, text = "Вот какие события были в этот день...")


    elif (message.text == "Узнать погоду"):
        



    elif (message.text == "Поставить напоминание"):
        bot.send_message(message.chat.id, text = "Введите время и дату в формате ЧЧ:ММ ДД.ММ.ГГ")
    

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("Дать ему задание")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text = "Вы вернулись в главное меню", reply_markup = markup)
    else:
        bot.send_message(message.chat.id, text = "На такую комманду я не запрограммирован...")
    



bot.polling(none_stop = True)



