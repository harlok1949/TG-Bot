import telebot

bot = telebot.TeleBot("5115489647:AAHDNqXtbDPdqMfOgbpLApZj7OyfDUvcuEI")

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Саламалейкум', parse_mode='html')


bot.polling(none_stop=True)