import pytest
import allure

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium_stealth import stealth

from ui_pages.auth_page import AuthPage
from ui_pages.main_page import MainPage
from ui_pages.extended_search_page import ExtendedSearchPage
from api.movie_api import MovieApi
from ui_pages.search_result_page import SearchResultPage
from ui_pages.top_250_page import Top250Page

from test_data.data_provider import DataProvider


def create_driver() -> WebDriver:
    """
        Функция для создания объекта WebDriver с настройками бразуера,
        позволяющими снизить вероятность обнаружение автоматизированного ПО
    """

    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless') # опция для запуска браузера без GUI-интерфейса

    driver = webdriver.Chrome(options=options)
    ua = UserAgent(browsers='chrome', os='windows', platforms='pc').random

    stealth(
        driver=driver,
        user_agent=ua,
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        run_on_insecure_origins=True
    )

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
      '''
    })
    return driver


@pytest.fixture(scope="session")
def browser() -> WebDriver:
    """Фикстура для получения объекта WebDriver"""

    with allure.step("Открыть и настроить браузер"):
        browser = create_driver()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture(scope="session")
def test_data() -> DataProvider:
    """Фикстура создания объекта для получения данных"""
    return DataProvider()


@pytest.fixture(scope="module")
def movie_api(test_data: DataProvider) -> MovieApi:
    """Фикстура для получения класса для взаимодействия с API"""
    return MovieApi(test_data.get_api_token())


@pytest.fixture(scope="module")
def auth_ui_page(browser) -> AuthPage:
    """Фикстура для получения страницы авторизации"""
    return AuthPage(browser)


@pytest.fixture(scope="module")
def main_ui_page(browser) -> MainPage:
    """Фикстура для получения главной страницы"""
    return MainPage(browser)


@pytest.fixture(scope="module")
def search_ui_page(browser) -> SearchResultPage:
    """Фикстура для получения страницы поиска"""
    return SearchResultPage(browser)


@pytest.fixture(scope="module")
def extended_search_ui_page(browser) -> ExtendedSearchPage:
    """Фикстура для получения страницы расширенного поиска"""
    return ExtendedSearchPage(browser)


@pytest.fixture(scope="module")
def top_250_ui_page(browser) -> Top250Page:
    """Фикстура для получения страницы топ 250"""
    return Top250Page(browser)
