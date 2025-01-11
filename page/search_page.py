import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page.base_page import BasePage


class SearchPage(BasePage):
    def find_result_card(self) -> WebElement:
        return self._driver.find_element(By.CLASS_NAME, "element.most_wanted")

    @allure.step("Проверка наличия карточки фильма")
    def result_card_exist(self) -> bool:
        try:
            self.find_result_card()
            return True
        except NoSuchElementException:
            return False