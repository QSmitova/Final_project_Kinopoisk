import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Этот класс представляет страницу авторизации"""


class AuthPage:
    @allure.step("Настроить браузер, перейти на сайт")
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    @allure.step("Перейти на страницу Кинопоиска")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CLASS_NAME, "styles_loginButton__LWZQp").click()
        # Ожидаем появления поля ввода логина
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.ID, "passp-field-login"))))
        (self.__driver.find_element(By.ID, "passp-field-login").send_keys(email))
        self.__driver.find_element(By.ID, "passp:sign-in").click()
        # Ожидаем появления поля ввода пароля
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.ID, "passp-field-passwd"))))
        (self.__driver.find_element(By.ID, "passp-field-passwd").send_keys(password))
        (self.__driver.find_element(By.ID, "passp:sign-in").click())


