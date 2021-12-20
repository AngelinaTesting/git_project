import requests
import pytest

# Проверяем, что обрезаются цифры после точки
def test_post_negative_id_():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['id'] = "12394948449.4"
    request['username']= "Ange_tester_4"
    request['firstname'] = "Angelinochka"
    request['lastname']= "Angela"
    request['email'] = "2@mail.ru"
    request['password'] = "1237"
    request['phone'] = "11111111111"
    request['userStatus'] = '0'

    print("request", request)

    response = requests.post(url, json=request)
    print("response =", response.json())
    # assert response.json()['id'] == request['id'] в Postman приходит успешный код 200 и обрезаются цифры после .

    assert response.json()['code'] == 500  # в Postman ошибка 400, тут 500
    assert response.json()['message'] == 'something bad happened'