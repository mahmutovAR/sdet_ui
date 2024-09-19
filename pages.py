from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import AddCustomerLocators, CustomersLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'

    def open_url(self) -> None:
        self.browser.get(self.url)

    def wait_to_be_clickable(self, input_locator: WebElement) -> WebElement:
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(input_locator))

    def wait_for_visibility(self, input_locator: WebElement) -> WebElement:
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(input_locator))


class AddCustomerPage(BasePage):
    def go_to_form_page(self) -> None:
        tab = self.wait_to_be_clickable(AddCustomerLocators.tab)
        tab.click()

    def enter_first_name(self, input_data: str) -> None:
        first_name_field = self.wait_to_be_clickable(AddCustomerLocators.first_name)
        first_name_field.send_keys(input_data)

    def enter_last_name(self, input_data: str) -> None:
        last_name_field = self.wait_to_be_clickable(AddCustomerLocators.last_name)
        last_name_field.send_keys(input_data)

    def enter_post_code(self, input_data: str) -> None:
        post_code_field = self.wait_to_be_clickable(AddCustomerLocators.post_code)
        post_code_field.send_keys(input_data)

    def submit_data(self) -> None:
        self.wait_to_be_clickable(AddCustomerLocators.submit_button).submit()


class CustomersPage(BasePage):
    def go_to_page(self) -> None:
        tab = self.wait_to_be_clickable(CustomersLocators.tab)
        tab.click()

    def table_is_visible(self) -> None:
        self.wait_for_visibility(CustomersLocators.table)

    def search_customer(self, input_data: str) -> None:
        search_field = self.wait_to_be_clickable(CustomersLocators.search)
        search_field.send_keys(input_data)

    def sort_customers_by_first_name(self) -> None:
        sort_customers = self.wait_to_be_clickable(CustomersLocators.first_name_button)
        sort_customers.click()

    def delete_customer(self) -> None:
        delete_button = self.wait_to_be_clickable(CustomersLocators.delete_button)
        delete_button.click()
