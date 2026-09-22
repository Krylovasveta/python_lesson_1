from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class KINO:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @allure.id("Kino-1")
    @allure.title("Поиск фильма по названию")
    @allure.severity("critical")
    def srch_n(self, name) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ввести название фильма"):
            inpt_srch = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'kinopoisk-header-search-form-input__input'))
            )
            inpt_srch.clear()
            inpt_srch.send_keys(name)

        with allure.step("Кликнуть по кнопке Найти"):
            btn = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Найти"]'))
            )
            btn.click()

        with allure.step("Найти фильм"):
            ttl_loc = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span[data-tid="45f60312"]'))
            )
            t = ttl_loc.text

        return t

    @allure.id("Kino-2")
    @allure.title("Поиск режиссера")
    @allure.severity("normal")
    def srch_dir_crd(self, name='Томас Ян') -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ввести фамилию режиссера"):
            inpt_srch = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'kinopoisk-header-search-form-input__input'))
            )
            inpt_srch.clear()
            inpt_srch.send_keys(name)

        with allure.step("Кликнуть по кнопке Найти"):
            btn = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Найти"]'))
            )
            btn.click()

        search_query = name

        with allure.step("Получить карточку режиссера"):
            xpath_director = (
                f"//h2[contains(text(), 'Возможно, вы искали')]"
                f"/following::a[contains(text(), '{search_query}')]"
                f" | "
                f"//h2[contains(text(), 'Возможно, вы искали')]"
                f"/following::span[contains(text(), '{search_query}')]"
            )

            director_card = self.wait.until(
                EC.presence_of_element_located((By.XPATH, xpath_director))
            )

        return director_card.text

    @allure.id("Kino-3")
    @allure.title("Поиск фильмов по режиссеру")
    @allure.severity("normal")
    def srch_dir_films(self, name) -> str:
        with allure.step("Открыть страницу Кинопоиска"):
            self.driver.get(self.url)

        with allure.step("Ввести название фильма"):
            inpt_srch = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'kinopoisk-header-search-form-input__input'))
            )
            inpt_srch.clear()
            inpt_srch.send_keys(name)

        with allure.step("Кликнуть по кнопке Найти"):
            btn = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Найти"]'))
            )
            btn.click()

        with allure.step("Кликнуть по кнопке Найти"):
            section = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'section[data-testid="search-films"]'))
            )
            items = section.find_elements(
                By.CSS_SELECTOR, '[data-test-id="movie-list-item"]')

        films = []
        for item in items:
            title = item.find_element(
                By.CSS_SELECTOR, 'span[data-tid="45f60312"]').text
            films.append(title)

        return films
