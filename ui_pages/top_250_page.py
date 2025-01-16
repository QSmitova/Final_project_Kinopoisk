import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ui_pages.base_page import BaseKinopoiskPage

""" Класс, описывающий страницу Топ 250 """


class Top250Page(BaseKinopoiskPage):
    @allure.step("Поиск заголовка страницы `Топ 250`")
    def find_page_title(self) -> WebElement:
        return self.find_element(
            By.CSS_SELECTOR,
            "#__next > div > div > div > div > main > div > div > h1"
        )

    @allure.step("Проверка существования заголовка страницы `Топ 250`")
    def page_title_exists(self) -> bool:
        return self.element_exists(
            By.CSS_SELECTOR,
            "#__next > div > div > div > div > main > div > div > h1"
        )

    @allure.step("Получение текста заголовка страницы `Топ 250`")
    def get_page_title_text(self) -> str:
        return self.find_page_title().text

    @allure.step("Нахождение кнопки `Топ 250 сериалов`")
    def find_series_button(self) -> WebElement:
        return self.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]"
        )

    @allure.step("Нажатие на кнопку `Top250 сериалов` (Переход на страницу топ 250 сериалов)")
    def open_series(self):
        self.find_series_button().click()
