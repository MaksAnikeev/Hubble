import telegram
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ['TG_TOKEN']
chat_id = '@AnikeevMaks1'

bot = telegram.Bot(token=token)

# bot.send_message(chat_id=chat_id, text="ЕЕЕЕ у меня получилось прислать сообщение в канал")
bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_10.jpg', 'rb'))
