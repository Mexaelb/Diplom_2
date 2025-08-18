import allure
import requests
from test_data import Urls
from helpers import user_data


class TestUserLogin:

    @allure.title("логин под существующим пользователем")
    def test_user_exist_login(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        if response.status_code == 200:
            payload.pop("name")
            response = requests.post(f"{Urls.base_url}{Urls.api_auth_user}", json=payload)
            assert response.status_code == 200
            assert "accessToken" in response.json()

    @allure.title("логин с неверным логином и паролем")
    def test_user_fail_login(self):
        payload = Urls.wrong_data
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.json()["message"]
