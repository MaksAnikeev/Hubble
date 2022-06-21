import os
from pathlib import Path
from urllib.parse import urlparse

import requests


def create_directory(picture_path):
    directory = os.path.split(picture_path)
    Path(directory[0]).mkdir(parents=True, exist_ok=True)


def create_picture(picture_url, picture_path, picture_number):
    response_picture = requests.get(picture_url)
    response_picture.raise_for_status()
    with open(f'{picture_path}_{picture_number}{define_ext(picture_url)}', 'wb') as file:
            file.write(response_picture.content)


def define_ext(picture_url):
    parse_picture_url = urlparse(picture_url)
    picture_ext = os.path.splitext(parse_picture_url.path)
    return picture_ext[1]
