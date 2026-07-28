from pages.shop_page import ShopPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest


def test_shop():   
    driver = webdriver.Firefox()
    driver.maximize_window() 
    shop_page = ShopPage(driver, "https://www.saucedemo.com/") 

#открытие страницы
    shop_page.opn_shop()
#авторизация
    shop_page.autch(driver) 
#в магазине
    shop_page.in_shop(driver)   
#в корзине
    shop_page.cart(driver)
#вводим данные для доставки
    shop_page.form(driver)   
#итоговая сумма
    p_s = shop_page.summ(driver)                                 

    assert p_s == "Total: $58.29", f"На экране : {p_s}"

    driver.quit
    


