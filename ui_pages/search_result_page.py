import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ui_pages.base_page import BaseKinopoiskPage

""" Класс, описывающий страницу результата поиска """


class SearchResultPage(BaseKinopoiskPage):
    @allure.step("Поиск карточки фильма")
    def find_result_card(self) -> WebElement:
        return self.find_element(By.CLASS_NAME, "element.most_wanted")

    @allure.step("Проверка существования карточки фильма")
    def result_card_exist(self) -> bool:
        return self.element_exists(By.CLASS_NAME, "element.most_wanted")
