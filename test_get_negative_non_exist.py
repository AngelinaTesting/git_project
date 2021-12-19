import requests
import pytest

# Вход в систему несуществующим пользователем
def test_get_negative_non_exist():
    urlGet = "https://petstore.swagger.io/v2/user/login?username=Ange_tester_3&password=111"
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())

    assert responseGet.json()['code'] == 404
