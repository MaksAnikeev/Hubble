import argparse
import os
import sys

import requests
from dotenv import load_dotenv
from python_save_images import create_pictures


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('nasa_api_key', nargs='?', default='DEMO_KEY')
    return parser

def fetch_nasa_pictures(url, quantity_pictures, picture_path):
    payload = {
        'api_key': namespase.nasa_api_key,
        'count': quantity_pictures
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures_url = []
    for i in range(0, quantity_pictures):
        picture_url = response.json()[i]['url']
        pictures_url.append(picture_url)
    create_pictures(pictures_url, picture_path)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = create_parser()
    namespase = parser.parse_args(sys.argv[1:])

    nasa_url = 'https://api.nasa.gov/planetary/apod'

    fetch_nasa_pictures(url=nasa_url, quantity_pictures=30,
                        picture_path='images/nasa_apod')
