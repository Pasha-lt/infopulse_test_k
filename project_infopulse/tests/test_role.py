import requests


def test_create_role(book, base_url):
    role_data = {
        "name": "Polonius",
        "type": "Secondary",
        "level": 2,
        "book": book["id"]
    }
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 201
    resp_body = resp.json()
    assert "id" in resp_body
    for key in role_data:
        assert resp_body[key] == role_data[key]


def test_read_role(role, base_url):
    """Метод проверяет считываения обьекта"""
    resp = requests.get(f'{base_url}roles/{role["id"]}')
    assert resp.status_code == 200
    resp = resp.json()
    for key in resp:
        assert resp[key] == role[key]


def test_edite_role(role, base_url, book):
    """Метод проверяет изминения обьекта"""
    new_payload = {'name': 'pre Lord', 'type': 'middle', 'level': 500, 'book': book['id']}
    resp = requests.put(f'{base_url}/roles/{role["id"]}', data=new_payload)
    assert resp.status_code == 200
    resp = resp.json()
    for key in new_payload:
        assert new_payload[key] == resp[key]


def test_delete_role(base_url, book):
    new_payload = {'name': 'pre Lord', 'type': 'middle', 'level': 500, 'book': book['id']}
    resp = requests.post(f'{base_url}/roles', data=new_payload)
    delete_r = requests.delete(f'{base_url}/roles/{resp.json()["id"]}')
    assert delete_r.status_code == 204
