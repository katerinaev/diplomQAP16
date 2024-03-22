import allure

from helpers.base_page import BasePage
from pages.locators import SigninLocators


class SigninPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = SigninLocators()

    @allure.step("Assert Contact Us page is open")
    def assert_that_sign_in_page_open(self):
        assert self.wait_for(self.main_locators.SIGN_IN_H1)
