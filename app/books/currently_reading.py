import os
import requests
import xml.etree.ElementTree as ET


def _request(user_id):
    api_key = os.getenv('API_KEY')
    base_url = os.getenv('GOODREADS_URL')
    url = f'{base_url}/review/list/{user_id}.xml?key={api_key}&v=2&shelf=currently-reading'
    header = {'Accept': 'application/xml'}
    return requests.get(url, headers=header)


def get_currently_reading(user_id):
    response = _request(user_id)
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()
    reviews = root.find('reviews')
    books = []
    for r in reviews.findall('review'):
        book = r.find('book').find('title').text
        books.append(book)
    return books
