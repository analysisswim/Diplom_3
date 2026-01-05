import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from data.urls import PAGES


class FeedPage(BasePage):
    @allure.step("Открываем страницу ленты заказов")
    def open_feed(self):
        self.open(PAGES["feed"])
        self.wait_visible(FeedPageLocators.TITLE, timeout=20)

    @allure.step("Проверяем что мы на странице ленты заказов")
    def is_on_feed_page(self) -> bool:
        return self.is_visible(FeedPageLocators.TITLE, timeout=10)
