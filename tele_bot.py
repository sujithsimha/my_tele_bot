from telegram.ext import Updater,CommandHandler
import requests #gets data from cloud

def bot_command():
    context= requests.get('https://random.dog/woof.json').json()
    url=context['url']
    return url

def dog(bot,update):
    url=bot_command()
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo=url)


u=Updater('1277896979:AAGbPOEyFsOhhtzIu44kLqaDpLyaJwR2USA')
dp=u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
u.start_polling()
u.idle()
  

    
