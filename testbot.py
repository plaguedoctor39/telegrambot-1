import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def response(message):
    if message.text.lower() == 'durak' :
    bot.reply_to(message, 'Sam {!s}'.format(message.text))
    else:
        bot.send_message(message.chat.id, message.text)


# Start
bot.polling(none_stop=True)




