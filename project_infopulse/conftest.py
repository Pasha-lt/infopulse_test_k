import pytest
import requests


@pytest.fixture()
def base_url():
    yield "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture()
def book(base_url):
    book_data = {"title": "The Jungle Book", "author": "Rudyard Kipling"}
    resp = requests.post(f'{base_url}/books', data=book_data)
    book_body_resp = resp.json()
    yield book_body_resp
    print(f'{base_url}/books/{book_body_resp["id"]}')
    resp = requests.delete(f'{base_url}/books/{book_body_resp["id"]}')
    assert resp.status_code == 204





