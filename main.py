import telegram
import os

TOKEN=os.environ['TOKEN']
bot = telegram.Bot(TOKEN)

update = bot.getUpdates()
print(type(update[0]))