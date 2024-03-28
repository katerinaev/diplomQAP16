import allure
import pytest

from pages import MainPage
from pages.contact_us_page import ContactUsPage
from pages.signin_page import SigninPage

from data import DOMEN
from elements.header_element import HeaderElement

@allure.title("1. HCM Solutions")
@pytest.mark.parametrize("hcm_solution, hcm_solution_url", [
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[1]', 'https://www.frontlineeducation.com/solutions/absence-time/'),
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[2]', 'https://www.frontlineeducation.com/solutions/central/'),
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[3]', 'https://www.frontlineeducation.com/solutions/hrms/'),
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[4]', 'https://www.frontlineeducation.com/analytics-software/human-capital-analytics/'),
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[5]', 'https://www.frontlineeducation.com/solutions/professional-growth/'),
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[6]', 'https://www.frontlineeducation.com/solutions/recruiting-hiring/'),
    ('//div[@class="section-menu--list hcm-menu"]/child::ul[1]/li[7]', 'https://www.frontlineeducation.com/school-hcm-software/'),
])
def test_open_hcm_solutions(driver, hcm_solution, hcm_solution_url):
    header_element = HeaderElement(driver)
    header_element.open(DOMEN)
    header_element.click_on_solutions()
    header_element.click_on_hcm_solutions(hcm_solution)
    header_element.wait_url(hcm_solution_url)

    header_element.assert_url(hcm_solution_url)


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
