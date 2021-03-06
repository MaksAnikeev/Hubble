import os
import random
import time

import telegram
from dotenv import load_dotenv

from fetch_earth_images_from_nasa_ import fetch_earth_pictures_from_nasa
from fetch_space_images_from_nasa_ import fetch_space_pictures_from_nasa
from fetch_spacex_launch_images import fetch_spacex_launch


def fill_directory(picture_directory, flight_number, nasa_api_key):
    fetch_spacex_launch(picture_path=f'{picture_directory}/spacex',
                        flight_number=flight_number)
    fetch_space_pictures_from_nasa(pictures_quantity=20,
                        picture_path=f'{picture_directory}/nasa_apod',
                        nasa_api_key=nasa_api_key)
    fetch_earth_pictures_from_nasa(pictures_quantity=5,
                             picture_path=f'{picture_directory}/epic_nasa',
                             nasa_api_key=nasa_api_key)


def send_random_space_pictures(picture_directory, flight_number, nasa_api_key, chat_id, token, timer):
    pictures = os.listdir(f'{picture_directory}/')
    while pictures:
        random_picture = random.choice(pictures)
        send_picture(chat_id, token, picture_path=f'{picture_directory}/{random_picture}')
        pictures.remove(random_picture)
        time.sleep(timer)
    else:
        fill_directory(picture_directory, flight_number, nasa_api_key)
        send_random_space_pictures(picture_directory, flight_number, nasa_api_key, chat_id, token, timer)


def send_picture(chat_id, token, picture_path):
    bot = telegram.Bot(token=token)
    with open(picture_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def send_pictures_to_telegram(picture_directory, flight_number, nasa_api_key, chat_id, token, timer,
                 picture_user_path=None):
    if picture_user_path:
        send_picture(chat_id, token, picture_path=picture_user_path)
        time.sleep(timer)
        send_pictures_to_telegram(picture_directory, flight_number, nasa_api_key, chat_id, token, timer)
    else:
        if os.path.exists(picture_directory) and os.listdir(f'{picture_directory}/'):
            send_random_space_pictures(picture_directory, flight_number, nasa_api_key, chat_id, token, timer)
        else:
            fill_directory(picture_directory, flight_number, nasa_api_key)
            send_random_space_pictures(picture_directory, flight_number, nasa_api_key, chat_id, token, timer)


if __name__ == '__main__':
    load_dotenv()

    flight_number = os.getenv('flight_number', default=108)
    nasa_api_key = os.environ['NASA_API_KEY']
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    timer = os.getenv('timer', default=14400)
    picture_user_path = os.path.join('user_images', '????????????????.jpg')

    send_pictures_to_telegram(picture_directory='images',
                 flight_number=None,
                 nasa_api_key=nasa_api_key,
                 token=token,
                 chat_id=chat_id,
                 timer=timer,
                 picture_user_path=picture_user_path)
