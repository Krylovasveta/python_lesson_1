from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cals_page import CalsPage
import pytest
import allure

@allure.feature("сумма")
@allure.severity("critical")
@allure.title("Проверка работы калькулятора")
@allure.description("Вызов калькулятора, сложение двух числе, проверка результата вычисления")
def test_calc():
    """проверка результата вычисления"""
    driver = webdriver.Firefox()
    driver.maximize_window()    
    cals_page = CalsPage(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  
    cals_page.opn_cals()

    with allure.step("устанавливаем задержку"):
        cals_page.delay(45) 

    with allure.step("нажимаем на кнопки калькулятора"):
        cals_page.btn_clck(CalsPage.btn_7)
        cals_page.btn_clck(CalsPage.btn_p)
        cals_page.btn_clck(CalsPage.btn_8)
        cals_page.btn_clck(CalsPage.btn_r)

    with allure.step("получаем результат вычисления"):
        result_text = cals_page.get_result()                                 

    with allure.step("сверяем ожидаемый результат с фактическим"):
        assert result_text == '15', f"На экране : {result_text}"   

    driver.quit() 
