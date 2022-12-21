import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import Select


class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
        self.driver.maximize_window()

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(random.randint(8, 10)))
        return rand_string

    def test_registration(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://marketpapa.ru/register") # Переход на страницу регистрации
        driver.find_element(By.NAME, "name").send_keys('Имя') # Ввод имени
        random_email_name = TestRegistration.generate_random_string(self)
        driver.find_element(By.NAME, "email").send_keys(random_email_name + "@yandex.ru") # Ввод email
        driver.find_element(By.XPATH, "//div[@class = 'sc-ehCJOs idGXiq dropdown-toggle']").click()
        driver.find_element(By.XPATH, "(//a[@role='button'])[6]").click()
        phone_number = "31251"
        for number in range(4):
            if number <= 4:
                phone_number = phone_number + str(random.randint(0, 9))
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/input").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/input").send_keys(phone_number)
        random_password = TestRegistration.generate_random_string(self)
        driver.find_element(By.NAME, "password").send_keys(random_password)
        driver.find_element(By.NAME, "passwordRepeat").send_keys(random_password)
        driver.find_element(By.XPATH, "//span[@class='sc-iJKOTD ksUpGB']").click()
        driver.find_element(By.NAME, 'code').send_keys('1111')
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[text()='Готово']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[3]/label").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/button").click()
