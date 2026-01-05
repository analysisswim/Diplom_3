from selenium.webdriver.common.by import By

class MainPageLocators:
    # Верхнее меню (надёжнее через href и contains(. , ...))
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//*[contains(.,'Конструктор')]]")
    FEED_BUTTON = (By.XPATH, "//a[contains(@href,'/feed') or contains(@href,'feed')]")

    # Заголовок/признак конструктора
    CONSTRUCTOR_HEADER = (By.XPATH, "//*[contains(.,'Соберите бургер')]")

    # Первый ингредиент
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@href,'/ingredient/')])[1]")

    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")

    # Счётчик на карточке ингредиента
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class,'counter_counter__num')]")

    # Зона конструктора (привязка к секции с кнопкой "Оформить заказ")
    CONSTRUCTOR_DROPZONE = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor_basket')]"
        "|//div[contains(@class,'BurgerConstructor_basket')]"
        "|//section[contains(@class,'BurgerConstructor_constructor')]"
        "|//div[contains(@class,'BurgerConstructor_constructor')]"
    )

    ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти в аккаунт')]")

    EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(.,'Войти')]")

    ORDER_MODAL = (By.XPATH, "//*[contains(@class,'Modal_modal__container') or contains(@class,'Modal_modal__contentBox')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'text_type_digits-large') or contains(@class,'Modal_modal__title')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
