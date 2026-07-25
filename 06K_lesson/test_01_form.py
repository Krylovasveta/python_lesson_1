from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_update_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
     
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


    fn = wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
    fn.clear()
    fn.send_keys("Иван")
   

    fl = wait.until(EC.presence_of_element_located((By.NAME, "last-name")))
    fl.clear()
    fl.send_keys("Петров")
   
    a = wait.until(EC.presence_of_element_located((By.NAME, "address")))
    a.clear()
    a.send_keys("Ленина, 55-3")
    

    eml = wait.until(EC.presence_of_element_located((By.NAME, "e-mail")))
    eml.clear()
    eml.send_keys("test@skypro.com")
   

    phn = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
    phn.clear()
    phn.send_keys("+7985899998787")
  

    z = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    z.clear()    
  

    ct = wait.until(EC.presence_of_element_located((By.NAME, "city")))
    ct.clear()
    ct.send_keys("Москва")
 

    cntr = wait.until(EC.presence_of_element_located((By.NAME, "country")))
    cntr.clear()
    cntr.send_keys("Россия")
  

    jb = wait.until(EC.presence_of_element_located((By.NAME, "job-position")))
    jb.clear()
    jb.send_keys("QA")
  

    cmpn = wait.until(EC.presence_of_element_located((By.NAME, "company")))
    cmpn.clear()
    cmpn.send_keys("SkyPro")
    
    
    btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-outline-primary")))
    btn.click()

     # 1. Проверка zip-code: должен быть alert-danger
    zip_elem = driver.find_element(By.ID, "zip-code")
    zip_classes = zip_elem.get_attribute("class").split() 
    assert "alert-danger" in zip_classes, f"Для zip-code ожидался alert-danger, но найдено: {zip_classes}"
    
    # 2. Проверка остальных полей: должны быть alert-success
    success_fields = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company",
    ]

    for field_id in success_fields:
        elem = driver.find_element(By.ID, field_id)
        classes = elem.get_attribute("class").split()
        assert "alert-success" in classes, f"Поле {field_id} не подсвечено как alert-success: {classes}"
             

   

    driver.quit()

