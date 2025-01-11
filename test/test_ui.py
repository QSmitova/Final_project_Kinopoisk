from time import sleep
from tokenize import cookie_re

import allure
import os
from pathlib import Path
from page.auth_page import AuthPage
from page.movie_page import MoviePage


@allure.title("Тест на проверку авторизации")
@allure.severity("critical")
def test_auth(auth_ui_page, movie_ui_page, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")

    movie_ui_page.open()
    movie_ui_page.open_auth_page()
    if not auth_ui_page.login_as(email, password):
        movie_ui_page.open()

    with allure.step("Проверка успешной авторизации"):
        assert movie_ui_page.get_online_cinema_button()
        assert not movie_ui_page.enter_button_exist()

    auth_ui_page.open()
    auth_ui_page.save_cookie()


@allure.title("Тест на поиск фильма по названию")
@allure.severity("critical")
def test_find_movie_by_title(movie_ui_page, search_ui_page):
    movie_ui_page.open()
    movie_ui_page.find_by_title("Чебурашка")
    assert search_ui_page.result_card_exist() #существует карточка
    movie_ui_page.find_by_title("тмьдмт")
    assert not search_ui_page.result_card_exist() # не существует карточка


@allure.title("Тест на поиск коллекции ТОП-250 фильмов")
@allure.severity("major")
def test_find_top_250_movie(movie_ui_page, extended_search_ui_page, top_250_ui_page):
    movie_ui_page.open()
    movie_ui_page.open_extended_search()
    extended_search_ui_page.open_top_250_page()
    assert top_250_ui_page.page_title_exist()




@allure.title("Тест на поиск по году выпуска")
@allure.severity("major")
def test_find_by_year(browser):
    year = 2020
    auth_page = AuthPage(browser)
    auth_page.go()
    movie_page = MoviePage(browser)
    movie_page.find_by_year()

@allure.title("Тест на поиск коллекции ТОП-250 сериалов")
@allure.severity("major")
def test_find_top_250_series(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    movie_page = MoviePage(browser)
    movie_page.find_by_top_series()

@allure.title("Переход на страницу онлайн-кинотеатра")
@allure.severity("critical")
def test_online_cinema(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    movie_page = MoviePage(browser)
    movie_page.get_online_cinema_button.click()

sleep(15)


