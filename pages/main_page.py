from data import DOMEN
from helpers.base_page import BasePage
from pages.locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = MainLocators()

    def open_page(self):
        self.open(DOMEN)

    def click_on_learn_more(self):
        self.wait_and_click(self.main_locators.LEARN_MORE)

    def click_on_search_icon(self):
        self.wait_and_click(self.main_locators.SEARCH_ICON)

    def click_on_search(self):
        self.wait_and_click(self.main_locators.SEARCH_INPUT)

    def search_text(self, text):
        self.fill(self.main_locators.SEARCH_INPUT, text)
        # self.wait_and_click(self.main_locators.SUBMIT)
