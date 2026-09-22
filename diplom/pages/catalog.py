from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Catalog:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.id("catalog-1")
    @allure.title("Открыть магазин")
    @allure.severity("critical")
    def shop(self) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ждем пока исчезнет баннер"):
            self.wait.until(EC.invisibility_of_element_located(
                (By.CLASS_NAME, "ReactModal__Overlay"))
            )

        with allure.step("Перейти на страницу на магазина"):
            shop_xpath = '//a[@href="/buy"]'
            shop_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, shop_xpath))
             )
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", shop_link
            )
            self.driver.execute_script("arguments[0].click();", shop_link)

        self.wait.until(EC.url_contains("/buy"))

        with allure.step("Получаем url"):
            current_url = self.driver.current_url
        return current_url

    @allure.id("catalog-2")
    @allure.title("Открыть подписки")
    @allure.severity("normal")
    def podpiski(self) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ждем пока исчезнет баннер"):
            self.wait.until(EC.invisibility_of_element_located(
                (By.CLASS_NAME, "ReactModal__Overlay"))
            )

        with allure.step("Открыть страницу подписок"):
            shop_link = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="/promo"]'))
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", shop_link
            )
            self.driver.execute_script("arguments[0].click();", shop_link)

        self.wait.until(EC.url_contains("/promo"))

        with allure.step("Получаем url"):
            current_url = self.driver.current_url
        return current_url

    @allure.id("catalog-3")
    @allure.title("Открыть каналы")
    @allure.severity("normal")
    def channels(self) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ждем пока исчезнет баннер"):
            self.wait.until(EC.invisibility_of_element_located(
                (By.CLASS_NAME, "ReactModal__Overlay"))
            )

        with allure.step("Открыть страницу с каналами"):
            shop_link = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="/channels"]'))
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", shop_link
            )
            self.driver.execute_script("arguments[0].click();", shop_link)

        self.wait.until(EC.url_contains("/channels"))

        with allure.step("Получаем url"):
            current_url = self.driver.current_url
        return current_url

    @allure.id("catalog-4")
    @allure.title("Открыть спорт")
    @allure.severity("normal")
    def sport(self) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ждем пока исчезнет баннер"):
            self.wait.until(EC.invisibility_of_element_located(
                (By.CLASS_NAME, "ReactModal__Overlay"))
            )
            self.wait.until(EC.invisibility_of_element_located(
                (By.CLASS_NAME, "styles_overlay__tXZ2e"))
            )

        with allure.step("Открыть страницу спорта"):
            sport_link = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//a[.//div[contains(text(),"Спорт")]]'))
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", sport_link
            )
            self.driver.execute_script(
                "arguments[0].click();", sport_link
            )

        with allure.step("Убедиться что переход осуществлен"):
            self.wait.until(
                lambda d: d.current_url == "https://hd.kinopoisk.ru/sport/"
            )

        with allure.step("Получаем url"):
            current_url = self.driver.current_url
        return current_url
