import datetime
import os

import requests
from dotenv import load_dotenv

from save_images import create_picture
from save_images import create_directory

def fetch_epic_nasa_pictures(quantity_pictures, picture_path, nasa_api_key):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()
    create_directory(picture_path)
    picture_number = 0
    for picture in response.json()[:quantity_pictures]:
        picture_epic_date = datetime.datetime.fromisoformat(picture['date']).strftime('%Y/%m/%d')
        epic_picture_url = f'https://api.nasa.gov/EPIC/archive/natural/{picture_epic_date}/png' \
                           f'/{picture["image"]}.png?api_key={payload["api_key"]}'
        picture_number += 1
        create_picture(epic_picture_url, picture_path, picture_number)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_epic_nasa_pictures(quantity_pictures=10, picture_path='images/epic_nasa', nasa_api_key=nasa_api_key)
