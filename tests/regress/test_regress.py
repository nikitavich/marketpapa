import datetime
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from lib.base_case import BaseCase


class TestRegress:

    def test_actual_rates_step1(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://dev.marketpapa.ru/rates")
        # STEP 1
        driver.find_element(By.CSS_SELECTOR, "div[class='sc-jivBlf llhNyk'] input[placeholder='Поиск']").send_keys("шапка")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Введите артикул, который хотите рекламировать']").send_keys("16530207", Keys.RETURN)
        # TESTS
        id_category = driver.find_element(By.XPATH, "//td[normalize-space()='82']").is_displayed()
        assert id_category == True, "Не отображается id категории в актуальных ставках в 'реклама в поиске'"
        category = driver.find_element(By.XPATH, "//td[contains(text(),'Шапки')]").is_displayed()
        assert category == True, "Не отображается категория в актуальных ставках в 'реклама в поиске'"
        delivery_time = driver.find_element(By.XPATH, "//td[1]").is_displayed()
        assert delivery_time == True, "Не отображается срок доставки в актуальных ставках в 'реклама в поиске'"
        chance_of_getting_into_adv = driver.find_element(By.XPATH, "//*[text()='Высокая вероятность попадания в рекламу.']").is_displayed()
        assert chance_of_getting_into_adv == True, "Не отображается вероятность попадания в рекламу в актуальных ставках в 'реклама в поиске'"
        first_place = driver.find_element(By.XPATH, "//div[@class='sc-evcjhq Yzmce'][normalize-space()='1']").is_displayed()
        assert first_place == True, "Не отображается первая позиция в актуальных ставках в 'реклама в поиске'"

    def test_actual_rates_step2(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://dev.marketpapa.ru/rates")
        # STEP 2
        driver.find_element(By.XPATH, '//div[text()="Реклама в поиске"]').click()
        driver.find_element(By.XPATH, '//div[text()="Реклама в карточке товара"]').click()
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Артикул']").send_keys('39356500', Keys.RETURN)
        # TESTS
        first_string = driver.find_element(By.CSS_SELECTOR, ".sc-ewSTlh.eRZong").is_displayed()
        assert first_string == True, "Не отображается первая строка  в актуальных ставках в 'реклама в карточке товара'"
        last_10_requests_table = driver.find_element(By.CSS_SELECTOR, "div[name='left']").is_displayed()
        assert last_10_requests_table == True, "Не отображается таблица 10 последних запросов в актуальных ставках в 'реклама в карточке товара'"

    def test_actual_rates_step3(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://dev.marketpapa.ru/rates")
        driver.find_element(By.CSS_SELECTOR, "div[class='sc-jivBlf llhNyk'] input[placeholder='Поиск']").send_keys("кроссовки")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Введите артикул, который хотите рекламировать']").send_keys("10200410", Keys.RETURN)
        # TESTS
        text = driver.find_element(By.CSS_SELECTOR, ".sc-ciFQTS.eFFrwj").text
        assert text == "Высокая вероятность попадания в рекламу.", "Некорретное отображение вероятности попадания в рекламу"

    def test_actual_rates_step4(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://dev.marketpapa.ru/rates")
        driver.find_element(By.CSS_SELECTOR, "div[class='sc-jivBlf llhNyk'] input[placeholder='Поиск']").send_keys("шапки")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Введите артикул, который хотите рекламировать").send_keys("10200410", Keys.RETURN)
        # TESTS
        text = driver.find_element(By.CSS_SELECTOR, ".sc-ciFQTS.hfbeOv").text
        assert text == "Низкая вероятность попадания в рекламу.", "Некорретное отображение вероятности попадания в рекламу"

    def test_create_adv_company(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://dev.marketpapa.ru/ad_cabinet/1/campaigns")
        driver.find_element(By.XPATH, "//span[@class='sc-iJKOTD ksUpGB']").click()
        date = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        driver.find_element(By.XPATH, "//input[@placeholder='Введите название']").send_keys("autotest " + date)
        driver.find_element(By.XPATH, '//span[contains(text(),"Выберите группы предметов")]').click()
        driver.find_element(By.XPATH, "//label[contains(text(),'Брюки')]").click()
        driver.find_element(By.CSS_SELECTOR, ".sc-lkqIyp.cmaUOR").click()
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Выберите предметы']").click()
        driver.find_element(By.XPATH, "(//div[contains(text(),'Брюки классические женские / теплые / на резинке/ ')])[1]").click()
        driver.find_element(By.CSS_SELECTOR, ".sc-lkqIyp.cmaUOR").click()
        driver.find_element(By.CSS_SELECTOR, '.sc-bBHxTw.kMBSgb').click()
        driver.find_element(By.CSS_SELECTOR, '.sc-iJKOTD.ksUpGB').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Обновить данные')]").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Введите название кампании либо ID']").send_keys(f"autotest {date}", Keys.RETURN)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        new_company = driver.find_element(By.XPATH, "(//div[@role='row'])[5]").is_displayed()
        assert new_company == True, "Новая кампания не найдена"

    # def test_phrases(self, driver):
    #     BaseCase().add_cookie_to_chrome(driver)
    #     driver.get("https://dev.marketpapa.ru/phrases")
    #     driver.find_element(By.NAME, "articul").send_keys("74322224")
    #     driver.find_element(By.CSS_SELECTOR, "input[placeholder='Начните вводить ключевое слово']").send_keys("носки", Keys.RETURN)
    #     # TESTS
    #     main_table = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/table").is_displayed()
    #     assert main_table == True, "Не отображается элемент Id категории в подборе фраз"
    #     category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/span").is_displayed()
    #     assert category == True, "Не отображается элемент 'Категории' в подборе фраз"
    #     delivery_time = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[3]/span").is_displayed()
    #     assert delivery_time == True, "Не отображается элемент 'Срок доставки' в подборе фраз"
    #     frequency_per_month = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span").is_displayed()
    #     assert frequency_per_month == True, "Не отображается частотность за месяц в подборе фраз"
    #     frequency_per_day = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/span").is_displayed()
    #     assert frequency_per_day == True, "Не отображается частотность за день в подборе фраз"
    #     first_phrase = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div/div/div").is_displayed()
    #     assert first_phrase == True, "Не отображается фраза в подборе фраз"
    #     id_priority_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/div/div/div[1]/span").is_displayed()
    #     assert id_priority_category == True, "Не отображается Id приоритетной категории в подборе фраз"
    #     max_delivery_time = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/div").is_displayed()
    #     assert max_delivery_time == True, "Не отображается максимальное время доставки в подборе фраз"
    #     first_place = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[5]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[5]").is_displayed()
    #     assert first_place == True, "Не отображается первое место в таблице в подборе фраз"

