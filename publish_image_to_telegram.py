import os
import random
import time

import telegram
from dotenv import load_dotenv

from fetch_epic_images import fetch_epic_nasa_pictures
from fetch_nasa_images import fetch_nasa_pictures
from fetch_spacex_images import fetch_spacex_launch


def fill_directory(picture_directory, flight_number, nasa_api_key):
    fetch_spacex_launch(picture_path=f'{picture_directory}/spacex', flight_number=flight_number)
    fetch_nasa_pictures(quantity_pictures=20, picture_path=f'{picture_directory}/nasa_apod',
                        nasa_api_key=nasa_api_key)
    fetch_epic_nasa_pictures(quantity_pictures=5, picture_path=f'{picture_directory}/epic_nasa',
                             nasa_api_key=nasa_api_key)

def send_picture(picture_directory, flight_number, nasa_api_key, token, chat_id, timer, picture_user_path=None):
    bot = telegram.Bot(token=token)
    if picture_user_path == None:
        if not os.path.exists(picture_directory) or not os.listdir(f'{picture_directory}/'):
            fill_directory(picture_directory, flight_number, nasa_api_key)
            send_picture(picture_directory, flight_number, nasa_api_key, token, chat_id, timer)
        else:
            pictures = os.listdir(f'{picture_directory}/')
            while pictures:
                random_picture = random.choice(pictures)
                pictures.remove(random_picture)
                with open(f'{picture_directory}/{random_picture}', 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(timer)
            else:
                fill_directory(picture_directory, flight_number, nasa_api_key)
                send_picture(picture_directory, flight_number, nasa_api_key, token, chat_id, timer)
    else:
        with open(picture_user_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        time.sleep(timer)
        send_picture(picture_directory, flight_number, nasa_api_key, token, chat_id, timer)

if __name__ == '__main__':
    load_dotenv()
    flight_number = os.getenv('flight_number', default=108)
    nasa_api_key = os.environ['NASA_API_KEY']
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    timer = os.getenv('timer', default=14400)
    send_picture(picture_directory='images', flight_number=None, nasa_api_key=nasa_api_key,
                 token=token, chat_id=chat_id, timer=timer)
