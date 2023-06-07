import time

from webdriver_manager.chrome import ChromeDriverManager

from lib.base_case import BaseCase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestSmoke:

    def test_authorization(self, driver):
        driver.get('https://marketpapa.ru/login')
        driver.find_element(By.NAME, 'phone').send_keys('+79877120164')
        driver.find_element(By.NAME, 'password').send_keys('q1w2e3r4t5y6')
        driver.find_element(By.XPATH, "//span[@class='sc-iJnaPW izGUBw']").click()
        time.sleep(3)
        assert driver.current_url == "https://marketpapa.ru/find", "Не работает авторизация"

    def test_actual_rates(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://marketpapa.ru/rates")
        driver.find_element(By.XPATH, "//input[@placeholder='Введите фразу']").send_keys("шапка")
        driver.find_element(By.XPATH, "//input[@placeholder='Введите артикул']").send_keys("16530207", Keys.RETURN)
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'master-phrase-stat')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'master-phrase-compare')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-month')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-day')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'master-phrase-delivery-time')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'master-phrase-category')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'compare-your-product')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'rate-city-tab')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'rate-page')]")
        assert driver.find_element(By.XPATH, "//div[contains(@data-test,'table-master-phrase-rates')]")

    def test_list_of_advertising_campaigns(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get(
            "https://marketpapa.ru/ad_cabinet/1/campaigns?name=%D0%9D%D0%B0%D1%88%20%D0%9A%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82")
        assert driver.find_element(By.XPATH, "//span[@data-test='cabinet-status']")
        assert driver.find_element(By.XPATH, "//span[@data-test='cabinet-updated-at']")
        assert driver.find_element(By.XPATH, "//span[@data-test='btn-update-cabinet']")
        assert driver.find_element(By.XPATH, "//div[@data-test='tabs']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-filters-wrap']")
        assert driver.find_element(By.XPATH, "//div[@data-test='search-icon']")
        assert driver.find_element(By.XPATH, "//input[@data-test='search-input']")
        assert driver.find_element(By.XPATH, "//div[@data-test='dd-columns']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaigns-active']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-status-tab']")
        assert driver.find_element(By.XPATH, "//div[@data-test='table-campaigns']")
        assert driver.find_element(By.XPATH, "//div[@data-test='switch-active-left']")

    def test_advertising_campaign_search(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://marketpapa.ru/ad_cabinet_view/1/3499821?category_name=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-header']")
        assert driver.find_element(By.XPATH, "//div[@data-test='back-button']")
        assert driver.find_element(By.XPATH, "//a[@data-test='campaign-header-link-wb']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-name']")
        assert driver.find_element(By.XPATH, "//i[@data-test='campaign-update']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-created-time']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-created-date']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-manage']")
        assert driver.find_element(By.XPATH, "//a[@data-test='campaign-history']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-tuned']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-status']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-header-interval']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-info']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-type']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-supplier-name']")
        assert driver.find_element(By.XPATH, "//a[@data-test='campaign-id-link']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-id']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-subject-id']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-subject-name']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-delivery-time']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-articuls']")
        assert driver.find_element(By.XPATH, "//img[@data-test='campaign-articul-51358326']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-settings']")
        assert driver.find_element(By.XPATH, "//a[@data-test='campaign-import-settings']")
        assert driver.find_element(By.XPATH, "//span[@data-test='campaign-total-budget']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-target-place']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-max-price']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-interval-1']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-0']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-1']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-2']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-max-price-0']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-max-price-1']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-max-price-2']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-target-price']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-max-price-4']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-manage-type-max-price-3']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-target-place-0']")
        assert driver.find_element(By.XPATH, "//input[@data-test='campaign-target-place-1']")
        assert driver.find_element(By.XPATH, "//div[@data-test='campaign-master-phrase']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-region']")
        assert driver.find_element(By.XPATH, "//div[@data-test='dropdown-selected']")
        assert driver.find_element(By.XPATH, "//ul[@data-test='dropdown-list']")
        assert driver.find_element(By.XPATH, "//div[@data-test='search-wrapper']")
        assert driver.find_element(By.XPATH, "//input[@data-test='master-phrase-input']")
        assert driver.find_element(By.XPATH, "//button[@data-test='search-button']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-stat']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-frequency-month']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-frequency-day']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-delivery-time']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-category']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-compare']")
        assert driver.find_element(By.XPATH, "//div[@data-test='compare-your-product']")
        assert driver.find_element(By.XPATH, "//div[@data-test='compare-phrase-delivery-time']")
        assert driver.find_element(By.XPATH, "//div[@data-test='compare-your-delivery-time']")
        assert driver.find_element(By.XPATH, "//div[@data-test='compare-phrase-priority-category']")
        assert driver.find_element(By.XPATH, "//div[@data-test='compare-your-priority-category']")
        assert driver.find_element(By.XPATH, "//div[@data-test='master-phrase-chance']")
        assert driver.find_element(By.XPATH, "//div[@data-test='rate-city-tabs']")
        assert driver.find_element(By.XPATH, "//div[@data-test='rate-city-tab']")
        assert driver.find_element(By.XPATH, "//div[@data-test='rate-pages']")
        assert driver.find_element(By.XPATH, "//div[@data-test='table-master-phrase-rates']")
        assert driver.find_element(By.XPATH, "//input[@data-test='ctr-views']")
        assert driver.find_element(By.XPATH, "//input[@data-test='ctr-ctr']")
        assert driver.find_element(By.XPATH, "//input[@data-test='ctr-cpc']")
        assert driver.find_element(By.XPATH, "//input[@data-test='radio-ctr_radio']")
        assert driver.find_element(By.XPATH, "//input[@data-test='organic_place']")
        assert driver.find_element(By.XPATH, "//input[@data-test='radio-organic_place_radio']")
        assert driver.find_element(By.XPATH, "//button[@data-test='btn-save-campaign']")
        assert driver.find_element(By.XPATH, "//button[@data-test='btn-manage-campaign']")

    def test_monitoring_positions(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://marketpapa.ru/positions?product_id=48902763")
        assert driver.find_element(By.XPATH, "//div[@data-test='search-wrapper']")
        assert driver.find_element(By.XPATH, "//button[@data-test='search-button']")
        assert driver.find_element(By.XPATH, "//span[@data-test='favorite-icon']")
        assert driver.find_element(By.XPATH, "//span[@data-test='filter-date-start']")
        assert driver.find_element(By.XPATH, "//span[@data-test='filter-date-end']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-month']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-week']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-twoweeks']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-twomonths']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-threemonths']")
        assert driver.find_element(By.XPATH, "//div[@data-test='phrase-search']")
        assert driver.find_element(By.XPATH, "//div[@data-test='search-wrapper']")
        assert driver.find_element(By.XPATH, "//button[@data-test='search-button']")
        assert driver.find_element(By.XPATH, "//div[@data-test='monitoring-position-table']")

    def test_phrase_selection(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://marketpapa.ru/phrase_selection")
        assert driver.find_element(By.XPATH, "//div[@data-test='phrase-selection']")
        assert driver.find_element(By.XPATH, "//div[@data-test='tabs']")
        assert driver.find_element(By.XPATH, "//div[@data-test='tab-selection']")
        assert driver.find_element(By.XPATH, "//div[@data-test='tab-selected']")
        assert driver.find_element(By.XPATH, "//div[@data-test='tab-description']")
        assert driver.find_element(By.XPATH, "//div[@data-test='selection-wrapper']")
        assert driver.find_element(By.XPATH, "//input[@data-test='phrase-search']")
        assert driver.find_element(By.XPATH, "//div[@data-test='phrase-search-icon']")
        assert driver.find_element(By.XPATH, "//div[@data-test='btn-export']")
        assert driver.find_element(By.XPATH, "//span[@data-test='dd-columns']")
        assert driver.find_element(By.XPATH, "//div[@data-test='phrase-table']")
        assert driver.find_element(By.XPATH, "//div[@data-test='selected-wrapper']")
        assert driver.find_element(By.XPATH, "//div[@data-test='phrase-in-title']")
        assert driver.find_element(By.XPATH, "//div[@data-test='phrase-in-description']")
        assert driver.find_element(By.XPATH, "//div[@data-test='description-wrapper']")
        assert driver.find_element(By.XPATH, "//textarea[@data-test='input-name']")
        assert driver.find_element(By.XPATH, "//button[@data-test='copy-name']")
        assert driver.find_element(By.XPATH, "//textarea[@data-test='input-description']")
        assert driver.find_element(By.XPATH, "//button[@data-test='copy-description']")

    def test_order_sale_feed(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://marketpapa.ru/order_sale_feed")
        assert driver.find_element(By.XPATH, "//div[@data-test='order-sale-feed-page']")
        assert driver.find_element(By.XPATH, "//div[@data-test='internal-tabs']")
        assert driver.find_element(By.XPATH, "//a[@data-test='internal-tab']")
        assert driver.find_element(By.XPATH, "//div[@data-test='dd-search-wrap']")
        assert driver.find_element(By.XPATH, "//div[@data-test='dd-search']")
        assert driver.find_element(By.XPATH, "//input[@data-test='dd-search-input']")
        assert driver.find_element(By.XPATH, "//div[@data-test='btn-dd-search']")
        assert driver.find_element(By.XPATH, "//div[@data-test='switch-active-left']")
        assert driver.find_element(By.XPATH, "//div[@data-test='all-api-keys-toggle']")
        assert driver.find_element(By.XPATH, "//span[@data-test='filter-date-start']")
        assert driver.find_element(By.XPATH, "//span[@data-test='filter-date-start']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-today']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-yesterday']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-month']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-week']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-date-twoweeks']")
        assert driver.find_element(By.XPATH, "//button[@data-test='btn-filter-order-sale']")
        assert driver.find_element(By.XPATH, "//button[@data-test='btn-filter-cancel-return']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-item']")
        assert driver.find_element(By.XPATH, "//div[@data-test='btn-clear-filters']")
        assert driver.find_element(By.XPATH, "//div[@data-test='btn-export']")
        assert driver.find_element(By.XPATH, "//span[@data-test='dd-columns']")
        assert driver.find_element(By.XPATH, "//div[@data-test='order-feed-table']")
        assert driver.find_element(By.XPATH, "//button[@data-test='btn-save-order-feed']")

    def test_my_products(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.get("https://marketpapa.ru/my_products")
        assert driver.find_element(By.XPATH, "//div[@data-test='my-products-page']")
        assert driver.find_element(By.XPATH, "//div[@data-test='internal-tabs']")
        assert driver.find_element(By.XPATH, "//a[@data-test='internal-tab']")
        assert driver.find_element(By.XPATH, "//div[@data-test='dd-search-wrap']")
        assert driver.find_element(By.XPATH, "//div[@data-test='dd-search']")
        assert driver.find_element(By.XPATH, "//input[@data-test='dd-search-input']")
        assert driver.find_element(By.XPATH, "//div[@data-test='btn-dd-search']")
        assert driver.find_element(By.XPATH, "//button[@data-test='filter-with-cost-price']")
        assert driver.find_element(By.XPATH, "//button[@data-test='filter-without-cost-price']")
        assert driver.find_element(By.XPATH, "//button[@data-test='btn-upload-cost-price']")
        assert driver.find_element(By.XPATH, "//div[@data-test='all-api-keys-toggle']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-item']")
        assert driver.find_element(By.XPATH, "//div[@data-test='filter-clear']")
        assert driver.find_element(By.XPATH, "//span[@data-test='dd-columns']")
        assert driver.find_element(By.XPATH, "//div[@data-test='my-products-table']")
