class Urls:
    base_url = "https://stellarburgers.nomoreparties.site"

    api_get_ingredient = "/api/ingredients"  # Получение данных об ингредиентах
    api_make_order = "/api/orders"  # Создание заказа
    api_recovery_pass = "/api/password-reset"  # Восстановление и сброс пароля
    api_create_user = "/api/auth/register"  # Создание пользователя
    api_auth_user = "/api/auth/login"  # эндпоинт для авторизации
    api_register_user = "/api/auth/register"  # эндпоинт для регистрации пользователя
    api_logout_user = "/api/auth/logout"  # эндпоинт для выхода из системы
    api_refresh_token = "/api/auth/token"  # эндпоинт обновления токена
    api_data_user = "/api/auth/user"  # эндпоинт получения данных о пользователе
    api_update_data_user = "/api/auth/user"  # эндпоинт обновления данных о пользователе
    api_delete_user = "/api/auth/user"  # Удаление пользователя
    api_get_all_order = "/api/orders/all"  # Получить все заказы
    api_get_order_user = "/api/orders"  # Получить заказы конкретного пользователя

    wrong_data = {
        "email": "213@test.ru",
        "password": "123321"
    }

    test_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6c"]
    }

    non_ingredients = {
        "ingredients": []
    }

    non_hash_ingredient = {
        "ingredients": ["non_id"]
    }
