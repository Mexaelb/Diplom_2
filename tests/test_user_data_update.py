import allure
import requests
from test_data import Urls
from helpers import user_data, random_name, random_email, random_password


class TestUserDataUpdate:

    @allure.title("Изменение имени пользователя с авторизацией")
    def test_user_data_name_update_auth(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        accessToken = response.json()["accessToken"]
        headers = {
            'Authorization': f'{accessToken}'
        }
        new_name = random_name()
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={"name": new_name}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение почты пользователя с авторизацией")
    def test_user_data_email_update_auth(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        accessToken = response.json()["accessToken"]
        headers = {
            'Authorization': f'{accessToken}'
        }
        new_email = random_email()
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={"email": new_email}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == new_email

    @allure.title("Изменение пароля пользователя с авторизацией")
    def test_user_data_password_update_auth(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        accessToken = response.json()["accessToken"]
        headers = {
            'Authorization': f'{accessToken}'
        }
        new_password = random_password()
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={"password": new_password}, headers=headers)
        assert response.status_code == 200

    @allure.title("Изменение имени пользователя без авторизацией")
    def test_user_data_name_update_non_auth(self):
        headers = {
            "Content-Type": "application/json"
        }
        new_name = random_name()
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={"name": new_name}, headers=headers)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
