from selenium.webdriver.common.by import By

class IngredientModalLocators:
    MODAL = (By.CSS_SELECTOR, "section.Modal_modal__P3_V5")
    TITLE = (By.XPATH, "//section[contains(@class,'Modal_modal')]//h2")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS")

    # ✅ Имя ингредиента (самый стабильный вариант)
    INGREDIENT_NAME = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal')]"
        "//div[contains(@class,'Modal_modal__container')]"
        "//p[contains(@class,'text_type_main-medium')][1]"
    )
