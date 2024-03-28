import allure

from helpers.base_page import BasePage


class HeaderElement(BasePage):
    CONTACT_US = '//a[@class="nav-utility-item--link"][contains(@href, "contact-us")]'
    # SIGN_IN = '//a[@class="nav-utility-item--link"][contains(@href, "contact-us")]'
    SIGN_IN = '//*[@class="nav-utility-menu-list"]//a[text()="Sign In"]'
    SOLUTIONS = '//*[@data-target="#solutions-dropdown-menu"]'
    HCM_SOLUTIONS = '//div[@class="section-menu--list hcm-menu"]/child::ul[1]'
    HCM_SOLUTION = '//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_contact_us(self):
        self.wait_and_click(self.CONTACT_US)

    def click_on_sign_in(self):
        self.wait_and_click(self.SIGN_IN)

    def click_on_solutions(self):
        self.wait_and_click(self.SOLUTIONS)

    def click_on_hcm_solutions(self, element):
        self.wait_and_click(element)

