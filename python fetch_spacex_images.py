import argparse
import sys

import requests
from dotenv import load_dotenv
from python_save_images import create_pictures


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('flight_number', nargs='?', default=108)
    return parser


def fetch_spacex_launch(url, picture_path, flight_number):
    payload = {'flight_number': flight_number}
    response_url = requests.get(url, params=payload)
    response_url.raise_for_status()
    pictures_url = response_url.json()[0]['links']['flickr_images']
    create_pictures(pictures_url, picture_path)

if __name__ == '__main__':
    load_dotenv()
    parser = create_parser()
    namespase = parser.parse_args(sys.argv[1:])
    spacexdata_url = 'https://api.spacexdata.com/v3/launches/past'

    fetch_spacex_launch(url=spacexdata_url, picture_path='images/spacex',
                        flight_number=namespase.flight_number)
