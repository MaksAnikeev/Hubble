import requests
from dotenv import load_dotenv

from save_images import create_picture
from save_images import create_directory


def fetch_spacex_launch(picture_path, flight_number=108):
    spacexdata_url = 'https://api.spacexdata.com/v3/launches/past'
    load_dotenv()
    payload = {'flight_number': flight_number}
    response_url = requests.get(spacexdata_url, params=payload)
    response_url.raise_for_status()
    pictures_url = response_url.json()[0]['links']['flickr_images']
    create_directory(picture_path)
    picture_number = 0
    for picture_url in pictures_url:
        picture_number +=1
        create_picture(picture_url, picture_path, picture_number)


if __name__ == '__main__':
    fetch_spacex_launch(picture_path='images/spacex')
