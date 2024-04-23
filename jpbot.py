#I would like to declare that this code was written by AI as well
#IM LAZY TO CONTINUE UNLESS THERES MORE IDEAS
#--jianping

import os

import telebot
import random
from qotdList import quotes
from telebot import types
#from trivia import currentQuestion

BOT_TOKEN = os.environ.get('BOT_TOKEN')

playerScore = 0

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['ilovejp', 'majestyjp', 'start', 'hijp'])
def send_welcome(message):
    bot.reply_to(message, "What you want? Also uk, you can use the command '/help' for more")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Update 1.1.1 is out with updated UX together with a new feature heavily requested! Wait What theres a game you always lose now?? DO /help for all the commands and /start to begin using the bot! 'ilovejp', 'majestyjp', 'start', or 'hijp' to talk to him. \n \n Run the following commands for your needs: \n you are sad: '/imsad' \n you are angry: '/imangry' \n you want to book a meal with jian ping: '/eat'. \n JP's QUOTE OF THE DAY: '/QOTD' \n \n NEW UPDATE!! do '/fart', if you want to play a losing game do '/im_a_loser'!")

@bot.message_handler(commands=['fart'])
def fart(message):
    chat_id = message.chat.id
    audio_file = open('C:/Users/jianp/OneDrive/Desktop/randomCodes/fart-145914.mp3', 'rb')
    bot.send_audio(chat_id, audio_file)

@bot.message_handler(commands=['imsad'])
def sadPerson(message):
    bot.reply_to(message, "owh no why you sad lol too bad life's hard get a helmet heeheeheehaw")

@bot.message_handler(commands=['imangry'])
def angryPerson(message):
    bot.reply_to(message, "dont angry lah later you go bald lmao")

@bot.message_handler(commands=['eat'])
def eat(message):
    bot.reply_to(message, "welllll... im kind of busy... lol eat alone loser")

@bot.message_handler(commands=['QOTD'])
def QOTD(message):
    random_quote = random.choice(quotes)
    bot.reply_to(message, random_quote)

@bot.message_handler(commands=['im_a_loser'])
def losingGame(message):
    bot.reply_to(message, "Welcome to a game of you losing lol loser.")
    bot.reply_to(message, "It'll just be a simple game of Rock Paper Scissors. use commands '/rock', '/paper' or '/scissors' to lose lol loser YOU WILL NEVER WIN AGAINST ME HAHAHAHHAHA")
    # detectChoice()

@bot.message_handler(commands=['admin'])
def adminPerms(message):
    bot.reply_to(message, message)

#@bot.message_handler(commands=['quiz'])
#def quiz(message):
#   triviaQuestion = currentQuestion
#    bot.reply_to(message, triviaQuestion)

@bot.message_handler(commands=['rock', 'paper', 'scissors'])
def winningGame(message):
    if (message.text == "/rock"):
        bot.reply_to(message, "waiting")
        bot.reply_to(message, "I pick paper u lose lol loser u cant win me HAHHAHAHAHA HEHEHEHAW")
    elif (message.text == "/paper"):
        bot.reply_to(message, "waiting")
        bot.reply_to(message, "I pick scissors u lose like always HAHA")
    elif (message.text == "/scissors"):
        bot.reply_to(message, "waiting")
        bot.reply_to(message, "I pick rock u lose HAHA im always right and i will always pick rock")

bot.infinity_polling() #FOC taught this polling and interupt

#functions lol 
#basic syntax for message handling
#@bot.message_handler(commands=['imangry'])
#def angryPerson(message):
    #bot.reply_to(message, "dont angry lah later you go bald lmao")



#commands lol
#'ilovejp', 'majestyjp', 'start', or 'hijp' to talk to him.
#\n \n Run the following commands for your needs: \n you are sad: '/imsad' \n you are angry: '/imangry' \n you want to book a meal with jian ping: '/eat'. \n JP's QUOTE OF THE DAY: '/QOTD'