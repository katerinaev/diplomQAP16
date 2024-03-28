import allure
import pytest

from data import HCM_URL
from pages import MainPage
from pages.hcm_page import HcmPage


@allure.title("1. Open HCM page")
def test_open_hcm_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_learn_more()

    hcm_page = HcmPage(driver)
    hcm_page.assert_that_hcm_page_open()

@allure.title("2. HCM: Sidebar")
@pytest.mark.parametrize("product_tab, product_text", [
    ('//button[contains(@class, "accordianTrigger")][1]', 'Get a connected view of what’s happening with your employees.'),
    ('//button[contains(@class, "accordianTrigger")][2]', 'Hire the best educators.'),
    ('//button[contains(@class, "accordianTrigger")][3]', 'Engage and retain top talent.'),
    ('//button[contains(@class, "accordianTrigger")][4]', 'Get the complete view of employee attendance.'),
    ('//button[contains(@class, "accordianTrigger")][5]', 'Access unique insights across solutions in Frontline HCM.'),
    ('//button[contains(@class, "accordianTrigger")][6]', 'Be proactive from recruiting to retirement.'),
])
def test_text(driver, product_tab, product_text):
    hcm_page = HcmPage(driver)
    hcm_page.open(HCM_URL)
    hcm_page.scroll_to(product_tab)
    hcm_page.wait_and_click(product_tab)

    hcm_page.assert_sidebar_text(product_tab, product_text)

