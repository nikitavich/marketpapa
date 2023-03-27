import json
from lib.advertising_cabinet import send_request


class TestAdvertisingCabinet:
    # Отключение кампании
    def test_disabled_company(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/disabled_company/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        jsondata = response.json()
        assert jsondata['status'] == 'OK', f'Wrong status! - {jsondata["status"]}'

    # История управления
    def test_price_history(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/price_history/3499821/?limit=100&page=1')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        jsondata = response.json()
        assert type(jsondata['count']) == int, f'Wrong count! - {jsondata["count"]}'

    # Минус-фразы
    def test_excluded_keywords(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/excluded_keywords/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        jsondata = response.json()
        assert jsondata["result"][0] == 'одежда'

    # Информация о кампании
    def test_companies_info(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/companies_info/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        jsondata = response.json()
        assert jsondata["token"][
                   "phone_number"] == '9308689511', f'Wrong phone number! - {jsondata["token"]["phone_number"]}'

    # Плюс фразы кампании
    def test_company_keywords(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/company_keywords/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        jsondata = response.json()
        assert jsondata[0]["keyword"] == 'брюки', f'Wrong company keyword! - {jsondata[0]["keyword"]}'

    # Рекламные кабинеты
    def test_supplier_id(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/company_keywords/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/supplier_id/update',
                                data=json.dumps({
                                    "id": 1,
                                    "supplier_name": "Наш Кабинет"
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

        # Все плюс-фразы

    def test_full_keywords(self):
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/full_keywords/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    #
    def test_strong_excluded_words(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/strong_excluded_words/3499821')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        response1 = send_request(method='post',
                                 url='https://api.marketpapa.ru/api/advertising-cabinet/strong_excluded_words/3499821',
                                 data=json.dumps({
                                     "keywords": [
                                         "куртка женская весна"
                                     ]
                                 }))
        assert response1.status_code == 204, f'Wrong response code! - {response1.status_code}'

    def test_notification(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/notification/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить список категорий
    def test_supplier_subjects(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/supplier_subjects?token_id=1')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Обновление списка кампаний
    def test_update_companies(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/update_companies/?id=1')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить номер телефона
    def test_get_phone_number(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/get_phone_number')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    def test_extended_stat_by_keyword(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/extended_stat/by_keyword/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    def test_manage_rules(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/manage_rules/3499821')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/manage_rules/3499821',
                                data=json.dumps({
                                    "rules": [
                                        {
                                            "param_type": "CTR",
                                            "views": 1000,
                                            "value": 5
                                        }
                                    ]
                                }))
        assert response.status_code == 201, f'Wrong response code! - {response.status_code}'

    def test_delivery_time(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/delivery_time/3501540/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    def test_compare_prices(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/compare_prices/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    def test_compare_card_prices(self):
        response = send_request(method='get',
                                url='https://api.marketpapa.ru/api/advertising-cabinet/compare_card_prices/3499821/')
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'


