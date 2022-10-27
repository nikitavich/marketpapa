import json
from lib.base_case import BaseCase
from lib.assertions import Assertions
import requests

class TestAdvertisingEndpointsWB(BaseCase):
    def test_adv_endpoint_1(self):
        self.wb_token = f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODYwMjkxMX0.KimdYfTB9Yn2FMcvEVu3RF-Q91cbqyYMoMl66yDbU3A"
        self.supplier_id = f"234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        self.wb_user_id = f"87766907"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
            "Cookie": f"WBToken={self.wb_token}; x-supplier-id-external={self.supplier_id}",
            "X-User-Id": f"{self.wb_user_id}",
        }
        response = requests.get("https://cmp.wildberries.ru/campaigns/list/all?type=auction", headers=headers)
        Assertions.assert_code_status(response, 200)

    def test_adv_endpoint_2(self):
        self.wb_token = f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODYwMjkxMX0.KimdYfTB9Yn2FMcvEVu3RF-Q91cbqyYMoMl66yDbU3A"
        self.supplier_id = f"234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        self.wb_user_id = f"87766907"
        self.company_id = f"2798829"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
            "Cookie": f"WBToken={self.wb_token}; x-supplier-id-external={self.supplier_id}",
            "X-User-Id": f"{self.wb_user_id}",
        }
        response = requests.get(f"https://cmp.wildberries.ru/campaigns/list/all/edit/search/{self.company_id}", headers=headers)
        Assertions.assert_code_status(response, 200)

    def test_adv_endpoint_3(self):
        self.wb_token = f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODYwMjkxMX0.KimdYfTB9Yn2FMcvEVu3RF-Q91cbqyYMoMl66yDbU3A"
        self.supplier_id = f"234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        self.wb_user_id = f"87766907"
        self.company_id = f"2798829"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
            "Cookie": f"WBToken={self.wb_token}; x-supplier-id-external={self.supplier_id}",
            "X-User-Id": f"{self.wb_user_id}",
        }
        response = requests.get(f"https://cmp.wildberries.ru/campaigns/list/all/edit/carousel-auction/{self.company_id}",
                                headers=headers)
        Assertions.assert_code_status(response, 200)




