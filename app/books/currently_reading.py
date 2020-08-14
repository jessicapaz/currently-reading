import os
import logging
import requests
import xml.etree.ElementTree as ET

from app import exceptions
from app import config

log = logging.getLogger(__name__)


def _request(user_id):
    api = config.GOODREADS
    url = f'{api["base_url"]}/review/list/{user_id}.xml?key={api["api_key"]}&v=2&shelf=currently-reading'
    header = {'Accept': 'application/xml'}
    try:
        return requests.get(url, headers=header, timeout=5)
    except requests.exceptions.RequestException as err:
        log.exception(err)
        raise exceptions.GoodreadsException()


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
