# pages/main_page.py
import allure
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import PAGES
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    @allure.step("Открываем главную страницу")
    def open_main_page(self, url=PAGES["main"]):
        self.open(url)
        self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)

    @allure.step("Кликаем 'Лента заказов'")
    def click_feed_button(self):
        self.click(MainPageLocators.FEED_BUTTON, timeout=15)

    @allure.step("Кликаем 'Конструктор'")
    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=15)

    @allure.step("Проверяем что мы на главной (конструктор)")
    def is_on_main_page(self) -> bool:
        return self.is_visible(MainPageLocators.CONSTRUCTOR_HEADER, timeout=10)

    @allure.step("Снимаем оверлей, если он вдруг висит")
    def dismiss_overlay_if_present(self, timeout=3):
        overlays = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
        for ov in overlays:
            try:
                if ov.is_displayed():
                    # safest: JS click
                    self.driver.execute_script("arguments[0].click();", ov)
                    WebDriverWait(self.driver, timeout).until(
                        EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
                    )
                    break
            except Exception:
                pass

    @allure.step("Кликаем по первому ингредиенту")

    def click_first_ingredient(self):
        overlays = self.driver.find_elements(*MainPageLocators.MODAL_OVERLAY)
        for overlay in overlays:
            try:
                if overlay.is_displayed():
                    self.driver.execute_script("arguments[0].click();", overlay)
                    WebDriverWait(self.driver, 5).until(
                        EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
                    )
                    break
            except StaleElementReferenceException:
                pass

        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FIRST_INGREDIENT)
        )
        el.click()

    @allure.step("Получаем значение счётчика у первого ингредиента (int)")
    def get_first_ingredient_counter(self) -> int:
        card = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        counters = card.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if not counters:
            return 0
        txt = counters[0].text.strip()
        return int(txt) if txt.isdigit() else 0

    @allure.step("Получаем текст счётчика у первого ингредиента (str)")
    def get_first_ingredient_counter_text(self) -> str:
        card = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        counters = card.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if not counters:
            return ""
        return counters[0].text.strip()

    @allure.step("Проверяем что счётчик ингредиента виден")
    def is_ingredient_counter_visible(self) -> bool:
        card = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        counters = card.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        return len(counters) > 0 and counters[0].is_displayed()

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        source = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        target = self.wait_visible(MainPageLocators.CONSTRUCTOR_DROPZONE, timeout=20)

        before = self.get_first_ingredient_counter()

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target)

        # 1) пробуем обычный drag
        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except WebDriverException:
            pass

        # ждём чуть-чуть, вдруг сработало
        try:
            WebDriverWait(self.driver, 3).until(lambda d: self.get_first_ingredient_counter() > before)
            return
        except TimeoutException:
            pass

        # 2) фолбэк для Firefox: HTML5 drag через JS
        self.html5_drag_and_drop(source, target)

    @allure.step("Ждём пока счётчик станет >= expected_value")
    def wait_for_counter_value(self, expected_value: int, timeout=15):
        expected_value = int(expected_value)

        def _cond(_driver):
            return self.get_first_ingredient_counter() >= expected_value

        self.wait_until(_cond, timeout=timeout)

    # ---------- ЛОГИН И СОЗДАНИЕ ЗАКАЗА ДЛЯ ЛЕНТЫ ----------

    @allure.step("Логинимся через UI")
    def login(self, email: str, password: str):
        # если мы на главной и есть кнопка "Войти в аккаунт"
        if self.is_visible(MainPageLocators.LOGIN_MAIN_BUTTON, timeout=3):
            self.click(MainPageLocators.LOGIN_MAIN_BUTTON, timeout=10)
        else:
            self.open(PAGES["login"])

        email_el = self.wait_visible(MainPageLocators.EMAIL_INPUT, timeout=15)
        email_el.clear()
        email_el.send_keys(email)

        pass_el = self.wait_visible(MainPageLocators.PASSWORD_INPUT, timeout=15)
        pass_el.clear()
        pass_el.send_keys(password)

        self.click(MainPageLocators.LOGIN_SUBMIT, timeout=10)
        # возвращаемся на главную и ждём конструктор
        self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)

    @allure.step("Создаём заказ через UI и возвращаем номер заказа")
    def create_order_and_get_number(self) -> str:
        self.drag_ingredient_to_constructor()
        self.wait_for_counter_value(2, timeout=15)

        self.click(MainPageLocators.ORDER_BUTTON, timeout=15)

        # ждём модалку заказа
        self.wait_visible(MainPageLocators.ORDER_MODAL, timeout=25)

        # ждём, пока номер станет НЕ плейсхолдером 9999
        def _number_ready(_d):
            txt = self.driver.find_element(*MainPageLocators.ORDER_NUMBER).text.strip()
            return txt.isdigit() and txt != "9999"

        WebDriverWait(self.driver, 25).until(_number_ready)

        order_number = self.driver.find_element(*MainPageLocators.ORDER_NUMBER).text.strip()

        # закрываем модалку
        if self.is_visible(MainPageLocators.ORDER_MODAL_CLOSE, timeout=2):
            self.click(MainPageLocators.ORDER_MODAL_CLOSE, timeout=5)

        return order_number
