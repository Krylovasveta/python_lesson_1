from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(" https://gitflic.ru/")

    wait = WebDriverWait(driver, 10)

    driver.add_cookie({
      "name": "SESSION",
      "value": "YWYyNTk2MTEtODI4Mi00MTY3LThmYjAtOTVjODE3ZmIzMDdj",
      "domain": "gitflic.ru"
   })
    driver.add_cookie({
      "name": "cookiesAccepted",
      "value": "true",
      "domain": "gitflic.ru"
   })

    driver.refresh()

    driver.get("https://gitflic.ru/user/karr1")
    driver.refresh()

    url1 = driver.current_url
 
    u1 = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h6.mb-0"), "Sv1 K"
                                       )
    )                                   


    driver.delete_all_cookies()

    driver.refresh()

    driver.add_cookie({
      "name": "SESSION",
      "value": "NDUyMDI1N2EtZGYxMy00OTA0LTkzOTItNWJmYzE3OWM2ZmRm",
      "domain": "gitflic.ru"
   })
    driver.add_cookie({
      "name": "cookiesAccepted",
      "value": "true",
      "domain": "gitflic.ru"
   })

    driver.refresh()
   
    driver.get("https://gitflic.ru/user/kar2")
    driver.refresh()

    url2 = driver.current_url


    u2 = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h6.mb-0"), "Kar2"
                                       )
    )                                   

    assert url1 != url2
    
    driver.quit()

