import telebot

bot = telebot.TeleBot("youtoken")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id,  "Hello")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'You write: ' + message.text)

bot.polling(none_stop=True, interval=0)
