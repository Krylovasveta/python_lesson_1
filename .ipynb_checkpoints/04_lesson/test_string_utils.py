from string_utils import StringUtils
import pytest

@pytest.mark.parametrize('s1, rez', [
    ('hello', 'Hello'),
    ('   hello', '   Hello'),
    ('today is 05/07/2026', 'Today is 05/07/2026'),
    ('1. today is 05/07/2026', '1. today is 05/07/2026'),
    ('hi, i am Sveta', 'Hi, i am Sveta')
    ])
def test_capitalize_positive(s1, rez):
    s = StringUtils()
    p = s.capitalize(s1)
    assert p == rez


@pytest.mark.parametrize('s1, rez', [
    ('', ''),
    (' ', ' '),    
    (None, None)
    ])
def test_capitalize_null(s1, rez):
    s = StringUtils()
    if s1 is None:
        with pytest.raises(TypeError):  # Проверка на ошибку для None
            s.capitalize(s1)
    else:
        p = s.capitalize(s1)
        assert p == s1

@pytest.mark.parametrize('s1, rez', [
    ('1', '1'),
    ('44 5 897', '44 5 897'),    
    ('this_is_a_test', 'This_is_a_test')
    ])
def test_capitalize_negative(s1, rez):
    s = StringUtils()
    p = s.capitalize(s1) 
    assert p == rez

@pytest.mark.parametrize('s1, rez', [
    (' hello', 'hello'),
    (' today is 05/07/2026', 'today is 05/07/2026'),
    (' 1. today is 05/07/2026', '1. today is 05/07/2026'),
    ('   multiple spaces', 'multiple spaces'),
    (' hi, i am Sveta', 'hi, i am Sveta')
    ])
def test_trim_positive(s1, rez):
    s = StringUtils()
    p = s.trim(s1)
    assert p == rez


@pytest.mark.parametrize('s1, rez', [
    ('', ''),
    (' ', ''),    
    (None, None)
    ])
def test_trim_null(s1, rez):
    s = StringUtils()
    if s1 is None:
        with pytest.raises(TypeError):  # Проверка на ошибку для None
            s.trim(s1)
    else:
        p = s.trim(s1)
        assert p == rez

@pytest.mark.parametrize('s1, rez', [
    ('  ', ' '),
    (' 44 5 897', '44 5 897'),    
    (' .- hj', '.- hj')
    ])
def test_trim_negative(s1, rez):
    s = StringUtils()
    p = s.trim(s1) 
    assert p == rez

@pytest.mark.parametrize('s1, s2, rez', [
    ('hello', 'e', True),
    ('Hello', 'H', True),
    ('today is 05/07/2026', '5',  True ),
    ('1. today is 05/07/2026', '/', True),
    ('hi, i am Olj', 'j',  True),
    ('hi, i am Sveta', 'h',  True)
    ])
def test_contains_positive(s1, s2, rez):
    s = StringUtils()
    p = s.contains(s1, s2)
    assert p == rez


@pytest.mark.parametrize('s1, s2, rez', [
    ('', 's', False),
    (' ', 'l', False),  
    (None, 's', False),  
    ('Hello! I am from Kazan.', '', True),   
    ('Hello! I am from Kazan.', ' ', True)
    ])
def test_contains_null(s1, s2, rez):
    s = StringUtils()
    if s1 is None or s2 is None:
        with pytest.raises(TypeError):
            s.contains(s1, s2)
    else:
        p = s.contains(s1, s2)
        assert p == rez

@pytest.mark.parametrize('s1,s2, rez', [
    ('Hello, i am Sveta', 'X', False),
    (' 44 5 897', '6', False),    
    (' .- hj', '!', False)
    ])
def test_contains_negative(s1,s2, rez):
    s = StringUtils()
    p = s.contains(s1, s2) 
    assert p == rez




@pytest.mark.parametrize('s1, s2, rez', [
    ('hello', 'e', 'hllo'),
    ('Hello', 'H', 'ello'),
    ('today is 05/07/2026', '5',  'today is 0/07/2026' ),
    ('1. today is 05/07/2026', '/', '1. today is 05072026'),
    ('hi, i am Olj', 'j',  'hi, i am Ol'),
    ('aabbcc', 'a', 'bbcc'),
    ('hi, i am Sveta', 'h',  'hi, i m Svet')
    ])
def test_delete_positive(s1, s2, rez):
    s = StringUtils()
    p = s.delete_symbol(s1, s2)
    assert p == rez


@pytest.mark.parametrize('s1, s2, rez', [
    ('', 's', ''),
    (' ', 'l', ' '),  
    (None, 's', None), 
    ('Hello! I am from Kazan.', '', 'Hello! I am from Kazan.'),   
    ('Hello! I am from Kazan.', ' ', 'Hello!IamfromKazan.')
    ])
def test_delete_null(s1, s2, rez):
    s = StringUtils()
    if s1 is None or s2 is None:
        with pytest.raises(TypeError):  # Ожидаем ошибку для None
            s.delete_symbol(s1, s2)
    else:
        p = s.delete_symbol(s1, s2)
        assert p == rez

@pytest.mark.parametrize('s1,s2, rez', [
    ('Hello, i am Sveta', 'X', 'Hello, i am Sveta'),
    (' 44 5 897', '6', ' 44 5 897'),        
    (' .- hj', '!', ' .- hj')
    ])
def test_delete_negative(s1,s2, rez):
    s = StringUtils()
    p = s.delete_symbol(s1, s2) 
    assert p == rez

