from lib.base_case import BaseCase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSmoke:

    def test_authorization(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get('https://marketpapa.ru/login')
        driver.find_element(By.NAME, 'phone').send_keys('+79877120164')
        driver.find_element(By.NAME, 'password').send_keys('q1w2e3r4t5y6')
        driver.find_element(By.XPATH, "//span[@class='sc-iJnaPW izGUBw']").click()
        wait.until(EC.url_to_be("https://marketpapa.ru/find"))
        assert driver.current_url == "https://marketpapa.ru/find", "Не работает авторизация"

    def test_actual_rates(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 30)
        driver.get("https://marketpapa.ru/rates")
        driver.find_element(By.XPATH, "//input[@placeholder='Введите фразу']").send_keys("шапка")
        driver.find_element(By.XPATH, "//input[@placeholder='Введите артикул']").send_keys("16530207", Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-stat')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-compare')]")))
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-mont')]")))
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-day')]")))
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-delivery-time')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-category')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'compare-your-product')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-city-tab')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-page')]")))
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'table-master-phrase-rates')]")))

    def test_list_of_advertising_campaigns(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 10)
        driver.get(
            "https://marketpapa.ru/ad_cabinet/1/campaigns?name=%D0%9D%D0%B0%D1%88%20%D0%9A%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82")
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'cabinet-status')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'cabinet-updated-at')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'btn-update-cabinet')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-filters-wrap')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'search-icon')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'search-input')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'dd-columns')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaigns-active')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-status-tab')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'table-campaigns')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'switch-active-left')]"))))

    def test_advertising_campaign_search(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 10)
        driver.get("https://marketpapa.ru/ad_cabinet_view/1/7045150?category_name=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA")
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-header')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'back-button')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-test,'campaign-header-link-wb')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-name')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//i[contains(@data-test,'campaign-update')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-created-time')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-created-date')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-manage')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-test,'campaign-history')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-tuned')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-status')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-header-interval')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-info')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-type')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-supplier-name')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-test,'campaign-id-link')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-id')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-subject-id')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-subject-name')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-delivery-time')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-articuls')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//img[contains(@data-test,'campaign-articul-51349857')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-settings')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-test,'campaign-import-settings')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//span[contains(@data-test,'campaign-total-budget')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'campaign-target-place')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'campaign-max-price')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-interval-1')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'campaign-target-price')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'campaign-master-phrase')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-region')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'dropdown-selected')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'search-wrapper')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'master-phrase-input')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-stat')]"))))
        wait.until((EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-month')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-day')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-delivery-time')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-category')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-compare')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'compare-your-product')]"))))
        wait.until((EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@data-test,'compare-phrase-delivery-time')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'compare-your-delivery-time')]"))))
        wait.until((EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@data-test,'compare-phrase-priority-category')]"))))
        wait.until((EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@data-test,'compare-your-priority-category')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-chance')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-city-tabs')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-city-tab')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-pages')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'table-master-phrase-rates')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'ctr-views')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'ctr-ctr')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'ctr-cpc')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//input[contains(@data-test,'organic_place')]"))))
        wait.until((EC.visibility_of_element_located((By.XPATH, "//button[contains(@data-test,'btn-save-campaig')]"))))
        wait.until(
            (EC.visibility_of_element_located((By.XPATH, "//button[contains(@data-test,'btn-manage-campaign')]"))))

    def test_monitoring_positions(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 10)
        driver.get("https://marketpapa.ru/positions?product_id=48902763")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='search-wrapper']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='search-wrapper']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='search-button']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='favorite-icon']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='filter-date-start']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='filter-date-end']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-month']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-week']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-twoweeks']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-twomonths']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-threemonths']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='phrase-search']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='search-wrapper']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='search-button']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='monitoring-position-table']")))

    def test_phrase_selection(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 10)
        driver.get("https://marketpapa.ru/phrase_selection")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='phrase-selection']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='tabs']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='tab-selection']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='tab-selected']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='tab-description']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='selection-wrapper']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='phrase-search']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='phrase-search-icon']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='btn-export']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='dd-columns']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='phrase-table']")))

    def test_order_sale_feed(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 10)
        driver.get("https://marketpapa.ru/order_sale_feed")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='order-sale-feed-page']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='internal-tabs']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-test='internal-tab']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='dd-search-wrap']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='dd-search']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='dd-search-input']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='btn-dd-search']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='switch-active-left']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='all-api-keys-toggle']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='filter-date-start']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='filter-date-start']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-today']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-yesterday']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-month']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-week']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-date-twoweeks']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='btn-filter-order-sale']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='btn-filter-cancel-return']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-item']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='btn-clear-filters']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='btn-export']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='dd-columns']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='order-feed-table']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='btn-save-order-feed']")))

    def test_my_products(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        wait = WebDriverWait(driver, 10)
        driver.get("https://marketpapa.ru/my_products")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='my-products-page']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='internal-tabs']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-test='internal-tab']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='dd-search-wrap']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='dd-search']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='dd-search-input']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='btn-dd-search']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='filter-with-cost-price']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='filter-without-cost-price']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='btn-upload-cost-price']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='all-api-keys-toggle']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-item']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='filter-clear']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-test='dd-columns']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='my-products-table']")))
