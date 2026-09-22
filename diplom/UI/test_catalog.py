import allure


@allure.step("Проверка открытия страницу магазина")
def test_ui_menu_shop(kino_menu_inst):
    kn_shop_page = kino_menu_inst.shop()
    assert kn_shop_page == "https://hd.kinopoisk.ru/buy"


@allure.step("Проверка открытия страницу подписок")
def test_ui_menu_podpiski(kino_menu_inst):
    kn_podpiski_page = kino_menu_inst.podpiski()
    assert kn_podpiski_page == "https://hd.kinopoisk.ru/promo"


@allure.step("Проверка открытия страницу каналы")
def test_ui_menu_channels(kino_menu_inst):
    kn_channels_page = kino_menu_inst.channels()
    assert kn_channels_page == "https://hd.kinopoisk.ru/channels"


@allure.step("Проверка открытия страницу спорт")
def test_ui_menu_sport(kino_menu_inst):
    kn_sport_page = kino_menu_inst.sport()
    assert kn_sport_page == "https://hd.kinopoisk.ru/sport/"
