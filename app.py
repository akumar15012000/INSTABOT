import telebot
import util
import os
import time
from dotenv import load_dotenv

load_dotenv()

bot=telebot.TeleBot(os.getenv('api_key'))

try:
    cl=util.login()
except:
    print('Unsucessful Login')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing? Please Send Link to Download Reels")




@bot.message_handler(content_types=["sticker", "pinned_message", "photo", "audio"])
def reject(message):
    chat_id=message.chat.id

    bot.send_message(chat_id,'Please Send Link')

    

@bot.message_handler(content_types=["text"])
def reply(message):
    chat_id=message.chat.id
    
    url=message.text
    
    if 'https://' not in url:
        bot.send_message(chat_id,'Please Send Link')
        return
    
    try:
        address=util.fetch_reels(cl,url)
    except:
        bot.send_message(chat_id,'Either Accout is private or Link is Invalid')
    else:
        try:
            with open(address,'rb') as f:
                bot.send_video(chat_id,f)
        except:
            bot.send_message(chat_id,'Either Accout is private or Link is Invalid')

        time.sleep(10)
        os.remove(address)


bot.infinity_polling()