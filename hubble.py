import argparse
import datetime
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('flight_number', nargs='?', default=108)
    parser.add_argument('nasa_api_key', nargs='?', default='DEMO_KEY')
    return parser


def fetch_spacex_launch(url, picture_name, flight_number):
    payload = {'flight_number': flight_number}
    response_url = requests.get(url, params=payload)
    response_url.raise_for_status()
    pictures_url = response_url.json()[0]['links']['flickr_images']
    create_pictures(pictures_url, picture_name)


def create_pictures(pictures_url, picture_name):
    pictures_directory = os.path.split(picture_name)
    picture_number = 0
    for picture_url in pictures_url:
        picture_number += 1
        Path(pictures_directory[0]).mkdir(parents=True, exist_ok=True)
        response_picture = requests.get(picture_url)
        response_picture.raise_for_status()
        with open(f'{picture_name}_{picture_number}{define_ext(picture_url)}', 'wb') as file:
            file.write(response_picture.content)


def define_ext(picture_url):
    parse_picture_url = urlparse(picture_url)
    picture_ext = os.path.splitext(parse_picture_url.path)
    return picture_ext[1]


def fetch_nasa_pictures(url, quantity_pictures, picture_name):
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
    create_pictures(pictures_url, picture_name)


def fetch_epic_nasa_pictures(url, quantity_pictures, picture_name):
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
    create_pictures(pictures_url, picture_name)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = create_parser()
    namespase = parser.parse_args(sys.argv[1:])

    spacexdata_url = 'https://api.spacexdata.com/v3/launches/past'
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    fetch_spacex_launch(url=spacexdata_url, picture_name='images/spacex',
                        flight_number=namespase.flight_number)
    fetch_nasa_pictures(url=nasa_url, quantity_pictures=30,
                        picture_name='images/nasa_apod')
    fetch_epic_nasa_pictures(url=epic_url, quantity_pictures=10,
                             picture_name='images/epic_nasa')
