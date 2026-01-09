import allure

from pages.order_feed_page import OrderFeedPage
from helpers.formatters import normalize_order_number

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Счетчик 'Выполнено за все время' увеличивается/не уменьшается")
    def test_done_all_time_increases(self, driver, authorized):
        feed = OrderFeedPage(driver)
        feed.open_feed()
        before = feed.get_done_all_time()
        driver.refresh()
        after = feed.get_done_all_time()
        assert after >= before

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается/не уменьшается")
    def test_done_today_increases(self, driver, authorized):
        feed = OrderFeedPage(driver)
        feed.open_feed()
        before = feed.get_done_today()
        driver.refresh()
        after = feed.get_done_today()
        assert after >= before

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_work(self, driver, authorized, order_number):
        feed = OrderFeedPage(driver)
        feed.open_feed()
        nums = feed.get_in_work_numbers()
        assert normalize_order_number(str(order_number)) in nums
