import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.base_page import BasePage

"""Этот класс представляет страницу поиска фильмов"""


class MoviePage(BasePage):
    @allure.step("Поиск фильма по названию в строке поиска")
    def find_by_title(self, title: str):
        search_input = self._driver.find_element(By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]')
        search_input.click()
        search_input.send_keys(title)
        search_input.send_keys(Keys.RETURN)

    @allure.step("Открытие страницы расширенного поиска")
    def open_extended_search(self):
        self._driver.find_element(By.CSS_SELECTOR, '[aria-label="Расширенный поиск"]').click()

    @allure.step("Поиск фильма по году выпуска")
    def find_by_year(self, year:int):
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[2]/"
                                             "div[2]/div[1]/form[1]/div[1]/div[1]/a[1]/*[name()='svg'][1]").click()
        year_input = self._driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]"
                                             "/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[7]")
        year_input.click()
        year_input.send_keys(year) #не нравится Питону аргумент "год". Делала аналогично тесту на поиск по названию.
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/"
                                             "td[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[11]").click()
    # здесь нужно написать проверку, открывается список или url нужный, или еще как

    @allure.step("Поиск Топ-250 сериалы")
    def find_by_top_series(self):
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[2]/"
                                             "div[2]/div[1]/form[1]/div[1]/div[1]/a[1]/*[name()='svg'][1]").click()
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/"
                                             "td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/ul[1]/li[1]/a[1]").click()
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]"
                                                 "/ul[1]/li[2]/a[1]").click()
    #здесь нужно написать проверку, открывается список или url нужный, или еще как

    @allure.step("Переход на страницу онлайн-кинотеатра")
    def get_online_cinema_button(self) -> WebElement:
        return self._driver.find_element(
            By.CSS_SELECTOR,
            '[src="https://avatars.mds.yandex.net/get-bunker/50064/15d30528c2394db32f9624a0fa4ff244f79d8c7c/orig"]'
        )

    @allure.step("Проверка существования кнопки Онлайн-кинотеатра")
    def online_cinema_button_exist(self) -> bool:
        try:
            self.get_online_cinema_button()
            return True
        except NoSuchElementException:
            return False

    @allure.step("Поиск кнопки 'Войти' на главной странице")
    def find_enter_button(self) -> WebElement:
        return self._driver.find_element(By.CLASS_NAME, "styles_loginButton__LWZQp")

    @allure.step("Проверка существования кнопки 'Войти'")
    def enter_button_exist(self) -> bool:
        try:
            self.find_enter_button()
            return True
        except NoSuchElementException:
            return False

    @allure.step("Открытие страницы авторизации")
    def open_auth_page(self) -> None:
        self.find_enter_button().click()