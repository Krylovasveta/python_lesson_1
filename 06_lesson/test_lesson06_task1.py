from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
   driver = webdriver.Chrome()
   wait = WebDriverWait(driver, 10)
   
   driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

   btn=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']")))
   btn.click()
   #"//div[@id='start']//button[contains(text(), 'Start')]".

   element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']")))
   driver.save_screenshot("screenshots/page.png")
   
   assert element.text == "Hello World!"
   
   driver.quit()
