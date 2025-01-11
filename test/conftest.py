import pickle
from pathlib import Path
import pytest
import allure
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options

from page.auth_page import AuthPage
from page.extended_search_page import ExtendedSearchPage
from page.movie_api import MovieApi
from page.movie_page import MoviePage
from page.search_page import SearchPage
from page.top_250_page import Top250Page
from testdata.data_provider import DataProvider
from fake_useragent import UserAgent


"""Фикстура перехода на страницу"""


@pytest.fixture(scope="session")
def browser():
    with allure.step("Открыть и настроить браузер"):
        ua = UserAgent(os='Windows')
        opts = Options()
        opts.add_argument(f'--user-agent={ua}')
        browser = webdriver.Chrome(options=opts)
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

@pytest.fixture(scope="module")
def search_ui_page(browser) -> SearchPage:
    return SearchPage(browser)

@pytest.fixture(scope="module")
def extended_search_ui_page(browser) -> ExtendedSearchPage:
    return ExtendedSearchPage(browser)

"""Фикстура для страницыТоп-250"""
@pytest.fixture(scope="module")
def top_250_ui_page(browser) -> Top250Page:
    return Top250Page(browser)

