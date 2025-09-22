import os
import telebot

# Pega o token das variáveis de ambiente do Render
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Bot ativo 😎")

# Mantém o bot rodando
bot.polling(none_stop=True, interval=0, timeout=20)