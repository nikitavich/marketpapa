import time
import unittest
from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By


class CreateAdvComp(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
        self.driver.maximize_window()

    def authorization(self):
        driver = self.driver
        driver.implicitly_wait(10)  # неявное ожидание появления элемента
        driver.get("https://dev.marketpapa.ru/login")  # переход на страницу авторизации
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div/div[2]/div[1]/div/input").click()  # клик на поле ввода номера телефона
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").send_keys(
            "9877120164")  # поиск поля ввода номера телефона и вставка
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/input").send_keys(
            "q1w2e3r4t5y6")  # поиск поля пароля и вставка
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/button').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/span').click()
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a[2]").click()
        return driver


    def test_create_adv_company(self):
        driver = CreateAdvComp.authorization(self)
        driver.get("https://dev.marketpapa.ru/ad_cabinet/1/campaigns")
        driver.find_element(By.XPATH, "//span[@class='sc-iJKOTD ksUpGB']").click()
        date = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        driver.find_element(By.XPATH, "//input[@placeholder='Введите название']").send_keys("autotest " + date)
        driver.find_element(By.XPATH, '//span[contains(text(),"Выберите группы предметов")]').click()
        driver.find_element(By.XPATH, "//label[contains(text(),'Брюки')]").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Введите название']").click()
        driver.find_element(By.XPATH, '//span[@class="sc-hBUSln vlIDm"]').click()
        driver.find_element(By.XPATH, '//body[1]/div[1]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//span[@class="sc-iJKOTD ksUpGB"]').click()
        driver.find_element(By.XPATH, '//span[@class="sc-iJKOTD ksUpGB"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Обновить данные')]").click()
        time.sleep(10)
        driver.refresh()
        time.sleep(1)
        name_of_company = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[3]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/a[2]").text
        assert name_of_company == "autotest " + date, "wrong"



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
