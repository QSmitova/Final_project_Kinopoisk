from time import sleep
import allure
from page.AuthPage import AuthPage
from page.MoviePage import MoviePage


@allure.title("Тест на проверку авторизации")
@allure.severity("critical")
def test_auth(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)
    #какой assert сделать на проверку авторизации?

    #избегать авторизации в начале каждого теста. Для этого на странице сайта нужно подложить в куки токен авторизации
    #как это сделать?

@allure.title("Тест на поиск фильма по названию")
@allure.severity("critical")
def test_find_movie_by_title(browser, test_data:dict):
    email = test_data.get("email") #это из теста убрать, потом учто вынесено в файле test_data.json
    password = test_data.get("password") #это из теста убрать, потом учто вынесено в файле test_data.json
    title = "Чебурашка"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    movie_page = MoviePage(browser)
    movie_page.find_by_title(title)

@allure.title("Тест на поиск коллекции ТОП-250 фильмов")
@allure.severity("major")
def test_find_top_250_movie(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    movie_page = MoviePage(browser)
    movie_page.find_by_top_movie()

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
    movie_page.online_cinema()

sleep(15)


