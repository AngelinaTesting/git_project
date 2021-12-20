import requests
import pytest

# Удаление несуществующего пользователя
def test_delete_negative_user():
    urlDelete = "https://petstore.swagger.io/v2/user/Ange_tester_7"
    print("urlDelete = ", urlDelete)
    responseDelete = requests.delete(urlDelete)
    print("responseDelete = ", responseDelete.json())
    assert responseDelete.json()['code'] == 404
