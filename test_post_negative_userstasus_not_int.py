import requests
import pytest

def test_post_negative_userStatus_not_int():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "12394948449"
    request['username']= "Ange_tester_4"
    request['firstname'] = "Angelinochka"
    request['lastname']= "Angela"
    request['email'] = "2@mail.ru"
    request['password'] = "1237"
    request['phone'] = "11111111111"
    request['userStatus'] = 'fdgd'

    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    # assert response.json()['code'] == 400   в Postman 400 ошибка
    assert response.json()['code'] == 500
    assert response.json()['message'] == 'something bad happened'
