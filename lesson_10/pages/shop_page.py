from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:   
    #авторизация
    lgn = (By.ID, "user-name")
    pswrd = (By.ID, "password")
    lgn_btn = (By.ID, "login-button")

    #товары
    bpck_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    t_srt_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    onc_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
    chct_btn = (By.ID, "checkout")
    crt = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")

    #корзина
    crt = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")

   #форма
    frst_n = (By.ID, "first-name")
    lst_n = (By.ID, "last-name")
    z_c = (By.ID, "postal-code")

    cntn_btn = (By.ID, "continue")

#итоговая сумма
    prs = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("открытие страницы магазина")
    def opn_shop(self):
        """открываем страницу магазина"""
        self.driver.get(self.url)

    @allure.step("авторизация в магазине")
    def autch (self, driver):
        """авторизируемся в магазине"""
        login_i = WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.lgn)).send_keys("standard_user")

        pswrd_i = WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.pswrd)).send_keys("secret_sauce")
    
        lgn_b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.lgn_btn)).click()
    
    @allure.step("выбор товаров")
    def in_shop(self, driver):
        """выбираем товары"""
        b_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.bpck_btn))
        b_btn.click()

        t_srt_b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.t_srt_btn))
        t_srt_b.click()

        onc_b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.onc_btn))
        onc_b.click()

        crt_a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.crt))
        crt_a.click()
    
    @allure.step("работа с формой личных данных")
    def cart (self, driver):
        """нажимаем кнопку перехода форму личных данный"""
        chct_b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.chct_btn))
        chct_b.click()

    @allure.step("заполнение личных данных")
    def form (self, driver):
        """заполняем личные данные"""
        fn_i = WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.frst_n))
        fn_i.send_keys("Svetlana")

        ln_i = WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.lst_n))
        ln_i.send_keys("Krylova")

        z_i = WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.z_c))
        z_i.send_keys("420-0-29")

        cntn_b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.cntn_btn))
        cntn_b.click()

    @allure.step("получение конечной суммы")
    def summ (self, driver) -> str:
        """получение конечной суммы"""
        txt = WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.prs))
        return txt.text







