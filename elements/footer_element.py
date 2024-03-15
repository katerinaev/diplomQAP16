import allure

from helpers.base_page import BasePage


class FooterElement(BasePage):
    SOLUTION = '//*[@class="footer-txt-link"][contains(text(), "{solution}")]'

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


    # def get_solution(self, solution):
    #     return f'//*[@class="footer-txt-link"][contains(text(), "{solution}")]'
