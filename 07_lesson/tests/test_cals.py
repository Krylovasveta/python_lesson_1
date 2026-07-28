from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cals_page import CalsPage
import pytest


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()    
    cals_page = CalsPage(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  
    cals_page.opn_cals()

    cals_page.delay(45) 

    cals_page.btn_clck(CalsPage.btn_7)
    cals_page.btn_clck(CalsPage.btn_p)
    cals_page.btn_clck(CalsPage.btn_8)
    cals_page.btn_clck(CalsPage.btn_r)

    result_text = cals_page.get_result()                                 

    assert result_text == '15', f"На экране : {result_text}"   

    driver.quit() 
