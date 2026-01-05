from selenium.webdriver.common.by import By


class OrderFeedLocators:
    DONE_ALL_TIME = (By.XPATH, "//p[contains(.,'Выполнено за все время')]/following-sibling::p")
    DONE_TODAY = (By.XPATH, "//p[contains(.,'Выполнено за сегодня')]/following-sibling::p")

    IN_WORK_SECTION = (By.XPATH, "//p[contains(.,'В работе')]/following::ul[1]")
    IN_WORK_NUMBERS = (By.XPATH, "//p[contains(.,'В работе')]/following::ul[1]//li")
