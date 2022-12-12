import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    wd = webdriver.Chrome()
    return wd


def test_authorization(driver):
    driver.implicitly_wait(10) # неявное ожидание появления элемента
    driver.get("https://dev.marketpapa.ru/login") # переход на страницу авторизации
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").click() # клик на поле ввода номера телефона
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/input").send_keys("9877120164") # поиск поля ввода номера телефона и вставка
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/input").send_keys("q1w2e3r4t5y6") # поиск поля пароля и вставка
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/span').click() # закрыть инструкцию