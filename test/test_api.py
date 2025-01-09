from page.movie_api import MovieApi
import allure


@allure.title("Тест на поиск фильма по названию")
@allure.severity("critical")
def test_get_movie_by_title(movie_api:MovieApi):
    print(movie_api.get_movie_by_title("Чебурашка"))

@allure.title("Тест на поиск фильма по ID")
@allure.severity("critical")
def test_get_movie_by_id(movie_api:MovieApi):
    movie_api.get_movie_by_id(1402937)

@allure.title("Тест на поиск фильма по рейтингу Кинопоиска")
@allure.severity("critical")
def test_get_movie_by_rating(movie_api:MovieApi):
    movie_api.get_movie_by_rating_kp("8-10")

@allure.title("Тест на поиск фильма по жанру")
@allure.severity("critical")
def test_get_movie_by_genre(movie_api:MovieApi):
    movie_api.get_movie_by_genre("Драма")

@allure.title("Тест на поиск фильма по коллекциям")
@allure.severity("critical")
def test_get_movie_by_collection(movie_api:MovieApi):
    movie_api.get_movie_by_collection("top250")
