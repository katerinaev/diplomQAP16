import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def wait_for(self, locator, time_out=10):
        try:
            return WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
        except TimeoutException:
            assert False, f'Element {locator} doesnt found'

    def wait_and_click(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element.click()
            return element
        except TimeoutException:
            assert False, f'Element {locator} doesnt found'

    def open(self, url):
        self.driver.get(url)

    def fill(self, locator, text):
        element = self.wait_for(locator)
        element.send_keys(text)
        element.submit()

    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
    @allure.step("Assert text is visible")
    def assert_text(self, text):
        assert self.wait_for(f'//*[contains(text(), "{text}")]'), "Text is not visible"


#
#     def force_click(self, element):
#         self.driver.execute_script("arguments[0].click();", element)
#
#     def scroll_to(self):
#         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     def click_on(self, locator):
#         element = self.get_locator_by_class(locator)
#         element.click()
#
#     def get_by_class_css(self, selector):
#         return f'[class="{selector}"]'
#
#     def get_locator_by_class(self, selector):
#         selector = self.get_by_class_css(selector)
#         return self.driver.find_element(By.CSS_SELECTOR, selector)
#
#     def get_locator_by_css(self, selector):
#         return self.driver.find_element(By.CSS_SELECTOR, selector)
#
#     def get_by_data_id(self, data_id):
#         return f"//*[data-id={data_id}]"
