import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPhrases(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
        self.driver.maximize_window()

    def authorization(self):
        driver = self.driver
        driver.implicitly_wait(10)  # неявное ожидание появления элемента
        driver.get("https://dev.marketpapa.ru/login")  # переход на страницу авторизации
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/input").click()  # клик на поле ввода номера телефона
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").send_keys("9877120164")  # поиск поля ввода номера телефона и вставка
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/input").send_keys("q1w2e3r4t5y6")  # поиск поля пароля и вставка
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/span').click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a[2]").click()
        return driver

    def test_phrases(self):
        driver = TestPhrases.authorization(self)
        driver.get("https://dev.marketpapa.ru/phrases")
        driver.find_element(By.NAME, "articul").send_keys("74322224")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/input").send_keys("носки", Keys.RETURN)
        # TESTS
        id_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[1]/span").is_displayed()
        assert id_category == True, "Не отображается элемент Id категории в подборе фраз"
        category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/span").is_displayed()
        assert category == True, "Не отображается элемент 'Категории' в подборе фраз"
        delivery_time = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[3]/span").is_displayed()
        assert delivery_time == True, "Не отображается элемент 'Срок доставки' в подборе фраз"
        frequency_per_month = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span").is_displayed()
        assert frequency_per_month == True, "Не отображается частотность за месяц в подборе фраз"
        frequency_per_day = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/span").is_displayed()
        assert frequency_per_day == True, "Не отображается частотность за день в подборе фраз"
        first_phrase = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div/div/div").is_displayed()
        assert first_phrase == True, "Не отображается фраза в подборе фраз"
        id_priority_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/div/div/div[1]/span").is_displayed()
        assert id_priority_category == True, "Не отображается Id приоритетной категории в подборе фраз"
        max_delivery_time = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/div").is_displayed()
        assert max_delivery_time == True, "Не отображается максимальное время доставки в подборе фраз"
        first_place = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[5]").is_displayed()
        assert first_place == True, "Не отображается первое место в таблице в подборе фраз"

    def tearDown(self):
        self.driver.close()