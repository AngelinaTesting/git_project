import requests
import pytest


def test_post_negative_id_non_integer():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "ывпва"
    request['username']= "Ange_tester_4"
    request['firstname'] = "Angelinochka"
    request['lastname']= "Angela"
    request['email'] = "1@mail.ru"
    request['password'] = "134567"
    request['password'] = "11111111111"
    request['userStatus'] = '0'

    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    assert response.json()['code'] == 400 # в Postman ошибка 400, тут 500