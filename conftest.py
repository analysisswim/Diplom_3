# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helpers.api_helpers import StellarBurgersAPI
from helpers.user_factory import make_user


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    headless = request.config.getoption("--headless")

    if request.param == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
        drv = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        drv = webdriver.Firefox(options=options)

    drv.implicitly_wait(0)
    yield drv
    try:
        drv.quit()
    except Exception:
        pass


@pytest.fixture()
def authorized():
    """
    Создаёт пользователя через API и отдаёт креды.
    После теста удаляет пользователя.
    """
    api = StellarBurgersAPI()
    user = make_user()

    r = api.register_user(user)
    if r.status_code != 200:
        # если вдруг уже есть, попробуем логин
        r2 = api.login_user(user["email"], user["password"])
        if r2.status_code != 200:
            raise RuntimeError(f"Не удалось создать/залогинить пользователя: {r.text} / {r2.text}")
        token = r2.json().get("accessToken")
    else:
        token = r.json().get("accessToken")

    yield user

    if token:
        try:
            api.delete_user(token)
        except Exception:
            pass
