import os

import requests
from pathlib import Path

from save_images import download_picture


def fetch_spacex_launch(picture_path,
                        flight_number = None):
    if flight_number:
        spacexdata_url = 'https://api.spacexdata.com/v3/launches'
        payload = {'flight_number': flight_number}
        response_url = requests.get(spacexdata_url, params=payload)
        response_url.raise_for_status()
        pictures_url = response_url.json()[0]['links']['flickr_images']
    else:
        spacexdata_url = 'https://api.spacexdata.com/v4/launches'
        response_url = requests.get(spacexdata_url)
        response_url.raise_for_status()
        for response in response_url.json()[::-1]:
            if response['links']['flickr']['original']:
                pictures_url = response['links']['flickr']['original']
                break
    directory = os.path.split(picture_path)
    Path(directory[0]).mkdir(parents=True, exist_ok=True)
    for picture_number, picture_url in enumerate(pictures_url):
        download_picture(picture_url, picture_path, picture_number)


if __name__ == '__main__':
    flight_number = os.getenv('flight_number', default=108)
    fetch_spacex_launch(picture_path='images/spacex',
                        flight_number=flight_number)
