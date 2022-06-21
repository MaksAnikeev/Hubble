import argparse
import os
import random
import sys
import time

import telegram
from dotenv import load_dotenv

from fetch_EPIC_images import fetch_epic_nasa_pictures
from fetch_NASA_images import fetch_nasa_pictures
from fetch_spacex_images import fetch_spacex_launch


def send_picture(picture_directory, flight_number, nasa_api_key, token, chat_id, timer):
    fetch_spacex_launch(picture_path='images/spacex', flight_number=flight_number)
    fetch_nasa_pictures(quantity_pictures=5, picture_path='images/nasa_apod', nasa_api_key=nasa_api_key)
    fetch_epic_nasa_pictures(quantity_pictures=5, picture_path=f'{picture_directory}/epic_nasa', nasa_api_key=nasa_api_key)

    bot = telegram.Bot(token=token)
    pictures = os.listdir(f'{picture_directory}/')
    while True:
        random_picture = random.choice(pictures)
        pictures.remove(random_picture)
        with open(f'{picture_directory}/{random_picture}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        time.sleep(timer)
        if not pictures:
            fetch_spacex_launch(picture_path='images/spacex', flight_number=flight_number)
            fetch_nasa_pictures(quantity_pictures=5, picture_path='images/nasa_apod', nasa_api_key=nasa_api_key)
            fetch_epic_nasa_pictures(quantity_pictures=5, picture_path=f'{picture_directory}/epic_nasa',
                                     nasa_api_key=nasa_api_key)
            pictures = os.listdir(f'{picture_directory}/')


if __name__ == '__main__':
    load_dotenv()
    flight_number = os.getenv('flight_number', default=108)
    nasa_api_key = os.environ['NASA_API_KEY']
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    timer = os.getenv('timer', default=14400)
    send_picture(picture_directory='images', flight_number = flight_number, nasa_api_key = nasa_api_key,
                 token = token, chat_id=chat_id, timer=5)

