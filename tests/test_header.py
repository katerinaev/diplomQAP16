import allure

from pages import MainPage
from pages.contact_us_page import ContactUsPage
from pages.signin_page import SigninPage

from data import DOMEN
from elements.header_element import HeaderElement


@allure.title("2. Open Contact Us page")
def test_open_contact_us_page(driver):
    header_element = HeaderElement(driver)
    header_element.open(DOMEN)
    header_element.click_on_contact_us()

    contact_us_page = ContactUsPage(driver)
    contact_us_page.assert_that_contact_us_page_open()

@allure.title("3. Open Sign In page")
def test_open_sign_in_page(driver):
    header_element = HeaderElement(driver)
    header_element.open(DOMEN)
    header_element.click_on_sign_in()

    sign_in_page = SigninPage(driver)
    sign_in_page.assert_that_sign_in_page_open()
