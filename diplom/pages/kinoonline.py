from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class KinoOnline:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def onln(self):
        self.driver.get(self.url)

        hrf = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a[href="https://hd.kinopoisk.ru/"]'))
        )
        hrf.click()

        current_url = self.driver.current_url

        return current_url

    @allure.id("KinoOnline-0")
    @allure.title("Фильмы из онлайн-кинотеатра")
    @allure.severity("critical")
    def film_card(self) -> int:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Переходим на страницу кинотеатра"):
            hrf = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'a[href="https://hd.kinopoisk.ru/"]'))
            )
            hrf.click()

        with allure.step("Получаем адрес страницы"):
            current_url = self.driver.current_url

        return current_url

    @allure.id("KinoOnline-1")
    @allure.title("Карусель фильмов для онлайн-просмотра")
    @allure.severity("critical")
    def get_karusel(self) -> int:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Кликнуть по кнопке онлайкинотеатра"):
            link_element = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="https://hd.kinopoisk.ru/"]'))
            )
            link_element.click()

        with allure.step("Проверить url"):
            self.wait.until(
                lambda d: d.current_url == "https://hd.kinopoisk.ru/"
            )

        with allure.step("Проверить что отображаются несколько фильмов"):
            links = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'a[data-test-id="RouterLink"]'))
            )

        return len(links)

    @allure.id("KinoOnline-2")
    @allure.title("Проверка наличия кнопки Трейлер")
    @allure.severity("normal")
    def film_treil(self) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Открыть онлайн-кинотеатр"):
            link_element = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="https://hd.kinopoisk.ru/"]'))
            )
            link_element.click()
            self.wait.until(
                lambda d: d.current_url.startswith("https://hd.kinopoisk.ru")
            )

        with allure.step("Ожидаем появления фильмов"):
            films = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'a[data-test-id="RouterLink"]'))
            )
            film_url = None
            for film in films:
                href = film.get_attribute("href")
                if href and "onboarding" not in href:
                    film_url = href
                    break

        self.driver.get(film_url)
        self.wait.until(lambda d: d.current_url == film_url)

        with allure.step("Дождаться появления кнопки трейлера"):
            s = (
                By.CSS_SELECTOR, 'button[data-test-id="ContentActions_trailer"]'
            )
            flm_btn = self.wait.until(EC.presence_of_element_located(s))
            button_text = flm_btn.text

        return button_text

    @allure.id("KinoOnline-3")
    @allure.title("Проверка наличия кнопки Просмотр")
    @allure.severity("critical")
    def film_view(self) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Открыть онлайн-кинотеатр"):
            link_element = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="https://hd.kinopoisk.ru/"]'))
            )
            link_element.click()
            self.wait.until(
                lambda d: d.current_url.startswith("https://hd.kinopoisk.ru")
            )

        with allure.step("Дождаться появления фильмов"):
            films = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'a[data-test-id="RouterLink"]'))
            )
            film_url = None
            for film in films:
                href = film.get_attribute("href")
                if href and "onboarding" not in href:
                    film_url = href
                    break

        self.driver.get(film_url)
        self.wait.until(lambda d: d.current_url == film_url)

        with allure.step("Ждем измения url"):
            self.wait.until(
                lambda d: d.current_url != self.url
            )

        with allure.step("Дождаться появления кнопки просмотра"):
            flm_btn = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[data-test-id="MainButton_offer"]')))
            button_text = flm_btn.text

        return button_text
