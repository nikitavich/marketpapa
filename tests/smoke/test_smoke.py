import time

from lib.base_case import BaseCase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.base_case import find_element_on_page

class TestSmoke:

    def test_authorization(self, driver):
        driver.get('https://marketpapa.ru/login')
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, 'phone').send_keys('+79877120164')
        driver.find_element(By.NAME, 'password').send_keys('q1w2e3r4t5y6')
        driver.find_element(By.XPATH, "//span[@class='sc-iJnaPW izGUBw']").click()
        time.sleep(3)
        assert driver.current_url == "https://marketpapa.ru/find", "Не работает авторизация"
    # нестабильный
    # def test_actual_rates(self, driver):
    #     BaseCase().add_cookie_to_chrome(driver)
    #     wait = WebDriverWait(driver, 30)
    #     driver.get("https://marketpapa.ru/rates")
    #     find_element_on_page(driver,, "//input[@placeholder='Введите фразу']").send_keys("шапка")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Введите артикул']").send_keys("16530207", Keys.RETURN)
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-stat')]")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-compare')]")))
    #     wait.until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-mont')]")))
    #     wait.until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-frequency-day')]")))
    #     wait.until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-delivery-time')]")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'master-phrase-category')]")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'compare-your-product')]")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-city-tab')]")))
    #     wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'rate-page')]")))
    #     wait.until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-test,'table-master-phrase-rates')]")))

    def test_list_of_advertising_campaigns(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.implicitly_wait(10)
        driver.get(
            "https://marketpapa.ru/ad_cabinet/1/campaigns?name=%D0%9D%D0%B0%D1%88%20%D0%9A%D0%B0%D0%B1%D0%B8%D0%BD%D0%B5%D1%82")
        assert find_element_on_page(driver, "//span[contains(@data-test,'cabinet-status')]"), 'list_of_advertising_campaigns: Не отображается статус кабинета'
        assert find_element_on_page(driver, "//span[contains(@data-test,'cabinet-updated-at')]"), 'list_of_advertising_campaigns: Не отображается дата последнего обновления'
        assert find_element_on_page(driver, "//span[contains(@data-test,'btn-update-cabinet')]"), 'list_of_advertising_campaigns: Не отображается кнопка обновления кабинета'
        assert find_element_on_page(driver, "//div[contains(@data-test,'tabs')]"), 'list_of_advertising_campaigns: Не отображаются вкладки'
        assert find_element_on_page(driver, "//div[contains(@data-test,'tab-campaigns')]"), 'list_of_advertising_campaigns: Не отображается кнопка РЕКЛАМНЫЕ КАМПАНИИ'
        assert find_element_on_page(driver, "//div[contains(@data-test,'tab-articuls')]"), 'list_of_advertising_campaigns: Не отображается кнопка АРТИКУЛЫ'
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-filters-wrap')]"), 'list_of_advertising_campaigns: Не отображаются ПОИСК КОЛОНКИ ФИЛЬТРЫ'
        assert find_element_on_page(driver, "//div[contains(@data-test,'search-icon')]"), 'list_of_advertising_campaigns: Не отображается иконка поиска'
        assert find_element_on_page(driver, "//input[contains(@data-test,'search-input')]"), 'list_of_advertising_campaigns: Не отображается поле поиска'
        assert find_element_on_page(driver, "//div[contains(@data-test,'dd-columns')]"), 'list_of_advertising_campaigns: Не отображается кнопка КОЛОНКИ'
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaigns-activ')]"), 'list_of_advertising_campaigns: Не отображается таблица кампаний'
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-status-tab')]"), 'list_of_advertising_campaigns: Не отображается статус таблицы кампаний'
        assert find_element_on_page(driver, "//div[contains(@data-test,'table-campaigns')]"), 'list_of_advertising_campaigns: Не отображается таблица кампаний'

    def test_advertising_campaign_search(self, driver):
        BaseCase().add_cookie_to_chrome(driver)
        driver.implicitly_wait(10)
        driver.get("https://marketpapa.ru/ad_cabinet_view/1/7045150?category_name=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA")
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-header')]"), "advertising_campaign_search: Не отображается header компании"
        assert find_element_on_page(driver, "//div[contains(@data-test,'back-button')]"), "advertising_campaign_search: Не отображается кнопка назад"
        assert find_element_on_page(driver, "//a[contains(@data-test,'campaign-header-link-wb')]"), "advertising_campaign_search: Не отображается ссылка на вб в header"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-name')]"), "advertising_campaign_search: Не отображается имя компании"
        assert find_element_on_page(driver, "//i[contains(@data-test,'campaign-update')]"), "advertising_campaign_search: Не отображается кнопка обновления кампании"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-created-time')]"), "advertising_campaign_search: Не отображается время создания кампании"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-created-date')]"), "advertising_campaign_search: Не отображается время создания кампании"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-manage')]"), "advertising_campaign_search: Не отображается блок УПРАВЛЕНИЕ КАМПАНИЕЙ"
        assert find_element_on_page(driver, "//a[contains(@data-test,'campaign-history')]"), "advertising_campaign_search: Не отображается ссылка на историю управления"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-tuned')]"), "advertising_campaign_search: Не отображается картинка НАСТРОЕНА В рекламной кампании"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-status')]"), "advertising_campaign_search: Не отображается статус кампании"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-header-interval')]"), "advertising_campaign_search: Не отображается интервалы показов"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-info')]"), "advertising_campaign_search: Не отображается информация о кампании"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-type')]"), "advertising_campaign_search: Не отображается тип кампании"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-supplier-name')]"), "advertising_campaign_search: Не отображается тип рекламного кабинета"
        assert find_element_on_page(driver, "//a[contains(@data-test,'campaign-id-link')]"), "advertising_campaign_search: Не отображается ссылка на вб в информации"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-id')]"), "advertising_campaign_search: Не отображается id кампании"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-subject-id')]"), "advertising_campaign_search: Не отображается категория"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-subject-name')]"), "advertising_campaign_search: Не отображается название категории"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-delivery-time')]"), "advertising_campaign_search: Не отображается срок доставки"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-articuls')]"), "advertising_campaign_search: Не отображается артикулы кампании"
        assert find_element_on_page(driver, "//img[contains(@data-test,'campaign-articul-51349857')]"), "advertising_campaign_search: Не отображается картинка артикула"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-settings')]"), "advertising_campaign_search: Не отображается настройки кампании"
        assert find_element_on_page(driver, "//a[contains(@data-test,'campaign-import-settings')]"), "advertising_campaign_search: Не отображается импорт настроек"
        assert find_element_on_page(driver, "//span[contains(@data-test,'campaign-total-budget')]"), "advertising_campaign_search: Не отображается бюджет"
        assert find_element_on_page(driver, "//input[contains(@data-test,'campaign-target-place')]"), "advertising_campaign_search: Не отображается целевая позиция"
        assert find_element_on_page(driver, "//input[contains(@data-test,'campaign-max-price')]"), "advertising_campaign_search: Не отображается максимальная ставка"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-interval-1')]"), "advertising_campaign_search: Не отображается интервалы показов"
        assert find_element_on_page(driver, "//div[contains(@data-test,'campaign-master-phrase')]"), "advertising_campaign_search: Не отображается блок с мастер фразой"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-region')]"), "advertising_campaign_search: Не отображается регион управления"
        assert find_element_on_page(driver, "//div[contains(@data-test,'dropdown-selected')]"), "advertising_campaign_search: Не отображается дропдаун региона управления"
        assert find_element_on_page(driver, "//div[contains(@data-test,'search-wrapper')]"), "advertising_campaign_search: Не отображается поле поиска мастер-фразы"
        assert find_element_on_page(driver, "//input[contains(@data-test,'master-phrase-input')]"), "advertising_campaign_search: Не отображается поле ввода мастер-фразы"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-stat')]"), "advertising_campaign_search: Не отображается статистика по мастер фразе"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-frequency-month')]"), "advertising_campaign_search: Не отображается месяц в статистике"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-frequency-day')]"), "advertising_campaign_search: Не отображается день в статистике"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-delivery-time')]"), "advertising_campaign_search: Не отображается срок доставки в статистике"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-category')]"), "advertising_campaign_search: Не отображается приоритетная категория в статистике"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-compare')]"), "advertising_campaign_search: Не отображается вероятность попадания в рекламу"
        assert find_element_on_page(driver, "//div[contains(@data-test,'compare-your-product')]"), "advertising_campaign_search: Не отображается артикул в вероятности"
        assert find_element_on_page(driver, "//div[contains(@data-test,'compare-phrase-delivery-time')]"), "advertising_campaign_search: Не отображается макс. срок доставки в вероятности"
        assert find_element_on_page(driver, "//div[contains(@data-test,'compare-your-delivery-time')]"), "advertising_campaign_search: Не отображается макс срок доставки товара"
        assert find_element_on_page(driver, "//div[contains(@data-test,'compare-phrase-priority-category')]"), "advertising_campaign_search: Не отображается приоритетная категория в вероятности"
        assert find_element_on_page(driver, "//div[contains(@data-test,'compare-your-priority-category')]"), "advertising_campaign_search: Не отображается приоритет товара в вероятности"
        assert find_element_on_page(driver, "//div[contains(@data-test,'master-phrase-chance')]"), "advertising_campaign_search: Не отображается вероятность попадания"
        assert find_element_on_page(driver, "//div[contains(@data-test,'rate-city-tabs')]"), "advertising_campaign_search: Не отображается города в мастер фразе"
        assert find_element_on_page(driver, "//div[contains(@data-test,'rate-city-tab')]"), "advertising_campaign_search: Не отображается город в мастер фразе"
        assert find_element_on_page(driver, "//div[contains(@data-test,'rate-pages')]"), "advertising_campaign_search: Не отображается страницы в мастер фразе"
        assert find_element_on_page(driver, "//div[contains(@data-test,'table-master-phrase-rates')]"), "advertising_campaign_search: Не отображается таблица в мастер фразе"
        assert find_element_on_page(driver, "//input[contains(@data-test,'ctr-views')]"), "advertising_campaign_search: Не отображается показы в условиях управления"
        assert find_element_on_page(driver, "//input[contains(@data-test,'ctr-ctr')]"), "advertising_campaign_search: Не отображается CTR в условиях управления"
        assert find_element_on_page(driver, "//input[contains(@data-test,'ctr-cpc')]"), "advertising_campaign_search: Не отображается CPC в условиях управления"
        assert find_element_on_page(driver, "//input[contains(@data-test,'organic_place')]"), "advertising_campaign_search: Не отображается позиция в органике"
        assert find_element_on_page(driver, "//button[contains(@data-test,'btn-save-campaig')]"), "advertising_campaign_search: Не отображается кнопка сохранения кампании"
        assert find_element_on_page(driver, "//button[contains(@data-test,'btn-manage-campaign')]"), "advertising_campaign_search: Не отображается кнопка взыть под управление"

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
