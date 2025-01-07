import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Этот класс представляет страницу поиска фильмов"""


class MoviePage:
    @allure.step("Настроить браузер, перейти на сайт")
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    @allure.step("Перейти на страницу Кинопоиска")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Поиск фильма по названию в строке поиска")
    def find_by_title(self, title: str):
        self.__driver.find_element(By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]').click()
        search_input = self.__driver.find_element(By.CSS_SELECTOR, '[aria-label="Фильмы, сериалы, персоны"]')
        search_input.send_keys(title)
        search_input.send_keys(Keys.RETURN)
    #здесь нужно написать проверку, вернуть список найденных фильмов по названию, если не найдены, вывести сообщение, что результатов нет

    @allure.step("Поиск Топ-250 фильмы")
    def find_by_top_movie(self):
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[2]/"
                                             "div[2]/div[1]/form[1]/div[1]/div[1]/a[1]/*[name()='svg'][1]").click()
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/"
                                             "td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/ul[1]/li[1]/a[1]").click()
    #здесь нужно написать проверку, открывается список или url нужный, или еще как

    @allure.step("Поиск фильма по году выпуска")
    def find_by_year(self, year:int):
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[2]/"
                                             "div[2]/div[1]/form[1]/div[1]/div[1]/a[1]/*[name()='svg'][1]").click()
        year_input = self.__driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]"
                                             "/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[7]")
        year_input.click()
        year_input.send_keys(year) #не нравится Питону аргумент "год". Делала аналогично тесту на поиск по названию.
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/"
                                             "td[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[11]").click()
    # здесь нужно написать проверку, открывается список или url нужный, или еще как

    @allure.step("Поиск Топ-250 сериалы")
    def find_by_top_series(self):
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[2]/"
                                             "div[2]/div[1]/form[1]/div[1]/div[1]/a[1]/*[name()='svg'][1]").click()
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/"
                                             "td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/ul[1]/li[1]/a[1]").click()
        self.__driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]"
                                                 "/ul[1]/li[2]/a[1]").click()
    #здесь нужно написать проверку, открывается список или url нужный, или еще как

    @allure.step("Переход на страницу онлайн-кинотеатра")
    def online_cinema(self):
        self.__driver.find_element(By.CSS_SELECTOR, '[src="https://avatars.mds.yandex.net/get-bunker/50064/15d30528c2394db32f9624a0fa4ff244f79d8c7c/orig"]').click()

