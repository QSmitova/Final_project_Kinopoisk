import allure
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    url = "https://www.kinopoisk.ru/"
    @allure.step("Настроить браузер, перейти на сайт")
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    @allure.step("Перейти на страницу Кинопоиска")
    def open(self):
        self._driver.get(self.url)

    def get_current_url(self) -> str:
        return self._driver.current_url