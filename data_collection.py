import os
import requests
import cv2
from bs4 import BeautifulSoup


def download_file(url, directory, filename):
    response = requests.get(url)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'wb') as f:
        f.write(response.content)


def download_image(url, directory, filename):
    download_file(url, directory, filename)


def download_video(url, directory, filename):
    download_file(url, directory, filename)


def scrape_media(url, directory, media_type):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if media_type == 'image':
        media_tags = soup.find_all('img')
        download_function = download_image
    elif media_type == 'video':
        media_tags = soup.find_all('video')
        download_function = download_video
    else:
        raise ValueError('Invalid media type. Only "image" and "video" are supported.')

    for i, media in enumerate(media_tags):
        media_url = media['src']
        filename = f'{media_type}_{i}.{media_url.split(".")[-1]}'
        download_function(media_url, directory, filename)

