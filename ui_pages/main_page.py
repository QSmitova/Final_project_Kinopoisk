import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from ui_pages.base_page import BaseKinopoiskPage


class MainPage(BaseKinopoiskPage):
    """ Класс, описывающий главную страницу кинопоиска """

    @allure.step("Поиск поля поиска")
    def find_search_input(self) -> WebElement:
        return self.find_element(By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]')

    @allure.step("Поиск фильма по названию в строке поиска")
    def find_by_title(self, title: str):
        search_input = self.find_search_input()
        allure.step("Нажатие на поле поиска")
        search_input.click()
        allure.step(f"Ввод значения: {title} в поле поиска")
        search_input.send_keys(title)
        allure.step("Подтверждение ввода в поле поиска (Keys.RETURN)")
        search_input.send_keys(Keys.RETURN)
