import allure
import pytest

from pages import MainPage


@allure.title("1. Products")
@pytest.mark.parametrize("product_name,product_url", [
    ('//*[@class="solutionWrapper"]//a[1]', 'https://www.frontlineeducation.com/solutions/absence-time/'),
    ('//*[@class="solutionWrapper"]//a[2]', 'https://www.frontlineeducation.com/solutions/central/'),
    ('//*[@class="solutionWrapper"]//a[3]', 'https://www.frontlineeducation.com/solutions/hrms/'),
    ('//*[@class="solutionWrapper"]//a[4]', 'https://www.frontlineeducation.com/solutions/professional-growth/'),
    ('//*[@class="solutionWrapper"]//a[5]', 'https://www.frontlineeducation.com/solutions/recruiting-hiring/'),
    ('//*[@class="solutionWrapper"]//a[6]', 'https://www.frontlineeducation.com/analytics-software/district-comparison/'),
    ('//*[@class="solutionWrapper"]//a[7]', 'https://www.frontlineeducation.com/analytics-software/school-budget-planning/'),
    ('//*[@class="solutionWrapper"]//a[8]', 'https://www.frontlineeducation.com/analytics-software/school-mapping/'),
    ('//*[@class="solutionWrapper"]//a[9]', 'https://www.frontlineeducation.com/analytics-software/student-performance-data/'),
    ('//*[@class="solutionWrapper"]//a[10]', 'https://www.frontlineeducation.com/special-ed-software/medicaid-reimbursement/'),
    ('//*[@class="solutionWrapper"]//a[11]', 'https://www.frontlineeducation.com/solutions/school-health-management/'),
    ('//*[@class="solutionWrapper"]//a[12]', 'https://www.frontlineeducation.com/special-ed-software/'),
    ('//*[@class="solutionWrapper"]//a[13]', 'https://www.frontlineeducation.com/escape/'),
    ('//*[@class="solutionWrapper"]//a[14]', 'https://www.frontlineeducation.com/school-inventory-management-software/'),
    ('//*[@class="solutionWrapper"]//a[15]', 'https://www.frontlineeducation.com/help-desk-software-for-schools/'),
])
def test_open_products(driver, product_name, product_url):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.scroll_to_solution_wrapper()
    main_page.click_on_product_name(product_name)
    main_page.wait_url(product_url)

    main_page.assert_url(product_url)


@allure.title("2. Product tabs")
@pytest.mark.parametrize("product_tab, product_title", [
    ('//*[@class="solution_tabs"]//li[1]', '//h1[text()="Frontline Analytics"]'),
    ('//*[@class="solution_tabs"]//li[2]', '//h1[text()="Frontline HRMS"]'),
    ('//*[@class="solution_tabs"]//li[3]', '//h1[text()="Frontline Recruiting & Hiring"]'),
    ('//*[@class="solution_tabs"]//li[4]', '//h1[text()="Frontline Absence & Time"]'),
    ('//*[@class="solution_tabs"]//li[5]', '//h1[text()="Frontline Professional Growth"]'),
    ('//*[@class="solution_tabs"]//li[6]', '//h1[text()="Frontline Central"]'),
    ('//*[@class="solution_tabs"]//li[7]', '//h1[text()="Frontline ERP"]'),
    ('//*[@class="solution_tabs"]//li[8]', '//h1[text()="Frontline School Health Management"]'),
    ('//*[@class="solution_tabs"]//li[9]', '//h1[text()="Frontline Special Education Management"]'),
    ('//*[@class="solution_tabs"]//li[10]', '//h1[text()="Frontline SIS"]'),
])
def test_open_product_tab(driver, product_tab, product_title):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.scroll_to_product_overview()
    main_page.click_on_product_tab(product_tab)

    main_page.assert_title(product_title)

    # main_page.assert_text(product_title)

# def test_open_bot(driver):
#     main_page = MainPage(driver)
#     main_page.open_page()
#     main_page.click_on_bot_icon()
#
#     main_page.assert_that_chatbot_open()

def test_open_bot(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_bot_icon()

    main_page.assert_that_chatbot_open()


# def test_close_bot(driver):
#     main_page = MainPage(driver)
#     main_page.open_page()
#     main_page.click_on_bot()
#     main_page.close_alert()

