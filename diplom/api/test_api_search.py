import requests
import allure
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

base_url = "https://api.poiskkino.dev/v1.5/movie"
my_head = {"X-API-KEY": API_TOKEN}


@allure.step("Поиск фильма по названию")
def test_get_film_by_name():
    with allure.step("Отправка запроса на поиск фильма по имени"):
        f = requests.get(
            base_url + "/search?query='Достучаться до небес'", headers=my_head
        )
    with allure.step("Перевод ответа в формат json"):
        resp_data = f.json()

    with allure.step("Проверка кода ответа"):
        assert f.status_code == 200
    with allure.step("Проверка названия первого фильма списка"):
        first_film_name = resp_data["docs"][0]["names"][0]["name"]
        assert first_film_name == "Knockin' on Heaven's Door"

    return resp_data


@allure.step("Поиск фильмов по жанру")
def test_get_film_by_genre():
    with allure.step("Отправка запроса на поиск фильма по жанру"):
        f = requests.get(base_url + "?genres.name=криминал", headers=my_head)
    with allure.step("Перевод ответа в формат json"):
        resp_data = f.json()

    with allure.step("Проверка кода ответа"):
        assert f.status_code == 200
    with allure.step("Проверка названия первого фильма списка"):
        first_film = resp_data["docs"][0]
        first_film_name = first_film["names"][0]["name"]
    with allure.step("Проверка количества фильмов списка"):
        assert len(first_film_name) > 0
        assert len(resp_data.get("docs", [])) > 0

    return resp_data


@allure.step("Поиск фильма по году выпуска")
def test_get_film_by_year():
    with allure.step("Отправка запроса на поиск фильма по году выпуска"):
        f = requests.get(base_url + "?year=2026", headers=my_head)
    with allure.step("Перевод ответа в формат json"):
        resp_data = f.json()

    with allure.step("Проверка кода ответа"):
        assert f.status_code == 200
    with allure.step("Проверка названия первого фильма списка"):
        first_film = resp_data["docs"][0]
        first_film_name = first_film["names"][0]["name"]
    with allure.step("Проверка количества фильмов списка"):
        assert len(first_film_name) > 0
        assert len(resp_data.get("docs", [])) > 0

    return resp_data


@allure.step("Поиск фильма по некорректному названию")
def test_get_film_by_incorrect_name():
    with allure.step("Запрос на поиск фильма по некорректному названию"):
        f = requests.get(base_url + "/search?query='@6mlg'", headers=my_head)

    with allure.step("Перевод ответа в формат json"):
        resp_data = f.json()

    with allure.step("Проверка кода ответа"):
        assert f.status_code == 200
    with allure.step("Проверка количества фильмов списка"):
        assert len(resp_data.get("docs", [])) == 0

    return resp_data
