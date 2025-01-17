import os.path
import pickle
from pathlib import Path
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ui_pages.base_page import BasePage

""" Класс, описывающий страницу авторизации """


class AuthPage(BasePage):
    url = "https://passport.yandex.com/auth"
    COOKIE_PATH = Path(os.getcwd()) / 'cookies/cookie'

    @allure.step("Проверка наличия сохраненных ранее cookie-файлов")
    def cookies_exists(self) -> bool:
        cookies_exists = os.path.exists(self.COOKIE_PATH)
        with allure.step(
            "Cookie-файлы " +
            ("существуют" if cookies_exists else "не существуют")
        ):

            return cookies_exists

    @allure.step("Cохранение cookie в файл")
    def save_cookies(self) -> None:
        with open(self.COOKIE_PATH, 'wb') as cookies_file:
            pickle.dump(self._driver.get_cookies(), cookies_file)

    @allure.step("Загрузка cookie из файла")
    def load_cookies(self) -> None:
        with open(self.COOKIE_PATH, 'rb') as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                self._driver.add_cookie(cookie)

    @allure.step("Поиск поля ввода логина в форме авторизации")
    def find_login_input(self) -> WebElement:
        return self.find_element(By.ID, "passp-field-login")

    @allure.step("Поиск поля ввода пароля в форме авторизации")
    def find_password_input(self) -> WebElement:
        return self.find_element(By.ID, "passp-field-passwd")

    @allure.step("Поиск кнопки `войти` в форме авторизации")
    def find_signin_button(self) -> WebElement:
        return self.find_element(By.ID, "passp:sign-in")

    @allure.step("Проверка существования поля ввода логина в форме авторизации")
    def login_input_exists(self) -> bool:
        return self.element_exists(By.ID, "passp-field-login")

    def login(self, email: str, password: str) -> None:
        with allure.step(f"Авторизация пользователя с email: {email} и паролем: {password}"):
            login_input = self.find_login_input()
        with allure.step(f"Ввод значения: {email} в поле ввода логина в форме авторизации"):
            login_input.send_keys(email)
        with allure.step("Нажатие на кнопку `войти` в форме авторизации"):
            self.find_signin_button().click()

            password_input = self.find_password_input()
        with allure.step(f"Ввод значения: {password} в поле ввода пароля в форме авторизации"):
            password_input.send_keys(password)
        with allure.step("Нажатие на кнопку `войти` в форме авторизации"):
            self.find_signin_button().click()
