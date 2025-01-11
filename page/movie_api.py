import requests
import allure
from urllib.parse import quote


class MovieApi:
    def __init__(self, key:str, value:str):
        self.base_url = "https://api.kinopoisk.dev/v1.4/movie/"
        self.headers = {
           key:value
        }

    @allure.step("Поиск фильма по названию")
    def get_movie_by_title(self, name:str) -> list:
        name = quote(name)
        resp = requests.get(f'{self.base_url}search?query={name}', headers=self.headers)
        return resp.json().get("docs")

    @allure.step("Поиск фильма по ID")
    def get_movie_by_id(self, movie_id:int) -> dict:
        resp = requests.get(f'{self.base_url}{movie_id}', headers=self.headers)
        return resp.json()

    @allure.step("Поиск фильма по рейтингу Кинопоиска")
    def get_movie_by_rating_kp(self, rating:str) -> list:
        resp = requests.get(f'{self.base_url}?rating.kp={rating}', headers=self.headers)
        return resp.json().get("docs")

    @allure.step("Поиск фильма по жанру")
    def get_movie_by_genre(self,genre:str) -> list:
        resp = requests.get(f'{self.base_url}?genres.name={genre}', headers=self.headers)
        return resp.json().get("docs")

    @allure.step("Поиск фильма по коллекциям")
    def get_movie_by_collection(self, collection:str) -> list:
        resp = requests.get(f'{self.base_url}?lists={collection}', headers=self.headers)
        return resp.json().get("docs")
