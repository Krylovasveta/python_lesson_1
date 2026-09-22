import allure


@allure.step("Открываем карусель фильмов онлайн-кинотеатра")
def test_karusel(kino_online_inst):
    kar = kino_online_inst.get_karusel()
    assert kar > 0


@allure.step("Проверяем url онлайн-кинотеатра")
def test_ui_opn_online(kino_online_inst):
    kn_onln_page = kino_online_inst.onln()
    assert kn_onln_page == "https://hd.kinopoisk.ru/"


@allure.step("Проверяем длину url онлайн-кинотеатра")
def test_film_card(kino_online_inst):
    is_film = kino_online_inst.film_card()
    assert len(is_film) > 0


@allure.step("Проверяем наличия кнопки трейлера")
def test_film_treil(kino_online_inst):
    btn = kino_online_inst.film_treil()
    assert btn == "Трейлер"


@allure.step("Проверяем наличия кнопки просмотра")
def test_film_view(kino_online_inst):
    btn = kino_online_inst.film_view()
    assert btn == "Смотреть фильм"
