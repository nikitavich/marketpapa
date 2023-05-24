import pickle
import random
import time
import pytest
import requests
from selenium.webdriver.common.by import By
from lib import settings
from lib.base_case import BaseCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def get_id_from_token():
    response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                            headers={
                                "Authorization": "Bearer " + str(settings.token)
                            }
                            )
    parsed_response_text = response.json()
    ids = None
    for element in parsed_response_text['items']:
        if element["key_name"] == "NEW_Василий":
            ids = element["id"]
    response_status_code = response.status_code
    return response_status_code, ids


@pytest.fixture()
def driver():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "113.0",
        "selenoid:options": {
            "enableVideo": False,
            "timeouts": "180"
        }
    }
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://172.17.0.3:4444/",
        options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def add_cookies_for_auth(driver):
    driver.get("https://dev.marketpapa.ru/news")
    for cookie in pickle.load(open("../cookies.pkl", "rb")):
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()


@pytest.fixture()
def registration(driver):
    driver.implicitly_wait(5)
    driver.get("https://marketpapa.ru/register")  # Переход на страницу регистрации
    driver.find_element(By.NAME, "name").send_keys('Имярек')  # Ввод имени
    random_email_name = BaseCase().generate_random_string()
    driver.find_element(By.NAME, "email").send_keys(random_email_name + "@yandex.ru")  # Ввод email
    phone_number = "+99631251"
    for number in range(4):
        if number <= 4:
            phone_number = phone_number + str(random.randint(0, 9))
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Номер телефона']").send_keys(phone_number)
    random_password = BaseCase().generate_random_string()
    driver.find_element(By.NAME, "password").send_keys(random_password)
    driver.find_element(By.NAME, "passwordRepeat").send_keys(random_password)
    driver.find_element(By.CSS_SELECTOR, ".sc-iJKOTD.ksUpGB").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='radio_exp_0_50_exp_0_50']").click()
    driver.find_element(By.CSS_SELECTOR, ".sc-bBHxTw.gaeHcs").click()
    driver.find_element(By.NAME, 'code').send_keys('1111')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".sc-bBHxTw.sc-clIzBv.jqrcgG.fEXwZu").click()
    driver.find_element(By.CSS_SELECTOR, "")
