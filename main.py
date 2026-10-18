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
def home(): return "BOT RUNNING"
def run(): app.run(host='0.0.0.0',port=8080)
def keep(): Thread(target=run).start()

@bot.message_handler(commands=['start'])
def s(m):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("💎 Free Fire","🎮 PUBG")
    bot.send_message(m.chat.id, "🔥 Nazarov Shop\nOyin tanlang:", reply_markup=kb)

@bot.message_handler(func=lambda x: "Free Fire" in x.text)
def ff(m):
    users[m.chat.id]={'game':'
