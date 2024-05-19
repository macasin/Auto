import pytest
import requests


@pytest.mark.http
def test_first_request():
    r= requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/macasin')
    body = r.json()
    header = r.headers

    assert body["name"]=="Arsen Nebesniuk"
    assert body["type"]=="User"
    assert r.status_code == 200
    assert header["Content-Type"]=="application/json; charset=utf-8"

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404