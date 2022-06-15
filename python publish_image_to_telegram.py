import os
import random

import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.environ['TG_TOKEN']
chat_id = '@AnikeevMaks1'

picture_directory = 'images'

bot = telegram.Bot(token=token)
random_picture = random.choice(os.listdir(f'{picture_directory}/'))
bot.send_document(chat_id=chat_id,
                  document=open(f'{picture_directory}/{random_picture}', 'rb'))
