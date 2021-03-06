import requests
import pytest


def test_delete_positive():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}

    request['name'] = "Lola"

    request['category'] = {}
    request['category']['name'] = "Angelina"
    request['category']['id'] = "30121993"

    request['photoUrls'] = ['www.photoPlusha', 'www.photoPlusha_1']
    print("request", request)

    response = requests.post(url, json=request)
    print("response", response.json())

    # Проверяем, что вернулся не пустой id
    assert response.json()['id'] is not None
    # Проверяем, что имя в ответе совпадает с имеем в запросе
    assert response.json()['name'] == request['name']

    # Проверяем создание питомца методом get
    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])
    print("urlGet = ", urlGet)
    responseGet = requests.get(urlGet)
    print("responseGet = ", responseGet.json())
    # Проверяем, что id в post и get равны
    assert responseGet.json()['id'] == response.json()['id']
    # Проверяем, что имя в post и get одинаковые
    assert responseGet.json()['name'] == request['name']

    # Удаляем созданного питомца
    urlDelete = "https://petstore.swagger.io/v2/pet/" + str(responseGet.json()['id'])
    print("urlDelete = ", urlDelete)
    responseDelete = requests.delete(urlDelete)
    print("responseDelete = ", responseDelete.json())
    assert responseDelete.json()['code'] == 200

    # Проверяем, что питомец удалился
    urlGet_2 = "https://petstore.swagger.io/v2/pet/" + str(responseDelete.json()['message'])
    print("urlGet_2 = ", urlGet_2)
    responseGet_delete = requests.get(urlGet_2)
    print("responseGet_delete = ", responseGet_delete.json())
    assert responseGet_delete.json()['message'] == 'Pet not found'
