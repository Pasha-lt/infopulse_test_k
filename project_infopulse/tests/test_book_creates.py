import requests


def test_create_book(base_url, book):
    # Создание книги
    payload = {'title': 'Son of the Wolf', 'author': 'Jack London'}
    resp = requests.post(f'{base_url}/books', data=payload)
    assert 'id' in resp.json()
    for key in payload:
        assert payload[key] == resp.json()[key]


def test_read_book(base_url, book):
    # Проверяем книгу
    # print(f'{base_url}/books/{book["id"]}')
    assert requests.get(f'{base_url}/books/{book["id"]}').status_code == 200


def test_edite_book(base_url, book):
    # меняем книгу
    new_payload = {'title': 'Son of the Wolf', 'author': 'Jack London'}
    old_book = requests.get(f'{base_url}/books/{book["id"]}')
    change_r = requests.put(f'{base_url}/books/{book["id"]}', data=new_payload)
    for key in new_payload:
        assert old_book.json()[key] != new_payload[key]

    for key in new_payload:
        assert new_payload[key] == change_r.json()[key]


def test_delete_book(base_url, book):
    # удаление книги
    payload = {'title': 'Son', 'author': 'Jack'}
    resp = requests.post(f'{base_url}/books', data=payload)
    delete_b = requests.delete(f'{base_url}/books/{resp.json()["id"]}')
    assert delete_b.status_code == 204
