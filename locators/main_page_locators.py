from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href,'/') and .//*[contains(.,'Конструктор')]] | //a[contains(.,'Конструктор')]")
    FEED_BUTTON = (By.XPATH, "//a[contains(@href,'/feed') or contains(@href,'feed') or contains(.,'Лента заказов')]")

    CONSTRUCTOR_HEADER = (By.XPATH, "//*[contains(.,'Соберите бургер')]")

    FIRST_INGREDIENT = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='counter_counter__num']")

    # Зона конструктора (ловим любой корневой блок конструктора)
    CONSTRUCTOR_DROPZONE = (By.XPATH, "//*[contains(@class,'BurgerConstructor') and not(contains(@class,'tab_tab'))]")

    # Модалка: ловим любой контейнер модалки, но не overlay
    MODAL = (By.XPATH, "//*[contains(@class,'Modal_modal') and not(contains(@class,'overlay'))]")

    # Крестик: в проекте встречаются разные суффиксы, поэтому просто contains 'close'
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class,'close')]")

    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")


    ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")
    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти в аккаунт')]")

    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    # более надёжно — любые инпуты по type
    EMAIL_INPUT_FALLBACK = (By.XPATH, "//input[@type='text' or @type='email']")
    PASSWORD_INPUT_FALLBACK = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(.,'Войти')]")

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'text_type_digits-large') or contains(@class,'Modal_modal__title') or contains(@class,'text_type_digits')]")
