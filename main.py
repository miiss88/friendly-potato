from flask import Flask, render_template
import telebot

# Настройки
API_TOKEN = '362993215:AAEXcWK8oH-x28pu4rcnXxnB0TqXQY4qMe4'  # Замените на токен от BotFather
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Маршрут для главной страницы (интерфейс)
@app.route('/')
def index():
    return render_template('index1.html')

# Обработка команд Telegram
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Выберите категорию животных через интерфейс.")

# Запуск Flask
if __name__ == '__main__':
    app.run(debug=True)

