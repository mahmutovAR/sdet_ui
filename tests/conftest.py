from bs4 import BeautifulSoup
from pytest import fixture
from selenium import webdriver

from data import generate_form_data


@fixture
def set_up_browser():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@fixture
def get_generated_data():
    yield generate_form_data()


@fixture
def get_all_customers():
    def get_data(web_driver: webdriver):
        html = web_driver.page_source
        soup_object = BeautifulSoup(html, "lxml")
        return soup_object.find('table', class_='table').tbody
    return get_data
