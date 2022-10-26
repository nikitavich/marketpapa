import json

import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure
import requests


class TestInternalAnalytics(BaseCase):

    # Получить список ключей для авторизованного пользователя
    def test_get_token(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})

        parsed_response_text = response.json()
        x = parsed_response_text['items'][0]
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 200)
        assert "id" in x, "ошибка"

    # Получить список заказов
    def test_get_order_list(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_orders_brand(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders-drop-list/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить заказы по недельной статистике
    def test_get_order_weekly_stat(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders_weekly_stat/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # API для внутреннего использования
    def test_order_count(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "token_id": f"{self.ids}",
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
    def test_get_sales_list(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/sales/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить drop-list для фильтрации в разделе продажи
    def test_get_sales_brand(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/sales-drop-list/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Получить продажи по недельной статистике
    def test_get_sales_weekly_stat(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/sales_weekly_stat/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 200)

    # Подключение wb-token для внутренней аналитики
    def test_create_token(self):
        # Создание токена

        response = requests.post(
            "https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=YjVlY2U0OTEtYmMzYS00YzQ1LWI4YmMtNWI5NzFhNzk2ZmMZ&token_name=new_wb_token_1",
            headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']

        # Удаление токена

        response1 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/",
                                  headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        Assertions.assert_code_status(response1, 202)

    # Изменить название ключа
    def test_update_token(self):
        # Создание временного токена
        response = requests.post(
            "https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=YjVlY2U0OTEtYmMzYS00YzQ1LWI4YmMtNWI5NzFhNzk2ZmMZ&token_name=new_wb_token_1",
            headers={
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']

        # Изменение имени токена
        data = json.dumps({
            "key_name": "Василий"
        })
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k',
            'Content-Type': 'application/json'
        }
        response1 = requests.put(f"https://api.marketpapa.ru/api/internal-analytics/token/{self.token_id}/", data=data, headers=headers)
        Assertions.assert_code_status(response1, 202)

        # Удаление токена
        response2 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/",
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        Assertions.assert_code_status(response2, 202)

    # Удаление токена
    def test_delete_token(self):
        # Создание временного токена
        response = requests.post(
            "https://api.marketpapa.ru/api/internal-analytics/token/?wb_token=YjVlY2U0OTEtYmMzYS00YzQ1LWI4YmMtNWI5NzFhNzk2ZmMZ&token_name=new_wb_token_1",
            headers={
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response, 201)
        parsed_response_text = response.json()
        self.token_id = parsed_response_text['id']

        # Удаление токена
        response1 = requests.post(f"https://api.marketpapa.ru/api/internal-analytics/delete_token/{self.token_id}/",
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        # ПРОВЕРКИ
        Assertions.assert_code_status(response1, 202)

    # API для внутреннего использования
    def test_add_token_from_ads(self):
        data = json.dumps({
            "key": "YjVlY2U0OTEtYmMzYS00YzQ1LWI4YmMtNWI5NzFhNzk2ZmMz",
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
    def test_get_stock_list(self):
        # Получение ids токена
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']


        # Получение списка товаров
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k',
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/stocks/", data=data, headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Получить список товаров
    def test_get_product_list(self):
        # Получение ids токена
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']

        # Получение списка товаров
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k',
            'Content-Type': 'application/json'
        }
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/get-products/", data=data,
                                  headers=headers)
        # Проверки
        Assertions.assert_code_status(response1, 200)

    # Изменить себестоимость товара в поставке
    def test_send_cost_price(self):
        # Получение ids токена
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        self.ids = parsed_response_text['items'][0]['id']
        data = json.dumps({
            "ids": [
                f"{self.ids}"
            ]
        })

        # Получение nmId
        response1 = requests.post("https://api.marketpapa.ru/api/internal-analytics/orders/",
                                  data=data,
                                  headers={
                                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response1.json()
        self.nmId = parsed_response_text['items'][0]['nmId']

        # Изменить себестоимость товара
        data1 = json.dumps({
              "ids": [
                f"{self.ids}"
              ],
              "incomeId": 0,
              "items": [
                {
                  "nmId": f"{self.nmId}",
                  "costPrice": 0,
                  "api_key_id": 0
                }
              ]
            })
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k',
            'Content-Type': 'application/json'
        }
        response2 = requests.put("https://api.marketpapa.ru/api/internal-analytics/product/send-cost-price/", data=data1, headers=headers)
        print(response2.status_code)
        print(response2.text)

