from selenium.webdriver.common.by import By


class IngredientModalLocators:
    MODAL = (By.XPATH, "//*[contains(@class,'Modal_modal__container') or contains(@class,'Modal_modal__contentBox')]")
    TITLE = (By.XPATH, "//*[contains(@class,'Modal_modal__title') and contains(.,'Детали ингредиента')]")

    # НЕ по точному @class=..., а через contains(@class,...)
    NAME = (By.XPATH, "//*[contains(@class,'Modal_modal__container') or contains(@class,'Modal_modal__contentBox')]"
                    "//p[contains(@class,'text_type_main-medium')]")

    IMAGE = (By.XPATH, "//*[contains(@class,'Modal_modal__container') or contains(@class,'Modal_modal__contentBox')]//img")

    # Кликать именно по кнопке, не по svg/внутренностям
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
