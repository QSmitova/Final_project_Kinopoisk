import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ui_pages import BaseKinopoiskPage


class ExtendedSearchPage(BaseKinopoiskPage):

    @allure.step("Поиск кнопки `Top250`")
    def find_top250_button(self) -> WebElement:
        return self.find_element(By.CSS_SELECTOR, "div.block_left_pad table ul>li:nth-child(1)")

    @allure.step("Нажатие на кнопку `Top250` (Переход на страницу топ 250 фильмов)")
    def open_top_250_page(self):
        self.find_top250_button().click()

    @allure.step("Поиск поля года выпуска фильма")
    def find_year_input(self) -> WebElement:
        return self.find_element(By.ID, "year")

    @allure.step("Поиск кнопки `Поиск`")
    def find_search_button(self) -> WebElement:
        return self.find_element(
            By.XPATH,
            "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/"
            "tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[11]"
        )

    @allure.step("Поиск фильма по году выпуска")
    def find_movies_by_year(self, year: int):
        year_input = self.find_year_input()
        with allure.step(f'Ввод значения: {year} в поле поиска по году'):
            year_input.send_keys(str(year))
        search_button = self.find_search_button()
        with allure.step("Нажать на кнопку `Поиск`"):
            search_button.click()
