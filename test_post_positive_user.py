import requests
import pytest

# Создание пользователя с валидными значениями
def test_post_positive_user():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "12394948449"
    request['username']= "Ange_tester_4"
    request['firstname'] = "Angelinochka"
    request['lastname']= "Angela"
    request['email'] = "2@mail.ru"
    request['password'] = "134567"
    request['password'] = "11111111111"
    request['userStatus'] = '0'

    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    assert response.json()['code'] == 200
    assert response.json()['message'] == request['id']

    # Проверяем методом get, что созданный пользователь может залогиниться
    urlGet = "https://petstore.swagger.io/v2/user/login?username=Ange_tester_4&password=134567"
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())

    assert responseGet.json()['code'] == 200
    assert responseGet.json()['message'] is not None

    # Проверяем методом Get/user/username (не из моего варианта курсовой), что пользователь создался
    urlGet_2 = "https://petstore.swagger.io/v2/user/" + str(request['username'])  # передаем имя пользователя из POST
    print("urlGet_3 = ", urlGet_2)
    responseGet_2 = requests.get(urlGet_2)
    print("responseGet_2 = ", responseGet_2.json())

    assert str(responseGet_2.json()['id']) == response.json()['message']