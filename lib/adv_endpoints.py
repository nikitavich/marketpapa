import asyncio
import json
import random
import time
import datetime

from fake_useragent import UserAgent
import requests

import settings
from lib.base_case import BaseCase
from wb_errors import TooManyTime, InvalidWBToken


class AdvEndpoints:
    referer_types = {
        1: "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
        2: "https://cmp.wildberries.ru/campaigns/list/all/edit/search/{company_id}",
        3: "https://cmp.wildberries.ru/campaigns/list/all/edit/carousel-auction/{company_id}",
        4: "https://cmp.wildberries.ru/statistics",
        5: "https://cmp.wildberries.ru/finance/upd"}

    def send_request(self, method, url, referer, data=None, json=None):
        with open('../wb_token.txt', 'r') as wb_token_from_file:
            wb_token = str(wb_token_from_file.readline().rstrip('\n'))
            wb_token_from_file.close()
        url = url
        headers = {
            "Accept": "application/json, text/plain, */*",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            # "Accept-Language": "en-GB,en;q=0.9",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Connection": "keep-alive",
            "Referer": referer,
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={settings.supplier_id}",
            "X-User-Id": f"{settings.wb_user_id}",
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": settings.supplier_id}
        response = None
        count = 0
        h = 0
        while count < 20:
            if method == "get":
                response = requests.get(url=url, headers=headers, cookies=cookies)
                if response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                if response.status_code in [401, 403]:
                    h += 1
                    if h == 2:
                        BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
                    continue
                return response
            if method == "put":
                response = requests.put(url=url, headers=headers, cookies=cookies, data=data)
                if response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(2)
                    continue
                if response.status_code in [204]:
                    count = count + 1
                    time.sleep(2)
                    continue
                if response.status_code in [401, 403]:
                    h += 1
                    if h == 2:
                        BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
                    continue
                return response
            if method == "post":
                response = requests.post(url=url, headers=headers, cookies=cookies, json=json)
                if response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(2)
                    continue
                if response.status_code in [401, 403]:
                    h += 1
                    if h == 2:
                        BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
                    continue
                return response

    def get_keywords_new(self, company_id):
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/words"
        response = AdvEndpoints().send_request(method="get", url=url,
                                               referer=referer_type.format(company_id=company_id))
        return response

    def get_company_info(self, company_id):
        referer_type = self.referer_types[4]
        url = f"https://cmp.wildberries.ru/backend/api/v1/atrevd?advert-id={company_id}"
        response = AdvEndpoints().send_request(method="get", url=url,
                                               referer=referer_type.format(company_id=company_id))
        return response

    def get_placement_info(self, company_id):
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        response = AdvEndpoints().send_request(method="get", url=url,
                                               referer=referer_type.format(company_id=company_id))
        return response

    def set_excluded_keywords(self, company_id, keywords: list):
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/set-excluded"
        response = AdvEndpoints().send_request(method="post", url=url,
                                               referer=referer_type.format(company_id=company_id),
                                               json={"excluded": keywords})
        return response

    def set_new_price(self, company_id, price, placement=None):
        referer_type = self.referer_types[2]
        if not placement:
            response = AdvEndpoints().get_placement_info(company_id)
        placement = response.json()
        price = placement["place"][0]["price"]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/save"
        response1 = AdvEndpoints().send_request(
            method="put",
            url=url,
            referer=referer_type.format(company_id=company_id),
            data=json.dumps(placement).encode("utf-8")
        )
        return response1

    def stop_adv_company(self, company_id):
        response = AdvEndpoints().get_placement_info(company_id=company_id)
        placement = response.json()
        current_status = placement['status']
        if current_status == 11:
            AdvEndpoints().start_adv_company(company_id=company_id)
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/pause"
        response = AdvEndpoints().send_request(
            method="get",
            url=url,
            referer=referer_type.format(company_id=company_id),
        )
        return response

    def get_budget(self, company_id, placement=None):
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/budget"
        response = None
        if not placement:
            response = AdvEndpoints().get_placement_info(company_id)
        placement = response.json()
        response1 = AdvEndpoints().send_request(
            method="get", url=url, referer=referer_type.format(company_id=company_id)
        )
        data = response1.json()
        data["daily_budget"] = placement.get("budget").get("dailyMax")
        return response1, data

    def deposit(self, company_id, deposit, balance_type):
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/budget/deposit"
        response = AdvEndpoints().send_request(
            method="post",
            url=url,
            referer=referer_type.format(company_id=company_id),
            json={"sum": deposit, "type": balance_type},
        )
        return response

    # Пока не автоматизируем (затрагивает бюджет)
    def start_adv_company(self, company_id, placement=None, budget=None):
        referer_type = self.referer_types[2]
        response = None
        response1 = None
        if not placement:
            response = AdvEndpoints().get_placement_info(company_id=company_id)
        if not budget:
            response1, data = AdvEndpoints().get_budget(company_id=company_id)
        placement = response.json()
        budget = response1.json()
        total_budget = budget.get("total")
        placement["budget"]["total"] = total_budget

        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        response2 = AdvEndpoints().send_request(
            method="put",
            url=url,
            referer=referer_type.format(company_id=company_id),
            data=json.dumps(placement).encode("utf-8"),
        )
        if response2.status_code == 400:
            response = AdvEndpoints().deposit(company_id=company_id, deposit=100, balance_type=1)
            time.sleep(5)
            response3 = AdvEndpoints().send_request(
                method="put",
                url=url,
                referer=referer_type.format(company_id=company_id),
                data=json.dumps(placement).encode("utf-8"),
            )
            return response3
        else:
            return response2

    def get_card_budget(self, company_id, placement=None):
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/budget"
        if not placement:
            response = AdvEndpoints().get_card_placement(company_id)
            placement = response.json()
        response = AdvEndpoints().send_request(
            method="get", url=url, referer=referer_type.format(company_id=company_id)
        )
        data = response.json()
        data["daily_budget"] = placement.get("budget").get("dailyMax")
        return response, data

    def get_card_placement(self, company_id):
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/placement"
        response = AdvEndpoints().send_request(
            method="get", url=url, referer=referer_type.format(company_id=company_id)
        )
        return response

    def get_balance(self):
        referer_type = self.referer_types[1]
        url = "https://cmp.wildberries.ru/backend/api/v3/balance"
        response = AdvEndpoints().send_request(method="get", url=url, referer=referer_type)
        return response

    def get_search_stats(self, company_id):
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/stat"
        response = AdvEndpoints().send_request(
            method="get", url=url, referer=referer_type.format(company_id=company_id)
        )
        return response

    def get_card_stats(self, company_id):
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/stat"
        response = AdvEndpoints().send_request(
            method="get", url=url, referer=referer_type.format(company_id=company_id)
        )
        return response

    def get_supplier_info(self):
        referer_type = self.referer_types[1]
        url = f"https://cmp.wildberries.ru/backend/api/v3/supplier"
        response = AdvEndpoints().send_request(method="get", url=url, referer=referer_type)
        return response

    def get_order_stat(self):
        referer_type = self.referer_types[4]
        url = (
            f"https://cmp.wildberries.ru/backend/api/v3/stats/atrevds?pageNumber=1&pageSize=100&search=&type=null "
        )
        response = AdvEndpoints().send_request(method="get", url=url, referer=referer_type)
        return response

    def set_new_card_price(self, company_id, price, placement=None):
        referer_type = self.referer_types[3]
        if not placement:
            response = AdvEndpoints().get_card_placement(company_id)
        placement = response.json()
        placement["place"][0]["price"] = price
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/save"
        response1 = AdvEndpoints().send_request(
            method="put",
            url=url,
            referer=referer_type.format(company_id=company_id),
            data=json.dumps(placement).encode("utf-8"),
        )
        return response1

    def start_adv_card_company(self, company_id, placement=None, budget=None):
        referer_type = self.referer_types[3]
        if not placement:
            response = AdvEndpoints().get_card_placement(company_id)
        placement = response.json()
        placement["place"][0]["is_active"] = True
        placement["excludedBrands"] = []
        if not budget:
            response, data = AdvEndpoints().get_card_budget(company_id)
        budget = response.json()
        budget_total = budget.get("total")
        placement["budget"]["total"] = budget_total
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/placement"
        response2 = AdvEndpoints().send_request(
            method="put",
            url=url,
            referer=referer_type.format(company_id=company_id),
            data=json.dumps(placement).encode("utf-8"),
        )
        return response2

    def stop_adv_card_company(self, company_id):
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/pause"
        response = AdvEndpoints().send_request(
            method="get", url=url, referer=referer_type.format(company_id=company_id)
        )
        return response

    def get_full_company_stat(self, company_id):
        referer_type = self.referer_types[4]
        url = f"https://cmp.wildberries.ru/backend/api/v3/fullstat/{company_id}"
        response = AdvEndpoints().send_request(method="get", url=url, referer=referer_type)
        return response

    def get_expenses(self):
        referer_type = self.referer_types[5]
        url = f"https://cmp.wildberries.ru/backend/api/v1/upd"
        response = AdvEndpoints().send_request(method="get", url=url, referer=referer_type)
        return response

    def get_companies(self, is_update=False):
        page = None
        referer_type = self.referer_types[1]
        url = "https://cmp.wildberries.ru/backend/api/v3/atrevds?pageNumber={page}&pageSize=100&search=&status=%5B0,11,1,15,2,4,9,3,14,16,6,17,5,10,13,12,7,8%5D&order=createDate&direction=desc&type=%5B2,3,4,5,6,7%5"
        response = AdvEndpoints().send_request(method="get", url=url.format(page=1), referer=referer_type)
        jsondata = response.json()
        if is_update:
            return response
        count_companies = jsondata.get("counts").get("totalCount")
        page_count = count_companies // 100 + 1
        if page_count == 1 or count_companies == 100:
            return response
        else:
            for page_number in range(1, page_count + 1):
                if page_number == 1:
                    continue
                new_resp = AdvEndpoints().send_request(
                    method="get", url=url.format(page=page_number), referer=referer_type
                )
                jsondata1 = new_resp.json()
                for company in jsondata1.get("content"):
                    jsondata.get("content").append(company)
        return response

    def __try_request(self, method, url, referer, data=None, json=None):
        with open('../wb_token.txt', 'r') as wb_token_from_file:
            wb_token = str(wb_token_from_file.readline().rstrip('\n'))
            wb_token_from_file.close()
        cookies = {"WBToken": wb_token, "x-supplier-id-external": settings.supplier_id}
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer,
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={settings.supplier_id}",
            "X-User-Id": f"{settings.wb_user_id}",
        }
        count = 0
        h = 0
        while count < 20:
            if method == "get":
                response = requests.get(url=url, headers=headers, cookies=cookies)
                if response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                if response.status_code in [401, 403]:
                    h += 1
                    if h == 2:
                        raise InvalidWBToken(wb_token, settings.supplier_id)
                    continue
                return response
            if method == "put":
                response = requests.put(url=url, headers=headers, cookies=cookies, data=data)
                if response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(2)
                    continue
                if response.status_code in [204]:
                    count = count + 1
                    time.sleep(2)
                    continue
                if response.status_code in [401, 403]:
                    h += 1
                    if h == 2:
                        BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
                    continue
                return response
            if method == "post":
                response = requests.post(url=url, headers=headers, cookies=cookies, json=json)
                if response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(2)
                    continue
                if response.status_code in [401, 403]:
                    h += 1
                    if h == 2:
                        BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
                    continue
                return response

    def get_placement_info1(self, company_id):
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        response = AdvEndpoints().__try_request(method="get", url=url,
                                                referer=referer_type.format(company_id=company_id))
        return response


# Кампания для автотестов поиск = 3499821
# Кампания для автотестов карточка товара = 3501540
if __name__ == '__main__':
    response = AdvEndpoints().get_placement_info1(company_id=3499821)
    print(response.status_code)
