import allure

from pages.base_page import BasePage
from pages.feed_page import FeedPage
from locators.order_feed_locators import OrderFeedLocators
from helpers.formatters import normalize_order_number

class OrderFeedPage(FeedPage):
    @allure.step("Считываем 'Выполнено за все время'")
    def get_done_all_time(self) -> int:
        el = self.wait_visible(OrderFeedLocators.DONE_ALL_TIME, timeout=20)
        txt = el.text.strip()
        return int(txt) if txt.isdigit() else 0

    @allure.step("Считываем 'Выполнено за сегодня'")
    def get_done_today(self) -> int:
        el = self.wait_visible(OrderFeedLocators.DONE_TODAY, timeout=20)
        txt = el.text.strip()
        return int(txt) if txt.isdigit() else 0

    @allure.step("Получаем список номеров в колонке 'В работе'")
    def get_in_work_numbers(self) -> list[str]:
        self.wait_visible(OrderFeedLocators.IN_WORK_SECTION, timeout=20)
        els = self.find_elements(OrderFeedLocators.IN_WORK_NUMBERS)
        nums = []
        for el in els:
            t = el.text.strip()
            if t:
                nums.append(normalize_order_number(t))
        return nums
