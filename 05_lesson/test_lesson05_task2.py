import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_form_submission (): 
    try:
        driver = webdriver.Chrome()
        driver.get("https://httpbin.org/forms/post")
        time.sleep(15)

        driver.find_element(By.NAME, 'custname').send_keys("Sveta")
        s = driver.find_element(By.LINK_TEXT, 'Submit order')
        s.click()        
        time.sleep(15)

        new_url = driver.current_url
        #print("Текущий URL:", new_url)
        assert new_url == "https://httpbin.org/post"
       
    except Exception as e:
        print("Произошла ошибка:", e)
    finally:
        driver.quit()

    time.sleep(15)
    driver.quit()




