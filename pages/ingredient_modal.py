import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators

class IngredientModal(BasePage):

    @allure.step("Проверяем, что модальное окно ингредиента открыто")
    def is_modal_opened(self) -> bool:
        return self.is_visible(IngredientModalLocators.MODAL, timeout=10)

    @allure.step("Получаем заголовок модалки")
    def get_modal_title(self) -> str:
        el = self.wait_visible(IngredientModalLocators.TITLE, timeout=10)
        return el.text.strip()

    @allure.step("Закрываем модалку по крестику")
    def click_close_button(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON, timeout=10)

    @allure.step("Ждём, что модалка закрылась")
    def wait_modal_closed(self):
        self.wait_invisible(IngredientModalLocators.MODAL, timeout=10)

    @allure.step("Получаем имя ингредиента из модалки")
    def get_ingredient_name(self) -> str:
        el = self.wait_visible(IngredientModalLocators.INGREDIENT_NAME, timeout=10)
        return el.text.strip()

    @allure.step("Проверяем, что модалка закрыта")
    def is_modal_closed(self) -> bool:
        # True если модалка исчезла/не видна
        return self.wait_invisible(IngredientModalLocators.MODAL, timeout=10)
