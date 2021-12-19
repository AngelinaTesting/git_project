import requests
import pytest


def test_get_negative_empty_password():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "3012199371"
    request['username']= "Ange_tester"
    request['firstname'] = "Angelinochka"
    request['lastname']= "Angela"
    request['email'] = "1@mail.ru"
    request['password'] = "134567"
    request['password'] = "11111111111"
    request['userStatus'] = '0'

    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    assert response.json()['code'] == 200
    assert response.json()['message'] == request['id']

    # Удаляем user
    urlDelete = "https://petstore.swagger.io/v2/user/" + str(request['username'])
    print("urlDelete = ", urlDelete)
    responseDelete = requests.delete(urlDelete)
    print("responseDelete = ", responseDelete.json())

    assert responseDelete.json()['code'] == 200
    assert responseDelete.json()['message'] == request['username']

    # Проверяем методом get, что удаленный пользователь не может залогиниться
    urlGet = "https://petstore.swagger.io/v2/user/login?username=Ange_tester&password=134567"
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())

    assert responseGet.json()['code'] == 404
