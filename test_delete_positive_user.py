import requests
import pytest


def test_delete_positive_user():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "3012199371"
    request['username']= "Ange_tester_7"
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
    urlGet = "https://petstore.swagger.io/v2/user/login?username=Ange_tester_7&password=134567"
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())

    assert responseGet.json()['code'] == 200
    assert responseGet.json()['message'] is not None

    # Удаляем созданного пользователя
    urlDelete = "https://petstore.swagger.io/v2/user/" + str(request['username'])
    print("urlDelete = ", urlDelete)
    responseDelete = requests.delete(urlDelete)
    print("responseDelete = ", responseDelete.json())

    assert responseDelete.json()['code'] == 200
    assert responseDelete.json()['message'] == request['username']

    #Проверяем методом Get/user/username (не из моего варианта курсовой), что пользователь действительно удален
    urlGet_3 = "https://petstore.swagger.io/v2/user/"+ str(responseDelete.json()['message']) ## передаем имя пользователя из ответа в delete
    print("urlGet_3 = ", urlGet_3)
    responseGet_delete_2 = requests.get(urlGet_3)
    print("responseGet_delete_2 = ", responseGet_delete_2.json())
    assert responseGet_delete_2.json()['message'] == 'User not found'