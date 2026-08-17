from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalsPage:
  
    delay_inpt = (By.ID, "delay")  
    btn_7 = (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-primary') and text()='7']") 
    btn_p = (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-success') and text()='+']")
    btn_8 = (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-primary') and text()='8']")
    btn_r = (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-warning') and text()='=']")
    scr = (By.CSS_SELECTOR, "div.screen")      

  
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def opn_cals(self): 
        """открываем страницу калькулятора"""   
        self.driver.get(self.url)

    def delay(self, w : int):
        """настраиваем паузу"""
        wait = WebDriverWait(self.driver, 10)
        delay_input = wait.until(EC.element_to_be_clickable(self.delay_inpt))
        delay_input.clear()
        delay_input.send_keys(w)

    def btn_clck(self,  btn):
        """нажимаем кнопки калькулятора"""
        wait = WebDriverWait(self.driver, 1)
        b = wait.until(   EC.element_to_be_clickable(btn) )
        b.click()

    def get_result(self) -> str : 
        """работаем с экраном калькулятора"""
        wait = WebDriverWait(self.driver, 47)       
        wait.until(
             lambda d: d.find_element(By.CSS_SELECTOR, "div.screen").text == "15")

        element = self.driver.find_element(By.CSS_SELECTOR, "div.screen")
            
        return element.text



