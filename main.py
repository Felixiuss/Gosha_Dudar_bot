import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6029730650:AAGaSgMfatEyj8M69XKrVjO-xFh0SWgjLNs')


# переходит по указанной ссылке открывая браузер
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://itproger.com')


# обработчик команд начинающихся с /
@bot.message_handler(commands=['start', 'main', 'bok'])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} {message.from_user.last_name}')


# вывод словаря со всеми ключами
@bot.message_handler(commands=['key'])
def main(message):
    bot.send_message(message.chat.id, message)


# вывод текста с использованием тегов html
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


#  обработка простых текстовых сообщений
@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} {message.from_user.last_name}')
    # с приставкой - ответ на вопрос
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


# # ответ на отправленное фото
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     bot.reply_to(message, 'What is biutiful photo!')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to site', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change the text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What is biutiful photo!', reply_markup=markup)


bot.polling(none_stop=True)  # бесконечный цикл выполнения