import pickle
import unittest
import time
import os
from lib.base_case import BaseCase
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import Select


class TestRegistration:

    def test_simple(self, driver):
        # print(os.getcwd())
        BaseCase().add_cookie_to_chrome(driver)

    def test_auth(self, driver):
        driver.get("https://dev.marketpapa.ru/login")
        i = 0
        while i < 2:
            driver.find_element(By.NAME, 'phone').send_keys('+79877120164')
            driver.find_element(By.NAME, 'password').send_keys('q1w2e3r4t5y6')
            driver.find_element(By.CSS_SELECTOR, ".sc-iJKOTD.ksUpGB").click()
            time.sleep(1)
            driver.refresh()
            driver.find_element(By.XPATH, "//*[text()='ДенисК']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//a[contains(text(),'Выйти')]").click()
            i += 1






