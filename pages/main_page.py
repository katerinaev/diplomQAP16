import allure

from data import DOMEN
from helpers.base_page import BasePage
from pages.locators import MainLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


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

    def click_on_bot_message(self):
        element = self.wait_for(self.main_locators.FRED_MESSAGE)
        self.force_click(element)

    # def click_on_bot_icon(self):
    #     self.wait_and_click(self.main_locators.FRED_ICON)

    def click_on_bot_icon(self):
        iframe_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="drift-frame-controller"]'))
        )

        # Switch to the iframe
        self.driver.switch_to.frame(iframe_element)

        # Now interact with elements inside the iframe
        # For example, click on an element inside the iframe
        element_inside_iframe = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div[3]/div[1]/div[1]/div/div'))
        )
        # element_inside_iframe.click()
        self.wait_and_click(self.main_locators.FRED_ICON)

    @allure.step("Assert Chat bot is open")
    def assert_that_chatbot_open(self):
        iframe_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="drift-frame-controller"]'))
        )

        # Switch to the iframe
        self.driver.switch_to.frame(iframe_element)
        assert self.wait_for(self.main_locators.CHAT_BOT)

    def search_text(self, text):
        self.fill(self.main_locators.SEARCH_INPUT, text)
        # self.wait_and_click(self.main_locators.SUBMIT)
