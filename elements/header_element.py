import allure

from helpers.base_page import BasePage


class HeaderElement(BasePage):
    CONTACT_US = '//a[@class="nav-utility-item--link"][contains(@href, "contact-us")]'
    # SIGN_IN = '//a[@class="nav-utility-item--link"][contains(@href, "contact-us")]'
    SIGN_IN = '//*[@class="nav-utility-menu-list"]//a[text()="Sign In"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_contact_us(self):
        self.wait_and_click(self.CONTACT_US)

    def click_on_sign_in(self):
        self.wait_and_click(self.SIGN_IN)
