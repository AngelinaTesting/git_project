import requests
import pytest


def test_get_positive():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "30121993100"
    request['username']= "Ange_tester_1"
    request['firstname'] = "Angelinochka"
    request['lastname']= "Angela"
    request['email'] = "1@mail.ru"
    request['password'] = "134567"
    request['phone'] = "11111111111"
    request['userStatus'] = '0'

    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    assert response.json()['code'] == 200
    assert response.json()['message'] == request['id']

    # Проверяем методом get, что созданный пользователь может залогиниться
    urlGet = "https://petstore.swagger.io/v2/user/login?username=Ange_tester_1&password=134567"
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())

    assert responseGet.json()['code'] == 200
    assert responseGet.json()['message'] is not None