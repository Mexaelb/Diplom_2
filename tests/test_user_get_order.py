import allure
import requests
from test_data import Urls
from helpers import user_data


class TestGetOrder:

    @allure.title("Получение заказов конкретного авторизованного пользователя ")
    def test_get_order_user_auth(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        accessToken = response.json()["accessToken"]
        headers = {
            'Authorization': f'{accessToken}'
        }

        response = requests.get(f"{Urls.base_url}{Urls.api_get_order_user}", headers=headers)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Получение заказов не авторизованного пользователя ")
    def test_get_order_user_non_auth(self):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(f"{Urls.base_url}{Urls.api_get_order_user}", headers=headers)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
