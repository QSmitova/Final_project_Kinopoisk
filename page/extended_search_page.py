from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ExtendedSearchPage(BasePage):
    def open_top_250_page(self):
        self._driver.find_element(By.CSS_SELECTOR, "div.block_left_pad table ul>li:nth-child(1)").click()
