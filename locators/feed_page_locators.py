from selenium.webdriver.common.by import By

class FeedPageLocators:
    ORDERS_LIST = (By.XPATH, "//*[contains(@class,'OrderFeed_orderList') or contains(@class,'OrderFeed_list')]")
