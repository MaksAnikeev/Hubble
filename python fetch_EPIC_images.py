import argparse
import datetime
import os
import sys

import requests
from dotenv import load_dotenv
from python_save_images import create_pictures


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('nasa_api_key', nargs='?', default='DEMO_KEY')
    return parser

def fetch_epic_nasa_pictures(url, quantity_pictures, picture_path):
    payload = {'api_key': namespase.nasa_api_key}
    response = requests.get(url, params=payload)
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
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser = create_parser()
    namespase = parser.parse_args(sys.argv[1:])

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    fetch_epic_nasa_pictures(url=epic_url, quantity_pictures=10,
                             picture_path='images/epic_nasa')
