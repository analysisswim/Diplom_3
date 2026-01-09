import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import PAGES

class MainPage(BasePage):
    @allure.step("Открываем главную страницу")
    def open_main_page(self, url: str = PAGES["main"]):
        self.open(url)
        self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)

    @allure.step("Переходим в ленту заказов")
    def click_feed_button(self):
        self.click(MainPageLocators.FEED_BUTTON, timeout=15)

    @allure.step("Переходим в конструктор")
    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=15)

    @allure.step("Проверяем, что на главной странице (конструктор)")
    def is_on_main_page(self) -> bool:
        return self.is_visible(MainPageLocators.CONSTRUCTOR_HEADER, timeout=10)

    @allure.step("Кликаем на первый ингредиент")
    def click_first_ingredient(self):
        self.click(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        # подстраховка: ждём появление модалки (это убирает “то открылось, то нет”)
        self.wait_visible(MainPageLocators.MODAL, timeout=10)

    @allure.step("Получаем счётчик первого ингредиента (0 если нет)")
    def get_first_ingredient_counter(self) -> int:
        card = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        counters = card.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if not counters:
            return 0
        txt = counters[0].text.strip()
        return int(txt) if txt.isdigit() else 0

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        source = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        target = self.wait_visible(MainPageLocators.CONSTRUCTOR_DROPZONE, timeout=20)

        self.scroll_into_view(source)
        self.scroll_into_view(target)

        # самый стабильный вариант (особенно для Firefox)
        self.html5_drag_and_drop(source, target)

    @allure.step("Ждём, что счётчик первого ингредиента станет >= {expected_value}")
    def wait_for_counter_value(self, expected_value: int, timeout: int = 15):
        expected_value = int(expected_value)

        def _cond(_driver):
            return self.get_first_ingredient_counter() >= expected_value

        self.wait_until(_cond, timeout=timeout)

    @allure.step("Проверяем, что счётчик ингредиента отображается")
    def is_ingredient_counter_visible(self) -> bool:
        card = self.wait_visible(MainPageLocators.FIRST_INGREDIENT, timeout=20)
        counters = card.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        return bool(counters) and counters[0].is_displayed()

    @allure.step("Закрываем модалку по крестику (если открыта)")
    def close_modal_if_open(self):
        if self.is_visible(MainPageLocators.MODAL, timeout=2):
            self.js_click(MainPageLocators.MODAL_CLOSE_BTN, timeout=5)
            self.wait_invisible(MainPageLocators.MODAL_OVERLAY, timeout=10)
