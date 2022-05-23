import telebot
from telebot import types

bot = telebot.TeleBot("5344285897:AAETtCyA93hLe3OWFdILilpHY99cW7V6KiU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	mess = f'Hello,{message.from_user.first_name}!'
	bot.send_message(message.chat.id,mess, parse_mode='html')



@bot.message_handler(commands=['listof'])
def listof(message):
	markup = types.ReplyKeyboardMarkup()
	btn1 = types.KeyboardButton('Go to website')
	btn2 = types.KeyboardButton('Go to the list of flights')
	markup.add(btn1,btn2)
	bot.send_message(message.chat.id,'Make your choise', reply_markup=markup)
bot.infinity_polling()