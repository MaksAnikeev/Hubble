import requests
from dotenv import load_dotenv

from python_save_images import create_pictures


def fetch_spacex_launch(picture_path, flight_number=108):
    spacexdata_url = 'https://api.spacexdata.com/v3/launches/past'
    load_dotenv()
    payload = {'flight_number': flight_number}
    response_url = requests.get(spacexdata_url, params=payload)
    response_url.raise_for_status()
    pictures_url = response_url.json()[0]['links']['flickr_images']
    create_pictures(pictures_url, picture_path)


if __name__ == '__main__':
    fetch_spacex_launch(picture_path='images/spacex')
