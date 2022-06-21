import os

import requests
from dotenv import load_dotenv

from save_images import create_picture
from save_images import create_directory

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
    create_directory(picture_path)
    picture_number = 0
    for i in range(0, quantity_pictures):
        picture_url = response.json()[i]['url']
        picture_number += 1
        create_picture(picture_url, picture_path, picture_number)


if __name__ == '__main__':
    fetch_nasa_pictures(quantity_pictures=30, picture_path='images/nasa_apod')
