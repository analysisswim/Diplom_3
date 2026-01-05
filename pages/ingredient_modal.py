# pages/ingredient_modal.py
import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModal(BasePage):
    @allure.step("Проверяем, что модальное окно открыто")
    def is_modal_opened(self) -> bool:
        return self.is_visible(IngredientModalLocators.MODAL, timeout=10)

    @allure.step("Получаем заголовок модалки")
    def get_modal_title(self) -> str:
        self.wait_visible(IngredientModalLocators.TITLE, timeout=10)
        return self.driver.find_element(*IngredientModalLocators.TITLE).text.strip()

    @allure.step("Получаем имя ингредиента в модалке")
    def get_ingredient_name(self) -> str:
        self.wait_visible(IngredientModalLocators.MODAL, timeout=10)
        el = self.wait_visible(IngredientModalLocators.NAME, timeout=10)
        return el.text.strip()

    @allure.step("Проверяем, что картинка ингредиента отображается")
    def is_ingredient_image_visible(self) -> bool:
        return self.is_visible(IngredientModalLocators.IMAGE, timeout=10)

    @allure.step("Кликаем крестик закрытия модалки")
    def click_close_button(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON, timeout=10)

    @allure.step("Проверяем, что модалка закрылась")
    def is_modal_closed(self) -> bool:
        try:
            self.wait_invisible(IngredientModalLocators.MODAL, timeout=10)
            return True
        except Exception:
            return False
