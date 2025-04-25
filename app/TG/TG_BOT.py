import telebot
from DataBase import *
from CodeFromDisplay import way, encode_in_message_on_display, decode_message_from_display
from random import *
from sqlite3 import *

bot = telebot.TeleBot("token")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name} ' \
           f'{message.from_user.last_name if message.from_user.last_name is not None else ""}!'
    bot.send_message(message.chat.id, mess)
    make_new_line_in_database(message.chat.id)
    print(message.chat.id)
    help(message)


@bot.message_handler(commands=['help'])
def help(message):
    mess_help = 'I can:\n\t1.\tgive you bonus points for returned bott' \
                'les\n\t2.\ttell you your current balance\n\t3.\ttell where you can spend bonus points\n' \
                '\n/topup - to give you bonus points\n/balance - to tell you your current balance\n/info - ' \
                'to get information about spend bonus points\n/help - to repeat this message'
    to_pin = bot.send_message(message.chat.id, mess_help).message_id
    bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin)


@bot.message_handler(commands=['topup'])
def topup(message):
    mess_topup = f'Please enter the code from the display'
    k = ''
    r = bot.send_message(message.chat.id, mess_topup, reply_markup=k)
    bot.register_next_step_handler(r, topup2)


def topup2(message):
    k = decode_message_from_display(message.text)
    if k == int(-1e100):
        bot.send_message(message.chat.id, 'You have entered a non-existent code')
        return
    add_to_balance_in_database(message.chat.id, k)
    balance(message)


@bot.message_handler(commands=['balance'])
def balance(message):
    bot.send_message(message.chat.id, f'Your balance: {get_balance_by_telegram_id(message.chat.id)} bonus points')


@bot.message_handler(commands=['info'])
def info(message):
    mess_info = f'{None}'
    bot.send_message(message.chat.id, mess_info)


bot.polling(none_stop=True)
