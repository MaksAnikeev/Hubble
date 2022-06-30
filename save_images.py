import os
from urllib.parse import urlparse

import requests


def download_picture(picture_url, picture_path, picture_number, payload=None):
    picture_response = requests.get(picture_url, params=payload)
    picture_response.raise_for_status()
    with open(f'{picture_path}_{picture_number}{define_ext(picture_url)}', 'wb') as file:
            file.write(picture_response.content)


def define_ext(picture_url):
    parse_picture_url = urlparse(picture_url)
    picture_path, picture_ext = os.path.splitext(parse_picture_url.path)
    return picture_ext
