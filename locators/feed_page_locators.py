from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Самый стабильный признак страницы
    TITLE = (By.XPATH, "//h1[contains(.,'Лента заказов')]")

    # Если хочешь проверять именно список заказов
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList__list')]")
