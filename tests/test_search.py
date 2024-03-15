import allure
import pytest

from pages import MainPage


# def test_search(driver):
#     main_page = MainPage(driver)
#     main_page.open_page()
#     main_page.click_on_search_icon()
#     main_page.search_text('school')
#
#     main_page.assert_text('schools across the country')

@allure.title("2. Search")
@pytest.mark.parametrize("search_input,expected", [
    ('school', 'schools across the country'),
    ('       ', 'Frontline Central manages'),
    ('', 'Frontline Central manages'),
    ('school administration', 'Frontline empowers strategic K-12 leaders with school administration software'),
    ('!@#$%', 'Sorry, we couldn’t find anything matching'),
])
def test_search(driver, search_input, expected):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_search_icon()
    main_page.search_text(search_input)

    main_page.assert_text(expected)
