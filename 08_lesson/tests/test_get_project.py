
from pages.projectapi import ProjctApi

def test_get_positive():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.get_project("ba351ac5-f551-4e0f-aea3-81c9336ad780")    

    assert t[1] == 200, "Ожидался код 200, но пришло {t[1]}"

def test_get_empty():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.get_project("")    

    assert t[1] == 200, "Ожидался код 200, но пришло {t[1]}"    

def test_get_incorrect():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.get_project("666")    

    assert t[1] == 200, "Ожидался код 200, но пришло {t[1]}"
