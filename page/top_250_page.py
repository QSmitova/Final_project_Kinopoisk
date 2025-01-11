from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page.base_page import BasePage


class Top250Page(BasePage):
    def find_page_title(self) -> WebElement:
        return self._driver.find_element(
            By.CSS_SELECTOR,
            "#__next > div > div > div > div > main > div > div > h1"
        )

    def page_title_exist(self) -> bool:
        try:
            self.find_page_title()
            return True
        except NoSuchElementException:
            return False