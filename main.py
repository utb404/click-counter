import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    response = requests.get(url)
    response.raise_for_status()
    bit_link = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': token}
    response = requests.post(bit_link, headers=headers, 
                             json={'long_url': url})
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    url = urlparse(bitlink)
    url = f'{url.netloc}{url.path}'
    bit_link = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
    headers = {'Authorization': token}
    payload = {'unit': 'day', 'units': '-1'}
    response = requests.get(bit_link, headers=headers,
                            params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, bitlink):
    url = urlparse(bitlink)
    url = f'{url.netloc}{url.path}'
    bit_link = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {'Authorization': token}
    response = requests.get(bit_link, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Программа принимает ссылки, укорачивает их и считает клики'
    )
    parser.add_argument('url', help='Ссылка')
    args = parser.parse_args()
    url = args.url
    token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(token, url):
            clicks_count = count_clicks(token, url)
            print(f'Кликов {clicks_count}')
        else:
            bitlink = shorten_link(token, url)
            print(f'Битлинк {bitlink}')
    except requests.exceptions.HTTPError:
        print('Введена несуществующая страница')
