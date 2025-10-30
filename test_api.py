import requests
import pytest

BASE_URL = "https://reqres.in/api/users"
HEADERS = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}

def test_get_user():
    response = requests.get(f"{BASE_URL}/2", headers=HEADERS)
    assert response.status_code == 200

    json_data = response.json()
    assert "data" in json_data, "В ответе нет ключа 'data'"
    user = json_data["data"]

    for field in ["id", "email", "first_name", "last_name", "avatar"]:
        assert field in user, f"Нет поля '{field}'"
        assert user[field] is not None and str(user[field]).strip() != "", f"Поле '{field}' пустое"

def test_create_user():
    payload = {"name": "Darya Pozdnyakova", "job": "Developer"}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 201

    json_data = response.json()
    for field in ["name", "job", "id", "createdAt"]:
        assert field in json_data, f"Нет поля '{field}'"
        assert json_data[field] is not None and str(json_data[field]).strip() != "", f"Поле '{field}' пустое"


def test_update_user():
    payload = {"name": "Darya Pozdnyakova", "job": "Manager"}
    response = requests.put(f"{BASE_URL}/2", json=payload, headers=HEADERS)
    assert response.status_code == 200

    json_data = response.json()
    for field in ["name", "job", "updatedAt"]:
        assert field in json_data, f"Нет поля '{field}'"
        assert json_data[field] is not None and str(json_data[field]).strip() != "", f"Поле '{field}' пустое"
