import allure

from helpers.base_page import BasePage
from pages.locators import ContactLocators


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = ContactLocators()

    @allure.step("Assert Contact Us page is open")
    def assert_that_contact_us_page_open(self):
        assert self.wait_for(self.main_locators.CONTACT_US_H1)
