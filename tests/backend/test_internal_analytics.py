import json
import requests


class TestInternalAnalytics:

    def send_request(self, method, url, payload=None, cookies=None, headers=None):
        with open('../wb_token.txt', 'r') as wb_token_from_file:
            wb_token = str(wb_token_from_file.readline().rstrip('\n'))
            wb_token_from_file.close()
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
                'Accept': '*/*',
                'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Referer': 'https://dev.marketpapa.ru/',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {wb_token}',
                'Origin': 'https://dev.marketpapa.ru',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'TE': 'trailers'
            }
        url = url
        response = None
        if method == 'GET':
            response = requests.get(url=url, headers=headers, cookies=cookies)
            return response
        if method == "PUT":
            response = requests.put(url=url, headers=headers, cookies=cookies, data=payload)
            return response
        if method == "POST":
            response = requests.post(url=url, headers=headers, cookies=cookies, data=payload)
            return response

    # Проверка получения ключей для авторизованного пользователя
    def test_get_token(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # ПРОВЕРКИ
        assert response_status_code == 200, f"Не удалось получить айди токена, статус {response_status_code}"

    # Получить список заказов
    def test_get_order_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST", url='https://api.marketpapa.ru/api/internal-analytics/orders/',
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     }))
        assert response.status_code == 200, f"Не удалось получить список заказов, статус {response.status_code}"

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_orders_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url='https://api.marketpapa.ru/api/internal-analytics/orders-drop-list/',
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     }))
        assert response.status_code == 200, f"Не удалось получить drop-list для фильтрации в разделе продажи, статус {response.status_code}"

    # Получить заказы по недельной статистике
    def test_get_order_weekly_stat(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url='https://api.marketpapa.ru/api/internal-analytics/orders_weekly_stat/',
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     }))
        assert response.status_code == 200, f"Не удалось получить заказы по недельной статистике, статус {response.status_code}"

    # API для внутреннего использования
    def test_order_count(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url='https://api.marketpapa.ru/api/internal-analytics/orders_count/',
                                     payload=json.dumps({
                                         "token_id": f"{ids}",
                                         "date_start": "2022-09-01",
                                         "date_finish": "2022-09-10",
                                         "nm_id_list": [51358326]
                                     }
                                     ),
                                     headers={
                                         'Authorization': '4191e77c-1126-42b0-b41f-cb2315f97da3',
                                         'Content-Type': 'application/json'
                                     }
                                     )

        assert response.status_code == 200, f"Не удалось получить API для внутреннего использования, статус {response.status_code}"

        # Получить список продаж

    def test_get_sales_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url='https://api.marketpapa.ru/api/internal-analytics/sales/',
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     }))
        assert response.status_code == 200, f"Не удалось получить список продаж, статус {response.status_code}"

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_sales_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url='https://api.marketpapa.ru/api/internal-analytics/sales-drop-list/',
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     }))
        assert response.status_code == 200, f"""Не удалось получить drop-list для фильтрации в разделе продажи,
                                                статус {response.status_code}"""

    # Получить продажи по недельной статистике
    def test_get_sales_weekly_stat(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url='https://api.marketpapa.ru/api/internal-analytics/sales_weekly_stat/',
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     }))
        assert response.status_code == 200, f"""Не удалось получить продажи по недельной статистике,
                                                статус {response.status_code}"""

    # Подключение wb-token для внутренней аналитики
    def test_create_token(self):
        response = self.send_request(method="POST",
                                     url=f"""https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbG
                                     ciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjUyMWUyYTZiLTU2YzAtNDRhMC1iZjY1
                                     LTJkYzlmYmYyNDJkZCJ9.rlYSdPbY1fueQe-O0ryzj19hSXkNOwvzSWk47BASzU8&token_name=123
                                     45""",
                                     payload=json.dumps({}))
        assert response.status_code == 201, f'Не удалось создать токен, статус {response.status_code}'
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']
        response1 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/")
        assert response1.status_code == 202, f'Не удалось удалить токен, статус {response1.status_code}'

    # Изменить название ключа
    def test_update_token(self):
        # Создание временного токена
        response = self.send_request(method="POST",
                                     url=f"""https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGci
                                     OiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjUyMWUyYTZiLTU2YzAtNDRhMC1iZjY1LTJk
                                     YzlmYmYyNDJkZCJ9.rlYSdPbY1fueQe-O0ryzj19hSXkNOwvzSWk47BASzU8&token_name=12345""",
                                     payload=json.dumps({}))
        assert response.status_code == 201, f'Не удалось создать токен, статус {response.status_code}'
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']
        # Изменение имени токена
        response1 = self.send_request(method="PUT",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/token/{self.token_id}/",
                                      payload=json.dumps({
                                          "key_name": "Василий"
                                      }))
        assert response1.status_code == 202, f'Не удалось изменить имя токена, статус {response1.status_code}'
        # Удаление токена
        response2 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/")
        assert response2.status_code == 202, f'Не удалось удалить токен, статус {response2.status_code}'

    def test_delete_token(self):
        response = self.send_request(method="POST",
                                     url=f"""https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbG
                                             ciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjUyMWUyYTZiLTU2YzAtNDRhMC1iZjY1
                                             LTJkYzlmYmYyNDJkZCJ9.rlYSdPbY1fueQe-O0ryzj19hSXkNOwvzSWk47BASzU8&token_name=123
                                             45""",
                                     payload=json.dumps({}))
        assert response.status_code == 201, f'Не удалось создать токен, статус {response.status_code}'
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']
        response1 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/")
        assert response1.status_code == 202, f'Не удалось удалить токен, статус {response1.status_code}'

    # API для внутреннего использования
    def test_add_token_from_ads(self):
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/add_token_from_ads/",
                                     payload=json.dumps({
                                         "key": '''eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLT
                                         I5MmItNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiep
                                         Nt-oM''',
                                         "user_id": 35
                                     }),
                                     headers={
                                         'Authorization': '4191e77c-1126-42b0-b41f-cb2315f97da3',
                                         'Content-Type': 'application/json'
                                     }
                                     )
        assert response.status_code == 201, f'Не удалось API для внутреннего использования, статус {response.status_code}'

    # Получить список товаров на складе (не используется)
    # def test_get_stock_list(self, get_id_from_token):
    #     response_status_code, ids = get_id_from_token
    #     response = self.send_request(method="POST",
    #                                  url=f"https://api.marketpapa.ru/api/internal-analytics/stocks/",
    #                                  payload=json.dumps({
    #                                      "ids": [
    #                                          f"{ids}"
    #                                      ]
    #                                  })
    #                                  )
    #     assert response.status_code == 200, f'Не удалось создать токен, статус {response.status_code}'

    # Получить список товаров
    def test_get_product_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/get-products/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список товаров, статус {response.status_code}'

    # Получить drop-list для фильтрации в разделе мои товары
    def test_get_product_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/products-drop-list/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить drop-list для фильтрации в разделе мои товары, статус {response.status_code}'

    # Получить шаблон excel таблицы
    def test_get_sample(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/get_excel_sample/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить шаблон excel таблицы, статус {response.status_code}'

    # Получить список реализаций
    def test_get_realization_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/realizations/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список реализаций, статус {response.status_code}'

    # Получить список поставок
    def test_supplies_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список поставок, статус {response.status_code}'

    # Получение списка артикулов в конкретной поставке
    def test_get_articles_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список поставок, статус {response.status_code}'
        parsed_response_text1 = response.json()
        self.incomeid = parsed_response_text1['items'][0]['incomeId']
        # Получение списка артикулов
        response1 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeid}/",
                                      payload=json.dumps({
                                          "ids": [
                                              f"{ids}"
                                          ]
                                      })
                                      )
        assert response1.status_code == 200, f'Не удалось получить список артикулов, статус {response1.status_code}'

    # Изменить себестоимость товара в поставке
    def test_change_cost_price(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список поставок, статус {response.status_code}'
        parsed_response_text1 = response.json()
        self.incomeid = parsed_response_text1['items'][0]['incomeId']
        # Получение nmId и api_key
        response1 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeid}/",
                                      payload=json.dumps({
                                          "ids": [
                                              f"{ids}"
                                          ]
                                      })
                                      )
        assert response1.status_code == 200, f'Не удалось получить список артикулов, статус {response1.status_code}'
        parsed_response_text1 = response1.json()
        api_key = parsed_response_text1['items'][0]['api_key']
        nmId = parsed_response_text1['items'][0]['nmId']
        # Изменение себестоимости
        response2 = self.send_request(method="PUT",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/send-cost-price/",
                                      payload=json.dumps({
                                          "ids": [
                                              f"{ids}"
                                          ],
                                          "incomeId": f"{self.incomeid}",
                                          "items": [
                                              {
                                                  "nmId": f"{nmId}",
                                                  "costPrice": 5,
                                                  "api_key_id": f"{api_key}"
                                              }
                                          ]
                                      })
                                      )
        assert response2.status_code == 202, f'Не удалось получить список артикулов, статус {response2.status_code}'

    # Получить drop-list для фильтрации в разделе поставки
    def test_list_of_supplies(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/supply-drop-list/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список поставок, статус {response.status_code}'

    # Получить drop-list для фильтрации в разделе поставки (не используется)
    # def test_list_of_supplies_by_supply(self, get_id_from_token):
    #     response_status_code, ids = get_id_from_token
    #     # Получения incomeId
    #     response = self.send_request(method="POST",
    #                                  url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/",
    #                                  payload=json.dumps({
    #                                      "ids": [
    #                                          f"{ids}"
    #                                      ]
    #                                  })
    #                                  )
    #     assert response.status_code == 200, f'Не удалось получить incomeId, статус {response.status_code}'
    #     parsed_response_text1 = response.json()
    #     self.incomeid = parsed_response_text1['items'][0]['incomeId']
    #     # Получение drop-list
    #     response = self.send_request(method="POST",
    #                                  url=f"""https://api.marketpapa.ru/api/internal-analytics/
    #                                  supply-drop-list-by-income-id/{self.incomeid}/""",
    #                                  payload=json.dumps({
    #                                      "ids": [
    #                                          f"{ids}"
    #                                      ]
    #                                  })
    #                                  )
    #     assert response.status_code == 200, f'Не удалось получить drop-list, статус {response.status_code}'

    # Обновить себестоимость товаров в поставке из истории себестоимости (не актуально)
    # def test_update_price_in_supply_history(self, get_id_from_token):
    #     response_status_code, ids = get_id_from_token
    #     # Получения incomeId
    #     response = self.send_request(method="POST",
    #                                  url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/",
    #                                  payload=json.dumps({
    #                                      "ids": [
    #                                          f"{ids}"
    #                                      ]
    #                                  })
    #                                  )
    #     assert response.status_code == 200, f'Не удалось получить список поставок, статус {response.status_code}'
    #     parsed_response_text1 = response.json()
    #     self.incomeid = parsed_response_text1['items'][0]['incomeId']
    #     print(self.incomeid)
    #     # Обновить себестоимость товаров
    #     response1 = self.send_request(method="POST",
    #                                  url=f"""https://api.marketpapa.ru/api/internal-analytics/
    #                                  cost-price-history/{self.incomeid}/?cost_price=8&for_all=false""",
    #                                  payload=json.dumps({
    #                                      "ids": [
    #                                          f"{ids}"
    #                                      ]
    #                                  })
    #                                  )
    #     assert response1.status_code == 202, f'Не удалось получить список поставок, статус {response1.status_code}'

    # Получить список по истории себестоимости
    def test_list_of_price_history(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        response = self.send_request(method="POST",
                                     url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/",
                                     payload=json.dumps({
                                         "ids": [
                                             f"{ids}"
                                         ]
                                     })
                                     )
        assert response.status_code == 200, f'Не удалось получить список поставок, статус {response.status_code}'
        parsed_response_text1 = response.json()
        self.incomeid = parsed_response_text1['items'][0]['incomeId']
        # Получение nmId
        response1 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeid}/",
                                      payload=json.dumps({
                                          "ids": [
                                              f"{ids}"
                                          ]
                                      })
                                      )
        assert response1.status_code == 200, f'Не удалось получить список поставок, статус {response1.status_code}'
        parsed_response_text1 = response1.json()
        nmid = parsed_response_text1['items'][0]['nmId']
        # Получение истории себестоимости
        response2 = self.send_request(method="POST",
                                      url=f"https://api.marketpapa.ru/api/internal-analytics/cost-price-history/{nmid}/",
                                      payload=json.dumps({
                                          "ids": [
                                              f"{ids}"
                                          ]
                                      })
                                      )
        assert response2.status_code == 200, f'Не удалось получить истории себестоимости, статус {response2.status_code}'
