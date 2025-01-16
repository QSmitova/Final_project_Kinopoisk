import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" Базовый класс """


class BasePage:
    url = None

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def open(self):
        with allure.step(f"Открытие страницы: {self.url}"):
            self._driver.get(self.url)

    @allure.step("Обновление страницы")
    def refresh(self):
        self._driver.refresh()

    @allure.step("Получение url текущей страницы")
    def get_current_url(self) -> str:
        return self._driver.current_url

    @allure.step("Поиск элемента на странице")
    def find_element(self, by: str, value: str, *, timeout: int = 10) -> WebElement:
        WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

        return self._driver.find_element(by, value)

    @allure.step("Проверка существования элемента на странице")
    def element_exists(self, by: str, value: str, *, timeout: int = 10) -> bool:
        try:
            self.find_element(by, value, timeout=timeout)
            return True
        except (NoSuchElementException, TimeoutException):
            return False


"""
    Базовый класс страницы кинопоиска с методами для поиска общих элементов всех страниц:
    элементов шапки, футера и т.д.
"""


class BaseKinopoiskPage(BasePage):

    url = "https://www.kinopoisk.ru/"

    @allure.step("Поиск кнопки `войти`")
    def find_enter_button(self) -> WebElement:
        return self.find_element(By.CLASS_NAME, "styles_loginButton__LWZQp")

    @allure.step("Проверка существования кнопки `войти`")
    def enter_button_exists(self) -> bool:
        return self.element_exists(By.CLASS_NAME, "styles_loginButton__LWZQp")

    @allure.step("Поиск кнопки `Онлайн кинотеатр`")
    def find_online_cinema_button(self) -> WebElement:
        return self.find_element(
            By.CSS_SELECTOR,
            '[src="https://avatars.mds.yandex.net/get-bunker/'
            '50064/15d30528c2394db32f9624a0fa4ff244f79d8c7c/orig"]'
        )

    @allure.step("Проверка существования кнопки `Онлайн кинотеатр`")
    def online_cinema_button_exists(self) -> bool:
        return self.element_exists(
            By.CSS_SELECTOR,
            '[src="https://avatars.mds.yandex.net/get-bunker/'
            '50064/15d30528c2394db32f9624a0fa4ff244f79d8c7c/orig"]'
        )

    @allure.step("Нажатие на кнопку `войти` (переход на страницу авторизации)")
    def open_auth_page(self) -> None:
        self.find_enter_button().click()

    @allure.step("Нажатие на кнопку `Онлайн кинотеатр` (переход на страницу онлайн кинотеатра)")
    def open_online_cinema_page(self) -> None:
        self.find_online_cinema_button().click()

    @allure.step("Нажатие на иконку `Расширенный поиск` (переход на страницу расширенного поиска)")
    def open_extended_search(self):
        self.find_element(By.CSS_SELECTOR, '[aria-label="Расширенный поиск"]').click()

    @allure.step("Проверка авторизации пользователя")
    def is_user_logged_in(self) -> bool:
        is_logged_in = self.online_cinema_button_exists() and not self.enter_button_exists()
        allure.step(
            "Пользователь " +
            ("авторизован" if is_logged_in else "не авторизован")
        )
        return is_logged_in
