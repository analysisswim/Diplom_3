import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helpers.api_helpers import StellarBurgersAPI
from helpers.user_factory import make_user
from data.urls import API_ENDPOINTS

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param

@pytest.fixture
def driver(browser):
    drv = None
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1280,900")
        drv = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=900")
        drv = webdriver.Firefox(options=options)

    yield drv
    with allure.step("Закрываем браузер"):
        try:
            drv.quit()
        except Exception:
            pass

@pytest.fixture
def authorized():
    """Создаёт пользователя через API. Возвращает dict с access_token + данными пользователя."""
    api = StellarBurgersAPI()
    user = make_user()
    data = api.register_user(user)
    access_token = data.get("accessToken")
    yield {"user": user, "access_token": access_token}

    if access_token:
        api.delete_user(access_token)

@pytest.fixture
def order_number(authorized):
    """Создаёт заказ через API и возвращает его номер (без ведущих нулей)."""
    api = StellarBurgersAPI()
    access_token = authorized["access_token"]

    ingredients = api.get_ingredients()
    ids = []
    # берём 2 любых ингредиента
    for item in (ingredients.get("data") or [])[:2]:
        if item.get("_id"):
            ids.append(item["_id"])

    order = api.create_order(access_token, ids)
    num = str(order.get("order", {}).get("number", "")).strip()
    return num
