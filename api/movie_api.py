import requests
import allure
from urllib.parse import quote


class MovieApi:
    """ Класс для взаимодействия с API api.kinopoisk.dev """
    def __init__(self, api_token: str):
        self.base_url = "https://api.kinopoisk.dev/v1.4/movie"
        self.headers = {
           "X-API-KEY": api_token
        }

    def get_movie_list(self, request: str) -> tuple[list, int]:
        request_str = f'{self.base_url}{request}'

        with allure.step(f"Делаем запрос к api кинопоиска: {request_str}"):
            resp = requests.get(request_str, headers=self.headers)
            return resp.json().get("docs"), resp.status_code

    @allure.step("Поиск фильма по названию")
    def get_movie_by_title(self, name: str) -> tuple[list, int]:
        name = quote(name)
        return self.get_movie_list(f"/search?query={name}")

    @allure.step("Поиск фильма по рейтингу Кинопоиска")
    def get_movie_by_rating_kp(self, rating: str) -> tuple[list, int]:
        return self.get_movie_list(f"?rating.kp={rating}")

    @allure.step("Поиск фильма по жанру")
    def get_movie_by_genre(self,genre: str) -> tuple[list, int]:
        return self.get_movie_list(f"?genres.name={genre}")

    @allure.step("Поиск фильма по коллекциям")
    def get_movie_by_collection(self, collection: str) -> tuple[list, int]:
        return self.get_movie_list(f"?lists={collection}")

    @allure.step("Поиск фильма по ID")
    def get_movie_by_id(self, movie_id: int) -> tuple[dict, int]:
        request_str = f'{self.base_url}/{movie_id}'

        with allure.step(f"Делаем запрос к api кинопоиска: {request_str}"):
            resp = requests.get(request_str, headers=self.headers)
            return resp.json(), resp.status_code