import allure

from pages import MainPage
from pages.hcm_page import HcmPage


@allure.title("1. Open HCM page")
def test_open_hcm_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_learn_more()

    hcm_page = HcmPage(driver)
    hcm_page.assert_that_hcm_page_open()

