# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def open(self, url: str):
        self.driver.get(url)

    def wait_visible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click(self, locator, timeout=None):
        el = self.wait_clickable(locator, timeout)
        # центрируем элемент (часто помогает Firefox)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'center'});", el
        )
        try:
            el.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            el = self.driver.find_element(*locator)
            self.js_click(el)

    def is_visible(self, locator, timeout=3) -> bool:
        try:
            self.wait_visible(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def wait_until(self, condition, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(condition)

    def wait_for_url_contains(self, part: str, timeout=10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(part))
            return True
        except TimeoutException:
            return False

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    def wait_invisible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

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
