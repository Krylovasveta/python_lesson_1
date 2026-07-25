from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_shop():
   
   driver = webdriver.Firefox()
   wait = WebDriverWait(driver, 10)   
   driver.get("https://www.saucedemo.com/")

#авторизация
   lgn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
   pswrd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
   lgn.send_keys("standard_user")
   pswrd.send_keys("secret_sauce")

   lgn_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
   lgn_btn.click()
         

#в магазине
   bpck_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
   bpck_btn.click()

   t_srt_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
   t_srt_btn.click()

   onc_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
   onc_btn.click()

   crt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")))
   crt.click()

   
#в корзине
   chct_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout")))
   chct_btn.click()
   

#вводим данные для доставки
   frst_n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name")))
   frst_n.send_keys("Svetlana")

   lst_n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last-name")))
   lst_n.send_keys("Krylova")

   z_c = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "postal-code")))
   z_c.send_keys("420-0-29")

   cntn_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "continue")))
   cntn_btn.click()

   
#итоговая сумма

   prs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
   
                              

   assert prs.text == "Total: $58.29", f"На экране : {prs.text}"

   driver.quit()

