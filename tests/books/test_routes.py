from expects import expect, equal
from unittest.mock import patch
from fastapi.testclient import TestClient

from app import exceptions
from app.main import build_api

client = TestClient(build_api())


@patch('app.books.routes.get_currently_reading')
def test_currently_reading_with_success(
        mock_currently_reading, currently_reading_list):
    mock_currently_reading.return_value = currently_reading_list
    response = client.get(
        url=f'/users/<id>/books'
    )
    expect(response.status_code).to(equal(200))
    expect(
        response.json()
    ).to(equal(['Book 1', 'Book 2']))


@patch('app.books.routes.get_currently_reading',
       side_effect=[exceptions.GoodreadsException()])
def test_currently_reading_when_an_error_occurred_in_goodreads_request(
        mock_currently_reading):
    response = client.get(
        url=f'/users/<id>/books'
    )
    expect(response.status_code).to(equal(502))
