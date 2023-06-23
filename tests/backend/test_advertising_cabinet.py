import json

from lib.advertising_cabinet import send_request
from lib.base_case import delete_test_companies


class TestAdvertisingCabinet:
    def test_token(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/disabled_company/7045150/')

    # Отключение кампании
    def test_disabled_company(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/disabled_company/7045150/')
        assert response.status_code == 200, f'disabled_company статус: {response.status_code}'
        jsondata = response.json()
        assert jsondata['status'] == 'OK', "disabled_company status != OK"

    # История управления
    def test_price_history(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/price_history/7045150/?limit=100&page=1')
        assert response.status_code == 200, f'price_history статус: {response.status_code}'
        jsondata = response.json()
        assert jsondata['count'], 'Не работает price_history 1'
        assert jsondata['results'][0]['company'], 'Не работает price_history 2'

    # Минус-фразы
    def test_excluded_keywords(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/excluded_keywords/7045150/')
        assert response.status_code == 200, f'excluded_keyword code: {response.status_code}'

    # Информация о кампании
    def test_companies_info(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/companies_info/7045150/')
        assert response.status_code == 200, f'companies_info code: {response.status_code}'
        jsondata = response.json()
        assert jsondata["token"][
                   "phone_number"] == '9308689511', f'companies_info Wrong phone number! - {jsondata["token"]["phone_number"]}'

    # Плюс фразы кампании
    def test_company_keywords(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/company_keywords/7045150/')
        assert response.status_code == 200, f'company_keywords code: {response.status_code}'
        jsondata = response.json()
        assert jsondata[0]["keyword"] == 'брюки', f'company_keywords: Wrong company keyword! - {jsondata[0]["keyword"]}'

    # Рекламные кабинеты
    def test_supplier_id(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/company_keywords/7045150/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/supplier_id/update',
                                data=json.dumps({
                                    "id": 1,
                                    "supplier_name": "Наш Кабинет"
                                }))
        assert response.status_code == 200, f'supplier_id response code: {response.status_code}'

        # Все плюс-фразы

    def test_full_keywords(self):
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/full_keywords/7045150/')
        assert response.status_code == 200, f'full_keywords code: {response.status_code}'

    #
    def test_strong_excluded_words(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/strong_excluded_words/7045150')
        assert response.status_code == 200, f'strong_excluded_words code: {response.status_code}'
        response1 = send_request(method='post',
                                 url='https://api.marketpapa.ru/api/advertising-cabinet/strong_excluded_words/7045150',
                                 data=json.dumps({
                                     "keywords": [
                                         "куртка женская весна"
                                     ]
                                 }))
        assert response1.status_code == 204, f'strong_excluded_words 1 code: {response1.status_code}'

    def test_notification(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/notification/')
        assert response.status_code == 200, f'notification code: {response.status_code}'

    # Получить список категорий
    def test_supplier_subjects(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/supplier_subjects?token_id=1')
        assert response.status_code == 200, f'supplier_subjects code: {response.status_code}'

    # Обновление списка кампаний
    def test_update_companies(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/update_companies/?id=1')
        assert response.status_code == 200, f'update_companies code: {response.status_code}'

    # Получить номер телефона
    def test_get_phone_number(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/get_phone_number')
        assert response.status_code == 200, f'get_phone_number code: {response.status_code}'

    def test_extended_stat_by_keyword(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/extended_stat/by_keyword/7045150/')
        assert response.status_code == 200, f'extended_stat_by_keyword code: {response.status_code}'

    def test_manage_rules(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/manage_rules/7045150')
        assert response.status_code == 200, f'manage_rules code: {response.status_code}'
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/manage_rules/7045150',
                                data=json.dumps({
                                    "rules": [
                                        {
                                            "param_type": "CTR",
                                            "views": 1000,
                                            "value": 5
                                        }
                                    ]
                                }))
        assert response.status_code == 201, f'manage_rules response code: {response.status_code}'

    def test_delivery_time(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/delivery_time/7045136/')
        assert response.status_code == 200, f'delivery_time code: {response.status_code}'

    def test_compare_prices(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/compare_prices/7045150/')
        assert response.status_code == 200, f'compare_prices code: {response.status_code}'

    # def test_compare_card_prices(self):
    #     response = send_request(method='get',
    #                             url='https://api.marketpapa.ru/api/advertising-cabinet/compare_card_prices/7045150/')
    #     assert response.status_code == 200, f'compare_card_prices code: {response.status_code}'

    def test_keyword_hint(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/keyword_hint/?keyword=%D0%BA%D0%B0%D0%B1%D0%BB%D1%83%D0%BA%D0%B8&product_id=51358326')
        assert response.status_code == 200, f'keyword_hint code: {response.status_code}'

    def test_adv_products(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/adv_products?token_id=1')
        assert response.status_code == 200, f'adv_products code: {response.status_code}'

    def test_update_company(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/update_company/7045150')
        assert response.status_code == 200, f'update_company code: {response.status_code}'
        response1 = send_request(method='post',
                                 url='https://api.marketpapa.ru/api/advertising-cabinet/update_company/',
                                 data=json.dumps({
                                     "max_price": 500,
                                     "manage_type_max_price": 0,
                                     "manage_type_same_price": 0,
                                     "daily_budget": 1000,
                                     "intervals": [],
                                     "manage_type": 0,
                                     "target_place": "3",
                                     "company_id": 7045150,
                                     "city": 1,
                                     "keyword": [
                                         {
                                             "keyword": "брюки",
                                             "is_master": True
                                         },
                                         {
                                             "keyword": "еда",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "картошка",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "брюки женские",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "манты",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "ложка",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "кофта",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "капюшон",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "шоколад",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "батарейка",
                                             "is_master": False
                                         },
                                         {
                                             "keyword": "брюки женские утепленные",
                                             "is_master": False
                                         }
                                     ]
                                 }))
        assert response1.status_code == 201, f'update_company response code: {response1.status_code}'

    def test_enable_company(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/enable_company/7045150/')
        assert response.status_code == 200, f'enable_company code: {response.status_code}'
        response1 = send_request(method='get',
                                 url='https://api.marketpapa.ru/api/advertising-cabinet/disabled_company/7045150/')
        assert response1.status_code == 200, f'disable_company response code! - {response1.status_code}'
        jsondata = response1.json()
        assert jsondata['status'] == 'OK', f'Wrong status! - {jsondata["status"]}'

    def test_expenses(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/expenses?company_id=7045150')
        assert response.status_code == 200, f'expenses code: {response.status_code}'

    def test_get_copy_companies(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/get_copy_companies/?token_id=1')
        assert response.status_code == 200, f'get_copy_companies code: {response.status_code}'

    def test_extended_stat_by_date(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/extended_stat/by_date/7045150/?sales=1')
        assert response.status_code == 200, f'extended_stat_by_date code: {response.status_code}'

    def test_update_search_stat(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/update_search_stat/7045150')
        assert response.status_code == 200, f'update_search_stat code: {response.status_code}'

    def test_extended_stat_by_product(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/extended_stat/by_product/7045150/')
        assert response.status_code == 200, f'extended_stat_by_product code: {response.status_code}'

    def test_extended_stat_by_app(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/extended_stat/by_app/7045150/')
        assert response.status_code == 200, f'extended_stat_by_app code: {response.status_code}'

    def test_full_product_stat(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/full_product_stat?token_id=1')
        assert response.status_code == 200, f'full_product_stat code: {response.status_code}'

    def test_create_company(self):
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/create_company?token_id=1',
                                data=json.dumps({
                                    "company_type": "search",
                                    "data": {
                                        "campaignName": "тест создание",
                                        "groups": [
                                            {
                                                "nms": [
                                                    51349857
                                                ],
                                                "key_word": "Брюки"
                                            }
                                        ]
                                    }
                                }))
        assert response.status_code == 200, f'create_company code: {response.status_code}'

    def test_tg_accounts(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/tg_accounts')
        assert response.status_code == 200, f'tg_accounts code: {response.status_code}'

    def test_new_supplier_products(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/new_supplier_products?token_id=1&subject_id=11&type=search')
        assert response.status_code == 200, f'new_supplier_products code: {response.status_code}'

    def test_new_tg_link(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/new_tg_link')
        assert response.status_code == 201, f'new_tg_link code: {response.status_code}'

    def test_keyword_hint_full(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/keyword_hint_full?keyword=%D0%B1%D1%80%D1%8E%D0%BA%D0%B8')
        assert response.status_code == 200, f'keyword_hint_full code: {response.status_code}'
        jsondata = json.loads(response.text)
        assert jsondata['rows'], "Пустой ответ по keyword_hint_full"

    def test_delete_companies(self):
        arg = delete_test_companies()
        assert arg, "не сработал delete_companies"
