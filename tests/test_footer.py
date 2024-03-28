import allure

from data import DOMEN
from elements.footer_element import FooterElement


@allure.title("3. Footer: solution")
def test_footer_solutions(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_solution_visible()


@allure.title("4. Footer: resource")
def test_footer_resources(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_resource_visible()


@allure.title("5. Footer: about")
def test_footer_about(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_about_visible()


@allure.title("6. Footer: learn more")
def test_footer_learn_more(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_learn_more_visible()
