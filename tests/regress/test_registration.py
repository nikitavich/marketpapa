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





