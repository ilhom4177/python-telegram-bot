import telegram
import os

TOKEN=os.environ['TOKEN']
bot = telegram.Bot(TOKEN)

update = bot.getUpdates()[-1]
update_id = update.update_id
text = update.message.text

chat_id = update.message.chat.id

bot.sendMessage(chat_id, text)