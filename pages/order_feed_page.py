# pages/order_feed_page.py
import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from data.urls import PAGES


class OrderFeedPage(BasePage):
    @allure.step("Открываем страницу /feed")
    def open_feed(self):
        self.open(PAGES["feed"])
        self.wait_visible(OrderFeedLocators.DONE_ALL_TIME, timeout=20)

    @allure.step("Читаем 'Выполнено за все время'")
    def get_done_all_time(self) -> int:
        el = self.wait_visible(OrderFeedLocators.DONE_ALL_TIME, timeout=20)
        txt = el.text.strip()
        return int(txt) if txt.isdigit() else 0

    @allure.step("Читаем 'Выполнено за сегодня'")
    def get_done_today(self) -> int:
        el = self.wait_visible(OrderFeedLocators.DONE_TODAY, timeout=20)
        txt = el.text.strip()
        return int(txt) if txt.isdigit() else 0

    @allure.step("Проверяем что номер заказа появился в 'В работе'")
    def is_order_in_work(self, order_number: str, timeout: int = 30) -> bool:
        self.wait_visible(OrderFeedLocators.IN_WORK_SECTION, timeout=20)
        target = self._norm(order_number)

        def _cond(_d):
            items = self.driver.find_elements(*OrderFeedLocators.IN_WORK_NUMBERS)
            nums = [self._norm(i.text) for i in items if i.text.strip()]
            return target in nums

        try:
            WebDriverWait(self.driver, timeout, poll_frequency=1).until(_cond)
            return True
        except TimeoutException:
            return False

    @staticmethod
    @allure.step("Ленте номера могут быть с ведущими нулями.")
    def _norm(num: str) -> str:
        num = num.strip().lstrip("#")
        return str(int(num)) if num.isdigit() else num

