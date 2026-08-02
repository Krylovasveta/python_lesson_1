from pages.projectapi import ProjctApi

def test_update_positive():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.update_project("ba351ac5-f551-4e0f-aea3-81c9336ad780", "666 Test project 6")    

    assert t[1] == 200, "Ожидался код 200, но пришло {t[1]}"

def test_update_empty():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.update_project("", "666 Test project 6")    

    assert t[1] == 200, "Ожидался код 200, но пришло {t[1]}"

def test_update_incorr():

    api = ProjctApi("https://ru.yougile.com/api-v2")
    t = api.update_project("666", "666 Test project 6")
    
    assert t[1] == 200, "Ожидался код 200, но пришло {t[1]}"


