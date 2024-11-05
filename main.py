import telebot 
from config import token

from logic import Pokemon

from datetime import datetime, timedelta

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)

        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
        bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        res = pok.info()
        bot.send_message(message.chat.id,res)
        
@bot.message_handler(commands=['feed'])
def feed(message):
    if  message.from_user.username in Pokemon.pokemons.keys():
        
        pok = Pokemon.pokemons[message.from_user.username]
        res = pok.feed()
        bot.send_message(message.chat.id, res)

    else:
        bot.send_message(message.chat.id, 'oo tebya net pokemona')



bot.infinity_polling(none_stop=True)

