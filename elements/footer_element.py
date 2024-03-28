import allure

from helpers.base_page import BasePage


class FooterElement(BasePage):
    SOLUTION = '//*[@class="footer-txt-link"][text()="{solution}"]'
    RESOURCE = '//*[@class="footer-txt-link"][text()="{resource}"]'
    ABOUT = '//*[@class="footer-txt-link"][text()="{about}"]'
    LEARN_MORE = '//*[@class="footer-txt-link"][text()="{learn_more}"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Assert solution is visible")
    def assert_solution_visible(self):
        self.wait_for(self.SOLUTION.format(solution='HRMS'))
        self.wait_for(self.SOLUTION.format(solution='Human Capital Analytics'))
        self.wait_for(self.SOLUTION.format(solution='Recruiting & Hiring'))
        self.wait_for(self.SOLUTION.format(solution='Absence & Time'))
        self.wait_for(self.SOLUTION.format(solution='Professional Growth'))
        self.wait_for(self.SOLUTION.format(solution='Frontline Central'))
        self.wait_for(self.SOLUTION.format(solution='Comparative Analytics'))
        self.wait_for(self.SOLUTION.format(solution='Financial Planning & Budget Management Analytics'))
        self.wait_for(self.SOLUTION.format(solution='Location Analytics'))
        self.wait_for(self.SOLUTION.format(solution='Student Analytics Lab'))
        self.wait_for(self.SOLUTION.format(solution='Inventory Management'))
        self.wait_for(self.SOLUTION.format(solution='Help Desk Management'))
        self.wait_for(self.SOLUTION.format(solution='Frontline ERP'))
        self.wait_for(self.SOLUTION.format(solution='Special Ed & Interventions'))
        self.wait_for(self.SOLUTION.format(solution='Medicaid & Service Management'))
        self.wait_for(self.SOLUTION.format(solution='School Health Management'))
        self.wait_for(self.SOLUTION.format(solution='Frontline SIS'))

    @allure.step("Assert resource is visible")
    def assert_resource_visible(self):
        self.wait_for(self.RESOURCE.format(resource='Frontline Blog'))
        self.wait_for(self.RESOURCE.format(resource='Resource Center'))
        self.wait_for(self.RESOURCE.format(resource='Field Trip Podcast'))
        self.wait_for(self.RESOURCE.format(resource='Webinars'))
        self.wait_for(self.RESOURCE.format(resource='Events'))
        self.wait_for(self.RESOURCE.format(resource='Frontline Research & Learning Institute '))
        self.wait_for(self.RESOURCE.format(resource='The Line '))


    @allure.step("Assert about is visible")
    def assert_about_visible(self):
        self.wait_for(self.ABOUT.format(about='About Frontline Education'))
        self.wait_for(self.ABOUT.format(about='Our People'))
        self.wait_for(self.ABOUT.format(about='Security'))
        self.wait_for(self.ABOUT.format(about='Careers'))
        self.wait_for(self.ABOUT.format(about='Partner Information'))
        self.wait_for(self.ABOUT.format(about='Find a Partner'))

    @allure.step("Assert learn more is visible")
    def assert_learn_more_visible(self):
        self.wait_for(self.LEARN_MORE.format(learn_more='Contact Us'))
        self.wait_for(self.LEARN_MORE.format(learn_more='Become a Partner'))
        self.wait_for(self.LEARN_MORE.format(learn_more='News'))
        self.wait_for(self.LEARN_MORE.format(learn_more='Privacy'))
        self.wait_for(self.LEARN_MORE.format(learn_more='Terms of Use'))
        self.wait_for(self.LEARN_MORE.format(learn_more='Aetna Transparency'))
    # def get_solution(self, solution):
    #     return f'//*[@class="footer-txt-link"][contains(text(), "{solution}")]'
