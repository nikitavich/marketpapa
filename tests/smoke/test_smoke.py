import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestSmoke:
    def test_authorization(self, driver):
        driver.get('https://marketpapa.ru/login')
        driver.find_element(By.NAME, 'phone').send_keys('+79877120164')
        driver.find_element(By.NAME, 'password').send_keys('q1w2e3r4t5y6')
        driver.find_element(By.XPATH, "//span[@class='sc-iJnaPW izGUBw']").click()
        time.sleep(3)
        assert driver.current_url == "https://marketpapa.ru/find", "Не работает авторизация"