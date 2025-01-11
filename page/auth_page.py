import os
import pickle
from pathlib import Path
from time import sleep

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import focus
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage

"""Этот класс представляет страницу авторизации"""


class AuthPage(BasePage):
    COOKIE_PATH = Path(os.getcwd()) / 'cookies/cookie'
    url = "https://passport.yandex.ru/auth"

    def cookie_exists(self) -> bool:
        return os.path.exists(self.COOKIE_PATH)

    def save_cookie(self) -> None:
        with open(self.COOKIE_PATH, 'wb') as filehandler:
            pickle.dump(self._driver.get_cookies(), filehandler)

    def load_cookie(self) -> None:
        with open(self.COOKIE_PATH, 'rb') as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                self._driver.add_cookie(cookie)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str) -> bool:
        # Ожидаем появления поля ввода логина
        (WebDriverWait(self._driver, 10).
         until(EC.visibility_of_element_located((By.ID, "passp-field-login"))))

        if self.cookie_exists():
            self.load_cookie()
            sleep(3)
            return False

        (self._driver.find_element(By.ID, "passp-field-login").send_keys(email))
        self._driver.find_element(By.ID, "passp:sign-in").click()
        # Ожидаем появления поля ввода пароля
        (WebDriverWait(self._driver, 10).
         until(EC.visibility_of_element_located((By.ID, "passp-field-passwd"))))
        (self._driver.find_element(By.ID, "passp-field-passwd").send_keys(password))
        (self._driver.find_element(By.ID, "passp:sign-in").click())
        return True
