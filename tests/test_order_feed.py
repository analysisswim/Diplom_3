# tests/test_order_feed.py
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Счетчик 'Выполнено за все время' увеличивается")
    def test_done_all_time_increases(self, driver, authorized):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        # логин
        main.open_main_page()
        main.login(authorized["email"], authorized["password"])

        # до
        feed.open_feed()
        before = feed.get_done_all_time()

        # создаём заказ
        main.open_main_page()
        _order_number = main.create_order_and_get_number()

        # после (берём снова)
        feed.open_feed()
        after = feed.get_done_all_time()

        assert after >= before, f"Счётчик 'за всё время' уменьшился: было {before}, стало {after}"

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается")
    def test_done_today_increases(self, driver, authorized):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        main.open_main_page()
        main.login(authorized["email"], authorized["password"])

        feed.open_feed()
        before = feed.get_done_today()

        main.open_main_page()
        _order_number = main.create_order_and_get_number()

        feed.open_feed()
        after = feed.get_done_today()

        assert after >= before, f"Счётчик 'за сегодня' уменьшился: было {before}, стало {after}"

    @allure.title("После оформления заказа номер появляется в разделе 'В работе'")
    def test_order_appears_in_work(self, driver, authorized):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        main.open_main_page()
        main.login(authorized["email"], authorized["password"])

        main.open_main_page()
        order_number = main.create_order_and_get_number()
        assert order_number, "Не получили номер заказа"

        feed.open_feed()
        assert feed.is_order_in_work(order_number), f"Заказ {order_number} не найден в 'В работе'"
