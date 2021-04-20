import pytest
import datetime
from fastapi.testclient import TestClient
from functions import dehash

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

def test_method():
    # testing GET method
    method = '"GET"'
    response = client.get("/method")
    assert response.status_code == 200
    assert response.text == f'{{"method":{method}}}'

    method = '"PUT"'
    response = client.put("/method")
    assert response.status_code == 200
    assert response.text == f'{{"method":{method}}}'

    method = '"OPTIONS"'
    response = client.options("/method")
    assert response.status_code == 200
    assert response.text == f'{{"method":{method}}}'

    method = '"DELETE"'
    response = client.delete("/method")
    assert response.status_code == 200
    assert response.text == f'{{"method":{method}}}'

    method = '"POST"'
    response = client.post("/method")
    assert response.status_code == 201
    assert response.text == f'{{"method":{method}}}'

@pytest.mark.parametrize(
    ["password", "password_hash"],
    [
        ["haslo",
         "013c6889f799cd986a735118e1888727d1435f7f623d05d58c61bf2cd8b49ac90105e5786ceaabd"
         "62bbc27336153d0d316b2d13b36804080c44aa6198c533215"
         ],
        ["haslo",
         "25ca68b6012554ee6c6fa3ef73fe633c990ca165607ad937d7d8beb51da0b85ae2d228f06337ae2584a"
         "8aa80a890892c674da93a3e4475fe3bb0568c37d4b06d"
         ]
    ]
)
def test_check_password(password: str, password_hash: str):
    assert password_hash == dehash(password)

@pytest.mark.parametrize(
    ['password', 'password_hash', 'result'],
    [
        ['abc', dehash('abc'), 204],
        ['haslo', 'zahaszowane_haslo', 401],
        ['', '', 401],
        ['', 'cos', 401],
        ['cos', '', 401]
    ]
)
def test_auth(password: str, password_hash: str, result: int):
    response = client.get(f"/auth?password={password}&password_hash={password_hash}")
    assert response.status_code == result
    if result == 204:
        assert not response.content

