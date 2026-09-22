import pytest
from selenium import webdriver
from pages.kino import KINO
from pages.kinoonline import KinoOnline
from pages.catalog import Catalog


@pytest.fixture
def kino_inst():
    """
    Фикстура открывает браузер
    Создает экземпляр класса Kinoonline
    Закрывает браузер
    """
    driver = webdriver.Chrome()
    url = "https://www.kinopoisk.ru/"

    instance = KINO(url, driver)

    yield instance
    driver.quit()


@pytest.fixture
def kino_online_inst():
    """
    Фикстура открывает браузер
    Создает экземпляр класса Kino
    Закрывает браузер
    """
    driver = webdriver.Chrome()
    url = "https://www.kinopoisk.ru/"
    instance = KinoOnline(url, driver)

    yield instance
    driver.quit()


@pytest.fixture
def kino_menu_inst():
    """
    Фикстура открывает браузер
    Создает экземпляр класса Catalog
    Закрывает браузер
    """
    driver = webdriver.Chrome()
    url = "https://hd.kinopoisk.ru/"

    instance = Catalog(url, driver)

    yield instance
    driver.quit()
