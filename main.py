import os, telebot
from flask import Flask
from threading import Thread

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CARD = "9762000123886250"
PHONE = "+992938246111"
order = 7006
users = {}

app = Flask('')

@app.route('/')
def home():
    return "BOT RUNNING"

def run():
    app.run(host='0.0.0.0',port=10000)

def keep():
    Thread(target=run).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, f"Assalomu alaykum {m.from_user.first_name}!\n\n🍩 Nazarov Donat Almaz!\n\n /menu - menyu")

@bot.message_handler(commands=['menu'])
def menu(m):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🍩 Donatlar", "☕ Ichimliklar", "📦 Buyurtma")
    bot.send_message(m.chat.id, "Menyuni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.send_message(m.chat.id, 
"Menyu uchun /menu bosing 😊")

keep()
bot.infinity_polling()

