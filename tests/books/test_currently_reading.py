import pytest
import requests
from expects import expect, equal
from unittest.mock import patch

from app import exceptions
from app.books.currently_reading import get_currently_reading


@patch('requests.get')
def test_get_currently_reading_with_success(mock_get, currently_reading_response):
    mock_get.return_value.content = currently_reading_response
    books = get_currently_reading(1)
    expect(books).to(equal(['História de Quem Foge e de Quem Fica']))


@patch('requests.get',
       side_effect=[requests.exceptions.RequestException()])
def test_get_currently_reading_when_an_error_occurred_in_goodreads_request(
        mock_get, currently_reading_response):
    with pytest.raises(exceptions.GoodreadsException):
        mock_get.return_value.content = currently_reading_response
        get_currently_reading(1)
