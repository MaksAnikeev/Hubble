import os
from pathlib import Path
from urllib.parse import urlparse

import requests


def create_pictures(pictures_url, picture_path):
    pictures_directory = os.path.split(picture_path)
    picture_number = 0
    for picture_url in pictures_url:
        picture_number += 1
        Path(pictures_directory[0]).mkdir(parents=True, exist_ok=True)
        response_picture = requests.get(picture_url)
        response_picture.raise_for_status()
        with open(f'{picture_path}_{picture_number}{define_ext(picture_url)}', 'wb') as file:
            file.write(response_picture.content)


def define_ext(picture_url):
    parse_picture_url = urlparse(picture_url)
    picture_ext = os.path.splitext(parse_picture_url.path)
    return picture_ext[1]
