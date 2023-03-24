import json
from lib.internal_analytics import send_request


class TestInternalAnalytics:

    # Проверка получения ключей для авторизованного пользователя
    def test_get_token(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # ПРОВЕРКИ
        assert response_status_code == 200, f"Wrong status code {response_status_code}"

    # Получить список заказов
    def test_get_order_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        print(ids)
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/orders/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_orders_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/orders-drop-list/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить заказы по недельной статистике
    def test_get_order_weekly_stat(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/orders_weekly_stat/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # API для внутреннего использования
    def test_order_count(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/orders_count/',
                                data=json.dumps({
                                    "token_id": f"{ids}",
                                    "date_start": "2022-09-01",
                                    "date_finish": "2022-09-10",
                                    "nm_id_list": [51358326]
                                }),
                                headers={
                                    'Authorization': '4191e77c-1126-42b0-b41f-cb2315f97da3',
                                    'Content-Type': 'application/json'
                                }
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить список продаж
    def test_get_sales_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/sales/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_sales_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/sales-drop-list/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить продажи по недельной статистике
    def test_get_sales_weekly_stat(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/sales_weekly_stat/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                }))
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Подключение wb-token для внутренней аналитики
    def test_create_token(self):
        # Создание токена
        response = send_request(method='post',
                                url='''https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGciOiJIU
                                zI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2Y
                                WIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oG&token_name=new_wb_token_1''',
                                )
        assert response.status_code == 201, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']
        # Удаление токена
        response1 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/',
                                 )
        assert response1.status_code == 202, f'Wrong response code! - {response1.status_code}'

    # Изменить название ключа
    def test_update_token(self):
        # Создание временного токена
        response = send_request(method='post',
                                url='''https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGciOiJIU
                                zI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2Y
                                WIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oG&token_name=new_wb_token_1''',
                                )
        assert response.status_code == 201, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']
        # Изменение имени токена
        response1 = send_request(method='put',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/token/{self.token_id}/',
                                 data=json.dumps({
                                     "key_name": "Василий"
                                 })
                                 )
        assert response1.status_code == 202, f'Wrong response code! - {response1.status_code}'
        # Удаление токена
        response2 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/',
                                 )
        assert response2.status_code == 202, f'Wrong response code! - {response2.status_code}'

    # Удаление токена
    def test_delete_token(self):
        # Создание токена
        response = send_request(method='post',
                                url='''https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGciOiJIU
                                zI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2Y
                                WIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oG&token_name=new_wb_token_1''',
                                )
        assert response.status_code == 201, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']
        # Удаление токена
        response1 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/',
                                 )
        assert response1.status_code == 202, f'Wrong response code! - {response1.status_code}'

    # API для внутреннего использования
    def test_add_token_from_ads(self):
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/add_token_from_ads/',
                                data=json.dumps({
                                    "key": '''eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmI
                                    tNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oM''',
                                    "user_id": 35
                                }),
                                headers={
                                    'Authorization': '4191e77c-1126-42b0-b41f-cb2315f97da3',
                                    'Content-Type': 'application/json'
                                }
                                )
        assert response.status_code == 201, f'Wrong response code! - {response.status_code}'

    # Получить список товаров
    def test_get_product_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/get-products/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить drop-list для фильтрации в разделе мои товары
    def test_get_product_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/products-drop-list/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить шаблон excel таблицы
    def test_get_sample(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/get_excel_sample/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить список реализаций
    def test_get_realization_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/realizations/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить список поставок
    def test_supplies_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получение списка артикулов в конкретной поставке
    def test_get_articles_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        parsed_response_text1 = response.json()
        self.incomeId = parsed_response_text1['items'][0]['incomeId']
        response1 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeId}/',
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ]
                                 })
                                 )
        assert response1.status_code == 200, f'Wrong response code! - {response1.status_code}'

    # Изменить себестоимость товара в поставке
    def test_change_cost_price(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.incomeId = parsed_response_text['items'][0]['incomeId']
        # Получение nmId и api_key
        response1 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeId}/',
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ]
                                 })
                                 )
        assert response1.status_code == 200, f'Wrong response code! - {response1.status_code}'
        parsed_response_text1 = response1.json()
        api_key = parsed_response_text1['items'][0]['api_key']
        nmId = parsed_response_text1['items'][0]['nmId']
        # Изменение себестоимости
        response2 = send_request(method='put',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/supplies/send-cost-price/',
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ],
                                     "incomeId": f"{self.incomeId}",
                                     "items": [
                                         {
                                             "nmId": f"{nmId}",
                                             "costPrice": 5,
                                             "api_key_id": f"{api_key}"
                                         }
                                     ]
                                 })
                                 )
        assert response2.status_code == 202, f'Wrong response code! - {response2.status_code}'

    # Получить drop-list для фильтрации в разделе поставки
    def test_list_of_supplies(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'

    # Получить drop-list для фильтрации в разделе поставки
    def test_list_of_supplies_by_supply(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.incomeId = parsed_response_text['items'][0]['incomeId']
        # Получение drop-list
        response1 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/supply-drop-list-by-income-id/{self.incomeId}/',
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ]
                                 })
                                 )
        assert response1.status_code == 200, f'Wrong response code! - {response1.status_code}'

    # Обновить себестоимость товаров в поставке из истории себестоимости
    def test_update_price_in_supply_history(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.incomeId = parsed_response_text['items'][0]['incomeId']
        # Обновить себестоимость товаров
        response1 = send_request(method='put',
                                 url=f"https://api.marketpapa.ru/api/internal-analytics/cost-price-history/{self.incomeId}/?cost_price=7&for_all=false",
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ]
                                 })
                                 )
        assert response1.status_code == 202, f'Wrong response code! - {response1.status_code}'

    # Получить список по истории себестоимости
    def test_list_of_price_history(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        response = send_request(method='post',
                                url='https://api.marketpapa.ru/api/internal-analytics/supplies/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ]
                                })
                                )
        assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
        parsed_response_text = response.json()
        self.incomeId = parsed_response_text['items'][0]['incomeId']
        # Получение nmId
        response1 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeId}/',
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ]
                                 })
                                 )
        assert response1.status_code == 200, f'Wrong response code! - {response1.status_code}'
        parsed_response_text1 = response1.json()
        nmId = parsed_response_text1['items'][0]['nmId']
        # Получение истории себестоимости
        response2 = send_request(method='post',
                                 url=f'https://api.marketpapa.ru/api/internal-analytics/cost-price-history/{nmId}/',
                                 data=json.dumps({
                                     "ids": [
                                         f"{ids}"
                                     ]
                                 })
                                 )
        assert response2.status_code == 200, f'Wrong response code! - {response2.status_code}'

    # Отправить себестоимость
    def test_send_cost_price(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='put',
                                url='https://api.marketpapa.ru/api/internal-analytics/product/send-cost-price/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ],
                                    "items": [
                                        {
                                            "nmId": 25629612,
                                            "costPrice": 20,
                                            "api_key_id": 15625
                                        }
                                    ]
                                }))
        assert response.status_code == 202, f'Wrong response code! - {response.status_code}'

    # самовыкуп для товара
    def test_orders_self_purchase(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = send_request(method='put',
                                url='https://api.marketpapa.ru/api/internal-analytics/orders-self-purchase/',
                                data=json.dumps({
                                    "ids": [
                                        f"{ids}"
                                    ],
                                    "items": [
                                        {
                                            "odid": 9002248958959,
                                            "self_purchase": True
                                        }
                                    ]
                                }))
        assert response.status_code == 202, f'Wrong response code! - {response.status_code}'

