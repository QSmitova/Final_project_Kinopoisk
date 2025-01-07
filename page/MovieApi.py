import requests
import allure
from page.apikey import KEY, VALUE #эти данные внесены в список test_data.json. Как их вытащить оттуда сюда,
                                   # чтобы файл apikey удалить?
                                   # и headers в каждом тесте, тоже бы в порядок привести
# "Content-Type": "application/json" нужно передавать в get запросах?

class MovieApi:
    def __init__(self):
        self.key = KEY
        self.value = VALUE
        self.base_url = "https://api.kinopoisk.dev/v1.4/movie/"

    @allure.step("Поиск фильма по названию")
    def get_movie_by_title(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        name = "%D0%A7%D0%B5%D0%B1%D1%83%D1%80%D0%B0%D1%88%D0%BA%D0%B0"
        resp = requests.get(self.base_url + 'search' + '?page=1&limit=10&query=' + name, headers = headers)
        return resp.json()
    #почему подчеркивает желтым requests?
    #нужно написать проверку, вывести список найденных фильмов, наверное.

    @allure.step("Поиск фильма по ID")
    def get_movie_by_id(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        id = "1402937"
        resp = requests.get(self.base_url + id, headers = headers)
        return resp.json()
    # нужно написать проверку, вывести список найденных фильмов, наверное.

    @allure.step("Поиск фильма по рейтингу Кинопоиска")
    def get_movie_by_rating_kp(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        rating = "8-10"
        resp = requests.get(self.base_url + '?rating.kp=' + rating, headers = headers)
        return resp.json()
        #нужно написать проверку, вывести список найденных фильмов, наверное.

    @allure.step("Поиск фильма по жанру")
    def get_movie_by_genre(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        genre = "драма"
        resp = requests.get(self.base_url + '?genres.name=' + genre, headers=headers)
        return resp.json()
    # нужно написать проверку, вывести список найденных фильмов, наверное.

    @allure.step("Поиск фильма по коллекциям")
    def get_movie_by_collection(self):
        headers = {
            "Key": self.key,
            "Value": self.value,
            "Content-Type": "application/json"
        }
        collection = "top250"
        resp = requests.get(self.base_url + '?lists=' + collection, headers=headers)
        return resp.json()
    # нужно написать проверку, вывести список найденных фильмов, наверное.

    #как бы вынести все вводные данные (названия, рейтинг и т.д.) куда-то наверх, чтобы легко было менять эти тестовые данные?