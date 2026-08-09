from pages.db import Db


def test_add():
    db = Db()
    e = "sveta@mail.ru"
    db.add_usr(3, e, 1)
    p = db.sel_usr(e)
    assert p[0]["user_email"] == e


def test_edt():
    db = Db()
    e1 = "sveta@mail.ru"
    db.add_usr(3, e1, 1)
    e = "sveta1@mail.ru"
    db.edit_usr(3, e)
    p = db.sel_usr(e)
    assert p[0]["user_email"] == e


def test_d():
    db = Db()
    e = "sveta@mail.ru"
    db.add_usr(3, e, 1)
    db.del_usr(3)
    p = db.sel_usr(e)
    assert len(p) == 0
