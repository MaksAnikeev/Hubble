import argparse
import os
import sys

import requests
from dotenv import load_dotenv
from pathlib import Path

from save_images import download_picture

def fetch_spacex_nasa_pictures(pictures_quantity, picture_path, nasa_api_key):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': pictures_quantity
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    directory = os.path.split(picture_path)
    Path(directory[0]).mkdir(parents=True, exist_ok=True)
    for picture_number, picture in enumerate(response.json()[:pictures_quantity]):
        download_picture(picture['url'], picture_path, picture_number)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser()
    parser.add_argument('pictures_quantity', nargs = '?', default=10)
    parser.add_argument('picture_path', nargs='?', default='images/nasa_apod')
    namespace = parser.parse_args(sys.argv[1:])
    fetch_spacex_nasa_pictures(pictures_quantity=namespace.pictures_quantity,
                        picture_path=namespace.picture_path,
                        nasa_api_key=nasa_api_key)
