import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.ingredient_modal import IngredientModal
from data.urls import PAGES, URL_PARTS

@allure.feature("Основная функциональность")
class TestMainFunctionality:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open_main_page(PAGES["main"])
        main_page.click_feed_button()
        assert feed_page.is_on_feed_page(), "Не удалось перейти на ленту заказов"

        main_page.click_constructor_button()
        assert URL_PARTS["domain"] in driver.current_url, "URL не содержит домен"
        assert main_page.is_on_main_page(), "Не удалось вернуться на главную страницу"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open_main_page(PAGES["main"])
        main_page.click_feed_button()
        assert feed_page.is_on_feed_page(), "Не удалось перейти на ленту заказов"

    @allure.title("Открытие модального окна при клике на ингредиент")
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        modal = IngredientModal(driver)

        main_page.open_main_page(PAGES["main"])
        main_page.click_first_ingredient()

        assert modal.is_modal_opened(), "Модальное окно не открылось"
        assert modal.get_modal_title() == "Детали ингредиента"

        ingredient_name = modal.get_ingredient_name()
        assert ingredient_name, "Не найдено имя ингредиента в модалке"

    @allure.title("Закрытие модального окна по крестику")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        modal = IngredientModal(driver)

        main_page.open_main_page(PAGES["main"])
        main_page.click_first_ingredient()
        assert modal.is_modal_opened(), "Модальное окно не открылось"

        modal.click_close_button()
        assert modal.is_modal_closed(), "Модальное окно не закрылось"

    @allure.title("Увеличение счётчика при добавлении ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page(PAGES["main"])
        assert main_page.get_first_ingredient_counter() == 0

        main_page.drag_ingredient_to_constructor()
        main_page.wait_for_counter_value(2, timeout=15)

        assert main_page.is_ingredient_counter_visible(), "Счётчик не отображается"
