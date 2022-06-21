import os

import requests
from dotenv import load_dotenv

from save_images import create_picture
from save_images import create_directory

def fetch_nasa_pictures(quantity_pictures, picture_path, nasa_api_key):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': quantity_pictures
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    create_directory(picture_path)
    picture_number = 0
    for picture in response.json()[:quantity_pictures]:
        picture_number += 1
        create_picture(picture['url'], picture_path, picture_number)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_nasa_pictures(quantity_pictures=30, picture_path='images/nasa_apod', nasa_api_key=nasa_api_key)
