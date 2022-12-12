import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActualRates(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
        self.driver.maximize_window()

    def authorization(self):
        driver = self.driver
        driver.implicitly_wait(10)  # неявное ожидание появления элемента
        driver.get("https://dev.marketpapa.ru/login")  # переход на страницу авторизации
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").click()  # клик на поле ввода номера телефона
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").send_keys("9877120164")  # поиск поля ввода номера телефона и вставка
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/input").send_keys("q1w2e3r4t5y6")  # поиск поля пароля и вставка
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/span').click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a[2]").click()
        return driver

    def test_actual_rates_step1(self):
        driver = TestActualRates.authorization(self)
        driver.get("https://dev.marketpapa.ru/rates")
        # STEP 1
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/input").send_keys("шапка")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/input").send_keys("16530207", Keys.RETURN)
        # TESTS
        id_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]").is_displayed()
        assert id_category == True, "Не отображается id категории в актуальных ставках в 'реклама в поиске'"
        category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[3]").is_displayed()
        assert category == True, "Не отображается категория в актуальных ставках в 'реклама в поиске'"
        delivery_time = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[4]").is_displayed()
        assert delivery_time == True, "Не отображается срок доставки в актуальных ставках в 'реклама в поиске'"
        chance_of_getting_into_adv = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/div[1]/div[3]').is_displayed()
        assert chance_of_getting_into_adv == True, "Не отображается вероятность попадания в рекламу в актуальных ставках в 'реклама в поиске'"
        first_place = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[7]/div[3]/div[2]/div[1]/div[3]/div[2]/div[2]").is_displayed()
        assert first_place == True, "Не отображается первая позиция в актуальных ставках в 'реклама в поиске'"
        last_10_requests = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/div[4]').is_displayed()
        assert last_10_requests == True, "Не отображается первая позиция в актуальных ставках в 'реклама в поиске'"
        last_10_requests_name = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/div[4]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]').is_displayed()
        assert last_10_requests_name == True, "Не отображается название в истории в актуальных ставках в 'реклама в поиске'"

    def test_actual_rates_step2(self):
        driver = TestActualRates.authorization(self)
        driver.get("https://dev.marketpapa.ru/rates")
        # STEP 2
        driver.find_element(By.XPATH, '//div[text()="Реклама в поиске"]').click()
        driver.find_element(By.XPATH, '//div[text()="Реклама в карточке товара"]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/input').send_keys('39356500', Keys.RETURN)
        # TESTS
        first_string = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/div[1]/div[3]/div[1]/div[2]/div[2]").is_displayed()
        assert first_string == True, "Не отображается первая строка  в актуальных ставках в 'реклама в карточке товара'"
        photo = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[6]/div[1]/div[3]/div[1]/div[2]/div[1]/img').is_displayed()
        assert photo == True, "Не отображается фото в актуальных ставках в 'реклама в карточке товара'"
        id_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/div[1]/div[3]/div[1]/div[2]/div[2]/span/span").is_displayed()
        assert id_category == True, "Не отображается id категории в актуальных ставках в 'реклама в карточке товара'"
        real_rate = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[6]/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]').is_displayed()
        assert real_rate == True, "Не отображается реальная цена в актуальных ставках в 'реклама в карточке товара'"
        last_10_requests_table = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/div[2]").is_displayed()
        assert last_10_requests_table == True, "Не отображается таблица 10 последних запросов в актуальных ставках в 'реклама в карточке товара'"
        date_time = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]").is_displayed()
        assert date_time == True, "Не отображается дата/время в таблице 10 последних запросов в актуальных ставках в 'реклама в карточке товара'"
        request = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]").is_displayed()
        assert request == True, "Не отображается запрос в таблице 10 последних запросов в актуальных ставках в 'реклама в карточке товара'"
        first_place = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[6]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]").is_displayed()
        assert first_place == True, "Не отображается первое место в таблице 10 последних запросов в актуальных ставках в 'реклама в карточке товара'"

    def test_actual_rates_step3(self):
        driver = TestActualRates.authorization(self)
        driver.get("https://dev.marketpapa.ru/rates")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/input").send_keys("кроссовки")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/input").send_keys("10200410", Keys.RETURN)
        # TESTS
        text = driver.find_element(By.XPATH, "(//div[@class='sc-ckRZPU fXtWsM'])[1]").text
        assert text == "Высокая вероятность попадания в рекламу.", "Некорретное отображение вероятности попадания в рекламу"

    def test_actual_rates_step4(self):
        driver = TestActualRates.authorization(self)
        driver.get("https://dev.marketpapa.ru/rates")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/input").send_keys("шапки")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[6]/input").send_keys("10200410", Keys.RETURN)
        # TESTS
        text = driver.find_element(By.XPATH, "//div[@class='sc-ckRZPU fwpNwI']").text
        assert text == "Низкая вероятность попадания в рекламу.", "Некорретное отображение вероятности попадания в рекламу"

    def tearDown(self):
        self.driver.close()