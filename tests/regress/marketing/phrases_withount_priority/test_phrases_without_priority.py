import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPhrasesWithoutPriority(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
        self.driver.maximize_window()

    def authorization(self):
        driver = self.driver
        driver.implicitly_wait(10)  # неявное ожидание появления элемента
        driver.get("https://marketpapa.ru/login")  # переход на страницу авторизации
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/input").click()  # клик на поле ввода номера телефона
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").send_keys("9877120164")  # поиск поля ввода номера телефона и вставка
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/input").send_keys("q1w2e3r4t5y6")  # поиск поля пароля и вставка
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/span').click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a[2]").click()
        return driver

    def test_phrases_without_priority_step1(self):
        driver = TestPhrasesWithoutPriority.authorization(self)
        driver.implicitly_wait(10)
        driver.get("https://marketpapa.ru/bad_priority_phrases")
        driver.find_element(By.XPATH, "//input[@class='sc-hkgtus gRNWA-d']").send_keys("9285253", Keys.RETURN)
        time.sleep(5)
        # TESTS
        phrase = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div/div/div").is_displayed()
        assert phrase == True, "Не отображается фраза на странице приоритетной категории"
        frequency = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span").is_displayed()
        assert frequency == True, "Не отображается частотность на странице приоритетной категории"
        id_priority_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/span").is_displayed()
        assert id_priority_category == True, "Не отображается id приоритетной категории на странице приоритетной категории"
        first_place = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]").is_displayed()
        assert first_place == True, "Не отображается первое место на странице приоритетной категории"

    def test_phrases_without_priority_step2(self):
        driver = TestPhrasesWithoutPriority.authorization(self)
        driver.implicitly_wait(10)
        driver.get("https://marketpapa.ru/bad_priority_phrases")
        driver.find_element(By.XPATH, "//div[@class='sc-jivBlf daFcZY dropdown-toggle']").click()
        driver.find_element(By.XPATH, "//div[@class='sc-edERGn eYeYxI dropdown-menu show']//div[2]").click()
        driver.find_element(By.XPATH, "//input[@class='sc-hkgtus gRNWA-d']").send_keys("носки", Keys.RETURN)
        time.sleep(5)
        # TESTS
        phrase = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div/div/div").is_displayed()
        assert phrase == True, "Не отображается фраза на странице приоритетной категории"
        frequency = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span").is_displayed()
        assert frequency == True, "Не отображается частотность на странице приоритетной категории"
        id_priority_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/span").is_displayed()
        assert id_priority_category == True, "Не отображается id приоритетной категории на странице приоритетной категории"
        first_place = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]").is_displayed()
        assert first_place == True, "Не отображается первое место на странице приоритетной категории"



