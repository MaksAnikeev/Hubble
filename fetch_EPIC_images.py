import datetime
import os

import requests
from dotenv import load_dotenv

from save_images import create_pictures


def fetch_epic_nasa_pictures(quantity_pictures, picture_path):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    payload = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()
    pictures_url = []
    for i in range(0, quantity_pictures):
        picture_epic_date = datetime.datetime.fromisoformat(response.json()[i]['date'])
        picture_epic_date = picture_epic_date.date()
        picture_epic_date = picture_epic_date.strftime('%Y/%m/%d')
        picture_epic_name = response.json()[i]['image']
        epic_picture_url = f'https://api.nasa.gov/EPIC/archive/natural/{picture_epic_date}/png' \
                           f'/{picture_epic_name}.png?api_key={payload["api_key"]}'
        pictures_url.append(epic_picture_url)
    create_pictures(pictures_url, picture_path)


if __name__ == '__main__':
    fetch_epic_nasa_pictures(quantity_pictures=10, picture_path='images/epic_nasa')
