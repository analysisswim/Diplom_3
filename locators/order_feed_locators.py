from selenium.webdriver.common.by import By

class OrderFeedLocators:
    DONE_ALL_TIME = (By.XPATH, "//*[contains(.,'Выполнено за все время')]/following::*[contains(@class,'OrderFeed_number')][1]")
    DONE_TODAY = (By.XPATH, "//*[contains(.,'Выполнено за сегодня')]/following::*[contains(@class,'OrderFeed_number')][1]")

    # Колонки заказов
    IN_WORK_SECTION = (By.XPATH, "//*[contains(.,'В работе')]/ancestor::*[self::section or self::div][1]")
    IN_WORK_NUMBERS = (By.XPATH, "//*[contains(.,'В работе')]/ancestor::*[self::section or self::div][1]//li//*[contains(@class,'OrderFeed_orderNumber') or contains(@class,'text_type_digits-default') or self::p]")
