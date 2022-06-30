import argparse
import datetime
import os
import sys

import requests
from dotenv import load_dotenv
from pathlib import Path

from save_images import download_picture

def fetch_earth_pictures_from_nasa(pictures_quantity, picture_path, nasa_api_key):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()
    directory = os.path.split(picture_path)
    Path(directory[0]).mkdir(parents=True, exist_ok=True)
    for picture_number, picture in enumerate(response.json()[:pictures_quantity]):
        picture_epic_date = datetime.datetime.fromisoformat(picture['date']).strftime('%Y/%m/%d')
        epic_picture_url = f'https://api.nasa.gov/EPIC/archive/natural/{picture_epic_date}/png' \
                           f'/{picture["image"]}.png'
        download_picture(epic_picture_url, picture_path, picture_number, payload=payload)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('pictures_quantity', nargs='?', default=30)
    parser.add_argument('picture_path', nargs='?', default='images/nasa_apod')
    namespace = parser.parse_args(sys.argv[1:])
    fetch_earth_pictures_from_nasa(pictures_quantity=10, picture_path='images/epic_nasa', nasa_api_key=nasa_api_key)
