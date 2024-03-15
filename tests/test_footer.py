import allure

from data import DOMEN
from elements.footer_element import FooterElement


@allure.title("3. Footer: solution")
def test_footer_solutions(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_solution_visible()
