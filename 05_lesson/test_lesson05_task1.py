import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_les5 (): 
    try:
        driver = webdriver.Chrome()
        driver.get("https://httpbin.org/")
        time.sleep(15)

        cf = driver.find_element(By.LINK_TEXT, 'HTML form')
        cf.click()
        time.sleep(15)

        new_url = driver.current_url
        #print("Текущий URL:", new_url)
        assert new_url == "https://httpbin.org/forms/post"

        driver.back()
        time.sleep(15)
        old_url = driver.current_url
        #print("URL после возврата:", old_url)
        assert old_url == "https://httpbin.org/"

    except Exception as e:
        print("Произошла ошибка:", e)
    finally:
        driver.quit()

    time.sleep(15)
    driver.quit()

#test_les5()


