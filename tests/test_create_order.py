import allure
import requests
from test_data import Urls
from helpers import user_data


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_auth(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        accessToken = response.json()["accessToken"]
        headers = {
            'Authorization': f'{accessToken}'
        }
        payload = Urls.test_ingredients
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload, headers=headers)
        assert response.status_code == 200
        assert "name" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_non_auth(self):
        payload = Urls.test_ingredients
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload)
        assert response.status_code == 401
        assert "You should be authorised" in response.json()["message"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_non_ingredient(self):
        payload = Urls.non_ingredients
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload)
        assert response.status_code == 400
        assert "Ingredient ids must be provided" in response.json()["message"]

    @allure.title("Создание заказа c неверным хэшом")
    def test_create_order_fake_hash(self):
        payload = Urls.non_hash_ingredient
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload)
        assert response.status_code == 500
