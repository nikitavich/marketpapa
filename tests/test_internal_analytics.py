import json
import requests

from environment import token
from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestInternalAnalytics:

    # Проверка получения ключей для авторизованного пользователя
    def test_get_token(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # ПРОВЕРКИ
        assert response_status_code == 200, f"Wrong status code {response_status_code}"

    # Получить список заказов
    def test_get_order_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получить список заказов
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer " + str(token)
                                  }
                                  )
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_orders_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получить drop-list для фильтрации
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders-drop-list/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить заказы по недельной статистике
    def test_get_order_weekly_stat(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders_weekly_stat/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # API для внутреннего использования
    def test_order_count(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        data = json.dumps({
            "token_id": f"{ids}",
            "date_start": "2022-09-01",
            "date_finish": "2022-09-10",
            "nm_id_list": [51358326]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders_count/",
                                  data=data,
                                  headers={
                                      'Authorization': '4191e77c-1126-42b0-b41f-cb2315f97da3',
                                      'Content-Type': 'application/json'
                                  })
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить список продаж
    def test_get_sales_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/sales/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_sales_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/sales-drop-list/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить продажи по недельной статистике
    def test_get_sales_weekly_stat(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/sales_weekly_stat/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Подключение wb-token для внутренней аналитики
    def test_create_token(self):
        # Создание токена

        response = requests.post(
            "https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oG&token_name=new_wb_token_1",
            headers={"Authorization": "Bearer " + str(token)})
        print(response.status_code)
        print(response.text)
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']

        # Удаление токена

        response1 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/",
                                  headers={"Authorization": "Bearer " + str(token)})
        Assertions.assert_code_status(response1, 202)

    # Изменить название ключа
    def test_update_token(self):
        # Создание временного токена
        response = requests.post(
            "https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oG&token_name=new_wb_token_1",
            headers={
                "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']

        # Изменение имени токена
        data = json.dumps({
            "key_name": "Василий"
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.put(f"https://api.marketpapa.ru/api/internal-analytics/token/{self.token_id}/", data=data, headers=headers)
        Assertions.assert_code_status(response1, 202)

        # Удаление токена
        response2 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/",
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        Assertions.assert_code_status(response2, 202)

    # Удаление токена
    def test_delete_token(self):
        # Создание временного токена
        response = requests.post(
            "https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oG&token_name=new_wb_token_1",
            headers={
                "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']

        # Удаление токена
        response1 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/",
                                  headers={
                                      "Authorization": "Bearer " + str(token)})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 202)

    def test_update_new_token(self):
        # Обновление токена на новый формат
        url = "https://api.marketpapa.ru/api/internal-analytics/token/change/5673/"
        headers = {"Authorization": "Bearer " + str(token)}
        data = json.dumps({"key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oM"})
        response = requests.put(url=url, headers=headers, data=data)
        Assertions.assert_code_status(response, 202)

    # API для внутреннего использования
    def test_add_token_from_ads(self):
        data = json.dumps({
            "key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM1ZDFhMTNhLTI5MmItNGQxMS1iOTgxLTIyNTllNjY2YWIwMiJ9.qy_513Yd-r752RDKK-GxeyQxSvJzrX63_eeiepNt-oM",
            "user_id": 35
        })
        headers = {
            'Authorization': '4191e77c-1126-42b0-b41f-cb2315f97da3',
            'Content-Type': 'application/json'
        }
        response = requests.post("https://api.marketpapa.ru/api/internal-analytics/add_token_from_ads/", data=data, headers=headers)
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)

    # Получить список товаров на складе
    def test_get_stock_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение списка товаров
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/stocks/", data=data, headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Получить список товаров
    def test_get_product_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение списка товаров
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/get-products/", data=data,
                                  headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)


    # Получить drop-list для фильтрации в разделе мои товары
    def test_get_product_brand(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение списка товаров
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/products-drop-list/", data=data,
                                  headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Получить шаблон excel таблицы
    def test_get_sample(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение шаблона
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/get_excel_sample/", data=data,
                                  headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Получить список реализаций
    def test_get_realization_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение списка реализаций
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/realizations/", data=data,
                                  headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Получить список поставок
    def test_supplies_list(self,get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение списка реализаций
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supplies/", data=data,
                                  headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Получение списка артикулов в конкретной поставке
    def test_get_articles_list(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получение incomeId
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supplies/", data=data,
                                  headers=headers)
        parsed_response_text1 = response1.json()
        self.incomeId = parsed_response_text1['items'][0]['incomeId']

        # Получение списка артикулов
        response2 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/supplies/{self.incomeId}/", data=data, headers=headers)
        # ПРОВЕРКИ
        Assertions.assert_code_status(response2, 200)

    # Изменить себестоимость товара в поставке
    def test_change_cost_price(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supplies/", data=data,
                                  headers=headers)

        parsed_response_text1 = response1.json()
        incomeId = parsed_response_text1['items'][0]['incomeId']

        # Получение nmId и api_key
        response2 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/supplies/{incomeId}/", data=data, headers=headers)
        parsed_response_text2 = response2.json()
        api_key = parsed_response_text2['items'][0]['api_key']
        nmId = parsed_response_text2['items'][0]['nmId']

        # Изменение себестоимости
        data1 = json.dumps({
            "ids": [
                f"{ids}"
            ],
            "incomeId": f"{incomeId}",
            "items": [
                {
                    "nmId": f"{nmId}",
                    "costPrice": 5,
                    "api_key_id": f"{api_key}"
                }
            ]
        })
        headers1 = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response2 = requests.put("https://api.marketpapa.ru/api/internal-analytics/supplies/send-cost-price/", data=data1, headers=headers1)
        # ПРОВЕРКА
        Assertions.assert_code_status(response2, 202)

    # Получить drop-list для фильтрации в разделе поставки
    def test_list_of_supplies(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения drop-list
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supply-drop-list/", data=data,
                                  headers=headers)

        # Проверка
        Assertions.assert_code_status(response1, 200)

    # Получить drop-list для фильтрации в разделе поставки
    def test_list_of_supplies_by_supply(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supplies/", data=data,
                                  headers=headers)

        parsed_response_text1 = response1.json()
        incomeId = parsed_response_text1['items'][0]['incomeId']

        # Получение drop-list
        response2 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/supply-drop-list-by-income-id/{incomeId}/", data=data, headers=headers)
        # Проверки
        Assertions.assert_code_status(response2, 200)

    # Обновить себестоимость товаров в поставке из истории себестоимости
    def test_update_price_in_supply_history(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supplies/", data=data,
                                  headers=headers)

        parsed_response_text1 = response1.json()
        incomeId = parsed_response_text1['items'][0]['incomeId']

        # Обновить себестоимость товаров
        response2 = requests.put(
            f"https://api.marketpapa.ru/api/internal-analytics/cost-price-history/{incomeId}/?cost_price=7&for_all=false",
            data=data, headers=headers)
        # Проверки
        Assertions.assert_code_status(response2, 202)

    # Получить список по истории себестоимости
    def test_list_of_price_history(self, get_id_from_token):
        response_status_code, ids = get_id_from_token
        # Получения incomeId
        data = json.dumps({
            "ids": [
                f"{ids}"
            ]
        })
        headers = {
            'Authorization': "Bearer " + str(token),
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/supplies/", data=data,
                                  headers=headers)

        parsed_response_text1 = response1.json()
        incomeId = parsed_response_text1['items'][0]['incomeId']

        # Получение nmId
        response1 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/supplies/{incomeId}/",
                                  data=data, headers=headers)
        parsed_response_text1 = response1.json()
        nmId = parsed_response_text1['items'][0]['nmId']

        # Получение истории себестоимости
        response2= requests.post(f"https://api.marketpapa.ru/api/internal-analytics/cost-price-history/{nmId}/", data=data, headers=headers)
        # Проверки
        Assertions.assert_code_status(response2, 200)









