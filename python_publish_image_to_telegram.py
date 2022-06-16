import os
import random
import time

import telegram
from dotenv import load_dotenv

from python_fetch_EPIC_images import fetch_epic_nasa_pictures
from python_fetch_NASA_images import fetch_nasa_pictures
from python_fetch_spacex_images import fetch_spacex_launch


def send_picture(picture_directory, timer=14400):
    fetch_spacex_launch(flight_number=108, picture_path=f'{picture_directory}/spacex')
    fetch_nasa_pictures(quantity_pictures=3, picture_path=f'{picture_directory}/nasa_apod')
    fetch_epic_nasa_pictures(quantity_pictures=2, picture_path=f'{picture_directory}/epic_nasa')

    load_dotenv()
    token = os.environ['TG_TOKEN']
    chat_id = '@AnikeevMaks1'

    bot = telegram.Bot(token=token)
    pictures = os.listdir(f'{picture_directory}/')
    while True:
        random_picture = random.choice(pictures)
        pictures.remove(random_picture)
        bot.send_document(chat_id=chat_id,
                          document=open(f'{picture_directory}/{random_picture}', 'rb'))
        time.sleep(timer)
        if not pictures:
            fetch_spacex_launch(flight_number=108, picture_path=f'{picture_directory}/spacex')
            fetch_nasa_pictures(quantity_pictures=30, picture_path=f'{picture_directory}/nasa_apod')
            fetch_epic_nasa_pictures(quantity_pictures=10, picture_path=f'{picture_directory}/epic_nasa')
            pictures = os.listdir(f'{picture_directory}/')


if __name__ == '__main__':
    send_picture(picture_directory='images')
