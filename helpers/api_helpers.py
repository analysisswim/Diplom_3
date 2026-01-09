import allure
import requests

from data.urls import API_ENDPOINTS

class StellarBurgersAPI:
    def __init__(self):
        self.session = requests.Session()

    @allure.step("API: регистрация пользователя")
    def register_user(self, user_data: dict) -> dict:
        resp = self.session.post(API_ENDPOINTS["register"], json=user_data, timeout=20)
        resp.raise_for_status()
        return resp.json()

    @allure.step("API: логин пользователя")
    def login_user(self, email: str, password: str) -> dict:
        resp = self.session.post(
            API_ENDPOINTS["login"],
            json={"email": email, "password": password},
            timeout=20,
        )
        resp.raise_for_status()
        return resp.json()

    @allure.step("API: удалить пользователя")
    def delete_user(self, access_token: str) -> None:
        headers = {"Authorization": access_token}
        resp = self.session.delete(API_ENDPOINTS["user"], headers=headers, timeout=20)
        # при повторной очистке может быть 202/401 — не падаем
        if resp.status_code not in (200, 202, 204, 401, 403):
            resp.raise_for_status()

    @allure.step("API: получить список ингредиентов")
    def get_ingredients(self) -> dict:
        resp = self.session.get(API_ENDPOINTS["ingredients"], timeout=20)
        resp.raise_for_status()
        return resp.json()

    @allure.step("API: создать заказ")
    def create_order(self, access_token: str, ingredient_ids: list) -> dict:
        headers = {"Authorization": access_token}
        resp = self.session.post(
            API_ENDPOINTS["orders"],
            headers=headers,
            json={"ingredients": ingredient_ids},
            timeout=20,
        )
        resp.raise_for_status()
        return resp.json()
