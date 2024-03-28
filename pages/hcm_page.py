import allure

from helpers.base_page import BasePage
from pages.locators import HCMLocators


class HcmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = HCMLocators()

    @allure.step("Assert HCM page is open")
    def assert_that_hcm_page_open(self):
        assert self.wait_for(self.main_locators.SOLUTION_HERO)

    @allure.step("Assert Sidebar text")
    def assert_sidebar_text(self, locator, text):
        assert self.wait_for(locator) == text
