
from pages.projectapi import ProjctApi

def test_create_positive():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.create_project("Test project 6")
    assert len (t[0]) > 0
    assert t[1] == 201, "Ожидался код 201, но пришло {t[1]}"

def test_create_empty():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.create_project("")
    assert len (t[0]) > 0
    assert t[1] == 201, "Ожидался код 201, но пришло {t[1]}"


