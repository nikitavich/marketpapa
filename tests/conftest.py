import pickle
import random
import time
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from lib import settings
from lib.base_case import BaseCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lib.internal_analytics import send_request


@pytest.fixture(scope="session")
def get_id_from_token():
    response = send_request(method='get',
                            url='https://api.marketpapa.ru/api/internal-analytics/token/')
    parsed_response_text = response.json()
    ids = None
    for element in parsed_response_text['items']:
        if element["key_name"] == "Загружено из рекламы 'Наш Кабинет'":
            ids = element["id"]
    response_status_code = response.status_code
    return response_status_code, ids


@pytest.fixture()
def driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "113.0",
    #     "selenoid:options": {
    #         "enableVideo": False
    #     }
    #
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("browserName", 'chrome')
    chrome_options.set_capability("browserVersion", '113.0')
    chrome_options.set_capability("selenoid:options", {"enableVideo": False})

    driver = webdriver.Remote(
        command_executor="http://158.160.69.202:4444/wd/hub", options=chrome_options)
    yield driver
    driver.quit()



@pytest.fixture()
def add_cookies_for_auth(driver):
    driver.get("https://dev.marketpapa.ru/news")
    for cookie in pickle.load(open("../cookies.pkl", "rb")):
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()



