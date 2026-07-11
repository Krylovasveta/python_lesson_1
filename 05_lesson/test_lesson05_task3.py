import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_multiple_elements (): 
    try:
        driver = webdriver.Chrome()
        driver.get("https://httpbin.org/links/10")
        time.sleep(15)

        l = driver.find_elements(By.TAG_NAME, 'a')  
        assert len(l) == 9

        for li in l:
            assert li.is_displayed(), f"Ссылка {li.text} не отображается на странице."

        assert "1" in l[0].text, f"Ожидался текст '1' в первой ссылке, но найдено: {l[0].text}"

        
    except Exception as e:
        print("Произошла ошибка:", e)
    finally:
        driver.quit()

    time.sleep(15)
    driver.quit()




