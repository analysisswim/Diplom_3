import requests
from data.urls import API_ENDPOINTS


class StellarBurgersAPI:
    def __init__(self):
        self.session = requests.Session()

    def register_user(self, user_data: dict):
        return self.session.post(API_ENDPOINTS["register"], json=user_data, timeout=15)

    def login_user(self, email: str, password: str):
        payload = {"email": email, "password": password}
        return self.session.post(API_ENDPOINTS["login"], json=payload, timeout=15)

    def delete_user(self, access_token: str):
        headers = {"Authorization": access_token}
        return self.session.delete(API_ENDPOINTS["user"], headers=headers, timeout=15)

    def create_order(self, access_token: str, ingredients: list):
        headers = {"Authorization": access_token}
        payload = {"ingredients": ingredients}
        return self.session.post(API_ENDPOINTS["orders"], headers=headers, json=payload, timeout=15)

    def get_ingredients(self):
        return self.session.get(API_ENDPOINTS["ingredients"], timeout=15)
