import allure
import pytest
from ui_pages import AuthPage, MainPage, SearchResultPage, ExtendedSearchPage, Top250Page


@pytest.mark.ui_test
@allure.title("Авторизация")
@allure.description("Тест на проверку авторизации")
@allure.feature("Auth")
@allure.severity("critical")
def test_auth(main_ui_page: MainPage, auth_ui_page: AuthPage, test_data: dict):
    main_ui_page.open()

    if auth_by_cookies := auth_ui_page.cookies_exists():
        auth_ui_page.load_cookies()
        main_ui_page.refresh()
    else:
        main_ui_page.open_auth_page()
        auth_ui_page.login(test_data.get("email"), test_data.get("password"))

    with allure.step("Проверка успешной авторизации"):
        assert main_ui_page.is_user_logged_in()

    if not auth_by_cookies:
        auth_ui_page.save_cookies()


@pytest.mark.ui_test
@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по названию")
@allure.feature("Title")
@allure.severity("critical")
def test_find_movie_by_title(main_ui_page: MainPage, search_ui_page: SearchResultPage):
    main_ui_page.open()

    main_ui_page.find_by_title("Чебурашка")
    with allure.step("Проверка, что карточка с результатом поиска существует"):
        assert search_ui_page.result_card_exist()
    main_ui_page.find_by_title("тмьдмт")
    with allure.step("Проверка, что карточка с результатом поиска не существует"):
        assert not search_ui_page.result_card_exist()


@pytest.mark.ui_test
@allure.title("Поиск коллекции фильмов")
@allure.description("Тест на поиск коллекции ТОП-250 фильмов")
@allure.feature("ТОП-250")
@allure.severity("major")
def test_find_top_250_movie(
    main_ui_page: MainPage,
    extended_search_ui_page: ExtendedSearchPage,
    top_250_ui_page: Top250Page
):
    main_ui_page.open()
    main_ui_page.open_extended_search()

    extended_search_ui_page.open_top_250_page()
    with allure.step("Проверка открытия страницы с заголовком топ 250"):
        assert top_250_ui_page.page_title_exists()
    with allure.step("Проверка соответствия текста заголовка страницы топ 250"):
        assert top_250_ui_page.get_page_title_text() == "250 лучших фильмов"


@pytest.mark.ui_test
@allure.title("Поиск коллекции сериалов")
@allure.description("Тест на поиск коллекции ТОП-250 сериалов")
@allure.feature("ТОП-250")
@allure.severity("major")
def test_find_top_250_series(
    main_ui_page: MainPage,
    extended_search_ui_page: ExtendedSearchPage,
    top_250_ui_page: Top250Page
):
    main_ui_page.open()
    main_ui_page.open_extended_search()

    extended_search_ui_page.open_top_250_page()
    top_250_ui_page.open_series()
    with allure.step("Проверка открытия страницы с заголовком топ 250"):
        assert top_250_ui_page.page_title_exists()
    with allure.step("Проверка соответствия текста заголовка страницы топ 250"):
        assert top_250_ui_page.get_page_title_text() == "250 лучших сериалов"


@pytest.mark.ui_test
@allure.title("Онлайн-кинотеатр")
@allure.description("Тест на переход в онлайн-кинотеатр")
@allure.feature("Online-cinema")
@allure.severity("critical")
def test_online_cinema(main_ui_page: MainPage):
    main_ui_page.open()
    main_ui_page.open_online_cinema_page()
    with allure.step("Проверка открытия страницы, url которой начинается https://hd.kinopoisk.ru/"):
        assert main_ui_page.get_current_url().startswith("https://hd.kinopoisk.ru/")


@pytest.mark.ui_test
@allure.title("Писк фильма")
@allure.description("Тест на поиск по году выпуска")
@allure.feature("Year")
@allure.severity("major")
def test_find_by_year(
    main_ui_page: MainPage,
    extended_search_ui_page: ExtendedSearchPage,
    search_ui_page: SearchResultPage
):
    main_ui_page.open()
    main_ui_page.open_extended_search()
    extended_search_ui_page.find_movies_by_year(2020)
    with allure.step("Проверка, что карточка с результатом поиска существует"):
        assert search_ui_page.result_card_exist()
    main_ui_page.open_extended_search()
    extended_search_ui_page.find_movies_by_year(1841)
    with allure.step("Проверка, что карточка с результатом поиска не существует"):
        assert not search_ui_page.result_card_exist()
