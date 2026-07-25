from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
   driver = webdriver.Chrome()
   wait = WebDriverWait(driver, 50)   
   driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

   delay_inpt = wait.until(EC.element_to_be_clickable((By.ID, "delay")))
   delay_inpt.clear()
   delay_inpt.send_keys("45")

   btn_7 = wait.until(   EC.element_to_be_clickable( (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-primary') and text()='7']") ) )
   btn_7.click()

   btn_p = wait.until(      EC.element_to_be_clickable(        (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-success') and text()='+']")        )         )      
   btn_p.click()

   btn_8 = wait.until(      EC.element_to_be_clickable(        (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-primary') and text()='8']")         )         )
   btn_8.click()

   btn_r = wait.until(      EC.element_to_be_clickable(       (By.XPATH, "//span[contains(@class, 'btn') and contains(@class, 'btn-outline-warning') and text()='=']")        )        )
   btn_r.click()

   wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "div.screen").text == "15")

# Потом берём элемент отдельно, чтобы сделать assert
   scr = driver.find_element(By.CSS_SELECTOR, "div.screen")
   assert scr.text == "15", f"На экране : {scr.text}"

   driver.quit()

