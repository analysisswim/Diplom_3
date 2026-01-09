import allure

from typing import Optional, Callable, Any

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Открываем страницу: {url}")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Ожидаем, что элемент видим: {locator}")
    def wait_visible(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидаем, что элемент кликабелен: {locator}")
    def wait_clickable(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator, timeout: Optional[int] = None):
        el = self.wait_clickable(locator, timeout=timeout)
        el.click()
        return el

    @allure.step("JS-клик по элементу: {locator}")
    def js_click(self, locator, timeout: Optional[int] = None):
        el = self.wait_visible(locator, timeout=timeout)
        self.driver.execute_script("arguments[0].click();", el)
        return el

    @allure.step("Ищем все элементы: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Проверяем, что элемент видим: {locator}")
    def is_visible(self, locator, timeout: Optional[int] = None) -> bool:
        try:
            self.wait_visible(locator, timeout=timeout)
            return True
        except Exception:
            return False

    @allure.step("Ожидаем условие")
    def wait_until(self, condition: Callable[[Any], Any], timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(condition)

    @allure.step("Ожидаем, что элемент исчез: {locator}")
    def wait_invisible(self, locator, timeout: Optional[int] = None) -> bool:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ждём, что URL содержит: {part}")
    def wait_for_url_contains(self, part: str, timeout: Optional[int] = None) -> bool:
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(EC.url_contains(part))
            return True
        except Exception:
            return False

    @allure.step("Скроллим к элементу")
    def scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )

    @allure.step("Drag&Drop элемента в цель")
    def drag_and_drop(self, source, target):
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).pause(0.2).release().perform()

    @allure.step("HTML5 drag&drop")
    def html5_drag_and_drop(self, source, target):
        js = """
        const source = arguments[0];
        const target = arguments[1];

        let dataTransfer;
        try {
          dataTransfer = new DataTransfer();
        } catch (e) {
          dataTransfer = new ClipboardEvent('').clipboardData;
        }

        function fire(type, elem) {
          const event = new DragEvent(type, {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
          });
          elem.dispatchEvent(event);
        }

        fire('dragstart', source);
        fire('dragenter', target);
        fire('dragover', target);
        fire('drop', target);
        fire('dragend', source);
        """
        self.driver.execute_script(js, source, target)
