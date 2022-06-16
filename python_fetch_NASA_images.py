import os

import requests
from dotenv import load_dotenv

from python_save_images import create_pictures


def fetch_nasa_pictures(quantity_pictures, picture_path):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    payload = {
        'api_key': nasa_api_key,
        'count': quantity_pictures
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    pictures_url = []
    for i in range(0, quantity_pictures):
        picture_url = response.json()[i]['url']
        pictures_url.append(picture_url)
    create_pictures(pictures_url, picture_path)


if __name__ == '__main__':
    fetch_nasa_pictures(quantity_pictures=30, picture_path='images/nasa_apod')
