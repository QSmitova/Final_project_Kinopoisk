import pytest
import allure
from selenium import webdriver

from testdata.DataProvider import DataProvider

"""Фикстура перехода на страницу"""


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

"""Фикстура с данными для авторизации на сайте"""

@pytest.fixture
def test_data():
    return DataProvider()


