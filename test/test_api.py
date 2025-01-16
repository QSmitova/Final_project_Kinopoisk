import pytest
from api.movie_api import MovieApi
import allure


@pytest.mark.api_test
@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по названию")
@allure.feature("Title")
@allure.severity("critical")
def test_get_movie_by_title(movie_api: MovieApi):
    movies, status_code = movie_api.get_movie_by_title("Чебурашка")
    assert status_code == 200
    assert "чебурашка" in [movie["name"].lower() for movie in movies]


@pytest.mark.api_test
@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по ID")
@allure.feature("ID")
@allure.severity("critical")
def test_get_movie_by_id(movie_api: MovieApi):
    movie, status_code = movie_api.get_movie_by_id(1402937)
    assert status_code == 200
    assert movie["id"] == 1402937


@pytest.mark.api_test
@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по рейтингу Кинопоиска")
@allure.feature("Rating")
@allure.severity("critical")
def test_get_movie_by_rating(movie_api: MovieApi):
    movies, status_code = movie_api.get_movie_by_rating_kp("8-10")
    assert status_code == 200
    assert "у края бездны" in [movie["name"].lower() for movie in movies]


@pytest.mark.api_test
@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по жанру")
@allure.feature("Genre")
@allure.severity("critical")
def test_get_movie_by_genre(movie_api: MovieApi):
    movies, status_code = movie_api.get_movie_by_genre("драма")
    assert status_code == 200
    assert 6975484 in [movie["id"] for movie in movies]


@pytest.mark.api_test
@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по коллекциям")
@allure.feature("Collection")
@allure.severity("critical")
def test_get_movie_by_collection(movie_api: MovieApi):
    movies, status_code = movie_api.get_movie_by_collection("top250")
    assert status_code == 200
    assert 1402937 in [movie["id"] for movie in movies]
