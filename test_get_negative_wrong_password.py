import requests
import pytest

# Создание пользователя с валидными значениями
def test_get_negative_wrong_password():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "30121993100"
    request['username']= "Ange_tester_1"
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

    # Проверяем методом get, что пользователь не может залогиниться с некорректным паролем
    urlGet = "https://petstore.swagger.io/v2/user/login?username=Ange_tester_1&password=111"
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())

    assert responseGet.json()['code'] == 404