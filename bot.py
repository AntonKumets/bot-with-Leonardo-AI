import telebot
from logic_ai import *
from config import *
import time

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
    message,
    "Это бот для генерации изображений с помощью Leonardo AI."
    "Просто напиши, какую картинку ты хочешь создать, и я сделаю её для тебя."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text
    status_message = bot.send_message(message.chat.id, "Генерирую картинку...")
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(1)
    image_path = f"generated_image_{message.chat.id}.jpg"
    api.generate_image(prompt, image_path)
    bot.delete_message(message.chat.id, status_message.message_id)
    with open(image_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

bot.polling()