import requests
import pytest

# Создание пользователя с пустым телом
def test_post_negative_empty_body():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    assert response.json()['code'] == 400
