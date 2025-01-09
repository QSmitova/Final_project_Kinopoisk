import pytest
import allure
from selenium import webdriver

from page.auth_page import AuthPage
from page.movie_api import MovieApi
from page.movie_page import MoviePage
from testdata.data_provider import DataProvider

"""Фикстура перехода на страницу"""


@pytest.fixture(scope="session")
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

"""Фикстура с данными для авторизации на сайте"""

@pytest.fixture(scope="session")
def test_data() -> DataProvider:
    return DataProvider()

"""Фикстура для получения API"""

@pytest.fixture(scope="module")
def movie_api(test_data:DataProvider) -> MovieApi:
    return MovieApi(test_data.get_key(), test_data.get_value())

"""Фикстура для получения страницы авторизации"""

@pytest.fixture(scope="module")
def auth_ui_page(browser) -> AuthPage:
    return AuthPage(browser)

"""Фикстура для страницы поисков фильмов"""

@pytest.fixture(scope="module")
def movie_ui_page(browser) -> MoviePage:
    return MoviePage(browser)
