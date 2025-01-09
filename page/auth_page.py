import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage

"""Этот класс представляет страницу авторизации"""


class AuthPage(BasePage):

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        self.find_enter_button().click()
        # Ожидаем появления поля ввода логина
        (WebDriverWait(self._driver, 10).
         until(EC.visibility_of_element_located((By.ID, "passp-field-login"))))
        (self._driver.find_element(By.ID, "passp-field-login").send_keys(email))
        self._driver.find_element(By.ID, "passp:sign-in").click()
        # Ожидаем появления поля ввода пароля
        (WebDriverWait(self._driver, 10).
         until(EC.visibility_of_element_located((By.ID, "passp-field-passwd"))))
        (self._driver.find_element(By.ID, "passp-field-passwd").send_keys(password))
        (self._driver.find_element(By.ID, "passp:sign-in").click())


    def find_enter_button(self) -> WebElement:
        return self._driver.find_element(By.CLASS_NAME, "styles_loginButton__LWZQp")

    def enter_button_exist(self) -> bool:
        try:
            self.find_enter_button()
            return True
        except NoSuchElementException:
            return False