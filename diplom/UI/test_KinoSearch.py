import allure


@allure.step("Поиск фильма по названию")
def test_ui_search_by_name(kino_inst):
    namet = "Достучаться до небес"

    film_name = kino_inst.srch_n(namet)
    assert film_name == namet


@allure.step("Поиск режиссера")
def test_ui_search_card_by_dir_name(kino_inst):
    namet = "Такеши Китано"

    dir_name = kino_inst.srch_dir_crd(namet)
    assert dir_name == namet


@allure.step("Поиск фильмов по режиссеру")
def test_ui_search_films_by_dir_name(kino_inst):
    namet = "Такеши Китано"

    flms = kino_inst.srch_dir_films(namet)
    assert len(flms) > 0
