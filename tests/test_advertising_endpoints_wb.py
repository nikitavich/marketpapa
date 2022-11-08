import json
import random
import time
import requests
from lib.assertions import Assertions
from lib import base_case
from lib.base_case import BaseCase


class TestAdvertisingEndpointsWB:

    referer_types = {
        1: "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
        2: "https://cmp.wildberries.ru/campaigns/list/all/edit/search/{company_id}",
        3: "https://cmp.wildberries.ru/campaigns/list/all/edit/carousel-auction/{company_id}",
        4: "https://cmp.wildberries.ru/statistics",
        5: "https://cmp.wildberries.ru/finance/upd"}

    def test_get_new_wb_token_by_wild_auth_new_and_supplier_id(self):
        coken, response_status_code, response0_status_code, response1_status_code, response2_status_code, response3_status_code = BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
        assert response_status_code == 200, f"Wrong status code is {response_status_code}"
        assert response0_status_code == 200, f"Wrong status code is {response0_status_code}"
        assert response1_status_code == 200, f"Wrong status code is {response1_status_code}"
        assert response2_status_code == 200, f"Wrong status code is {response2_status_code}"
        assert response3_status_code == 200, f"Wrong status code is {response3_status_code}"

    def test_get_companies(self):
        page = 1
        new_response = None
        wb_token = "Auuq7QPM79K2DMzNh7cMMo1EiGVfoVb6X5bnUTyzvJUJdO8SIIDQisGQv6cQrGQ5orbBWWmgKZ4ztUNqbXYCR4r7"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[1]
        url = f"https://cmp.wildberries.ru/backend/api/v3/atrevds?pageNumber={page}&pageSize=100&search=&status=%5B0,11,1,15,2,4,9,3,14,16,6,17,5,10,13,12,7,8%5D&order=createDate&direction=desc&type=%5B2,3,4,5,6,7%5"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                    cookies=cookies
                )
                if response.status_code == 200:
                    print(f"status code for placement is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token for placement is {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        if response.status_code == 200:
            pass
        jsondata = response.json()
        count_companies = jsondata.get("counts").get("totalCount")
        page_count = count_companies // 100 + 1
        if page_count == 1 or count_companies == 100:
            return response
        else:
            for page in range(1, page_count + 1):
                if page == 1:
                    continue
                new_response = requests.get(
                    url,
                    headers=headers,
                    cookies=cookies
                )
                jsondata1 = new_response.json()
                for company in jsondata1.get("content"):
                    jsondata.get("content").append(company)
        assert response.status_code == 200, f"Unknown status code {response.status_code}"
        assert new_response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_get_keywords_new(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/words"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies)
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                    cookies=cookies)
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"
        Assertions.assert_code_status(response, 200)

    def test_get_company_info(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[4]
        url = f"https://cmp.wildberries.ru/backend/api/v1/atrevd?advert-id={company_id}"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies)
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                    cookies=cookies)
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"
        Assertions.assert_code_status(response, 200)

    def test_get_placement_info(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                    cookies=cookies)
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_set_excluded_keywords(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        keywords= ["одежда"]
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/set-excluded"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.post(
                    url,
                    headers=headers,
                    cookies=cookies,
                    json={"excluded": keywords}
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_set_new_price(self):
        price = 531
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        print(f"status code is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"
        response1 = None
        placement = response.json()
        placement["place"][0]["price"] = price
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/save"
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        count = 0
        h = 0

        while count < 10:
            try:
                response1 = requests.put(
                    url,
                    headers=headers,
                    cookies=cookies,
                    data=json.dumps(placement).encode("utf-8"),
                )
                if response1.status_code == 200:
                    break
                elif response1.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response1.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response1.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response1.status_code}")
        assert response1.status_code == 200, f"Unknown status code {response1.status_code}"


    def test_start_adv_company(self):
        #get_placement_info
        price = 531
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        print(response.status_code)
        assert response.status_code == 200, f"Unknown status code {response.status_code}"
        #get_budget
        placement = response.json()
        url1 = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/budget"
        response1 = None
        while count < 10:
            try:
                response1 = requests.get(
                    url1,
                    headers=headers,
                )
                if response1.status_code == 200:
                    break
                elif response1.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response1.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response1.status_code}")
        print(response1.status_code)
        assert response1.status_code == 200, f"Unknown status code {response.status_code}"
        budget = response1.json()
        total_budget = budget.get("total")
        placement["budget"]["total"] = total_budget
        # start_adv_company
        response2 = None
        url2 = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        while count < 10:
            try:
                response2 = requests.get(
                    url2,
                    headers=headers,
                    data=json.dumps(placement).encode("utf-8"),
                )
                if response1.status_code == 200:
                    break
                elif response2.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response2.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response2.status_code}")
        print(response2.status_code)
        assert response2.status_code == 200, f"Unknown status code {response.status_code}"

    # Вечно 429 приходит
    def test_stop_adv_company(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/pause"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        cookies = {"WBToken": wb_token, "x-supplier-id-external": supplier_id}
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                    cookies=cookies,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        print(response.status_code)
        assert response.status_code == 200, f"Unknown status code {response.status_code}"



    def test_get_budget(self):

        # Получить placement
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        print(response.status_code)
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

        placement = response.json()
        response1 = None
        url1 = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/budget"
        while count < 10:
            try:
                response1 = requests.get(
                    url1,
                    headers=headers,
                )
                if response1.status_code == 200:
                    break
                elif response1.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response1.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response1.status_code}")
        print(response1.status_code)
        assert response1.status_code == 200, f"Unknown status code {response.status_code}"

    def test_get_card_budget(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/budget"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_get_balance(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[1]
        url = "https://cmp.wildberries.ru/backend/api/v3/balance"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    # def test_deposit(self):
    #     wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
    #     supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
    #     wb_user_id = "8082795"
    #     company_id = 2798829
    #     referer_type = self.referer_types[3]
    #     url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/budget/deposit"
    #     headers = {
    #         "Accept": "application/json, text/plain, */*",
    #         "Pragma": "no-cache",
    #         "Cache-Control": "no-cache",
    #         "Host": "cmp.wildberries.ru",
    #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
    #         "Accept-Language": "en-GB,en;q=0.9",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Connection": "keep-alive",
    #         "Referer": referer_type.format(company_id=company_id),
    #         "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
    #         "X-User-Id": f"{wb_user_id}"
    #     }
    #     count = 0
    #     h = 0
    #     response = None
    #     while count < 10:
    #         try:
    #             response = requests.post(
    #                 url,
    #                 headers=headers,
    #                 # json={"sum": deposit, "type": balance_type}
    #             )
    #             if response.status_code == 200:
    #                 print(f"status code is {response.status_code}")
    #                 break
    #             elif response.status_code in [429, 418]:
    #                 count = count + 1
    #                 print(f"status code is {response.status_code}")
    #                 time.sleep(random.randint(10, 30))
    #                 continue
    #             elif response.status_code in [401, 403]:
    #                 count = count + 1
    #                 h += 1
    #                 print(f"status code is {response.status_code}")
    #                 if h == 2:
    #                     raise print(f"Invalid token {wb_token} for {supplier_id}")
    #                 continue
    #         except:
    #             print(f"Unknown error, status is {response.status_code}")
    #     assert response.status_code == 200, f"Unknown status code {response.status_code}"


    def test_get_search_stats(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/stat"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_get_card_stats(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/stat"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_get_supplier_info(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[1]
        url = f"https://cmp.wildberries.ru/backend/api/v3/supplier"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"


    def test_get_order_stat(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[4]
        url = (
            f"https://cmp.wildberries.ru/backend/api/v3/stats/atrevds?pageNumber=1&pageSize=100"
            f"&search=&type=null "
        )
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_get_card_placement(self):
        wb_token = "Auuq7QPM79K2DMzNh7cMMo1EiGVfoVb6X5bnUTyzvJUJdO8SIIDQisGQv6cQrGQ5orbBWWmgKZ4ztUNqbXYCR4r7"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

    def test_set_new_card_price(self):
        # Получить placement
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    break
                elif response.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"

        #set_new_card_price
        placement = response.json()
        placement["place"][0]["price"] = 581
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/save"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response1 = None
        while count < 10:
            try:
                response1 = requests.put(
                    url,
                    headers=headers,
                    data=json.dumps(placement).encode("utf-8"),
                )
                if response1.status_code == 200:
                    print(f"status code is {response1.status_code}")
                    break
                elif response1.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code is {response1.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response1.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code is {response1.status_code}")
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response1.status_code}")
        assert response1.status_code == 200, f"Unknown status code {response1.status_code}"

 # не получается запустить, ошибка Invalid token на 3 запросе
    def test_start_adv_card_company(self):
        # Получить placement
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[2]
        url = f"https://cmp.wildberries.ru/backend/api/v2/search/{company_id}/placement"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code for placement is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token for placement is {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        print(response.status_code)
        assert response.status_code == 200, f"Unknown status code {response.status_code}"
        placement = response.json()
        placement["place"][0]["is_active"] = True
        placement["excludedBrands"] = []

    # budget
        referer_type = self.referer_types[3]
        url1 = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/budget"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response1 = None
        while count < 10:
            try:
                response1 = requests.get(
                    url1,
                    headers=headers,
                )
                if response1.status_code == 200:
                    print(f"status code for budget is {response1.status_code}")
                    break
                elif response1.status_code in [429, 418]:
                    count = count + 1
                    print(f"status code for budget is {response1.status_code}")
                    time.sleep(random.randint(10, 30))
                    continue
                elif response1.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    print(f"status code for budget is {response1.status_code}")
                    if h == 2:
                        raise print(f"Invalid token for budget {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response1.status_code}")
        assert response1.status_code == 200, f"Unknown status code {response1.status_code}"
        budget = response1.json()
        budget_total = budget.get("total")

        placement["budget"]["total"] = budget_total
        print(budget_total)
        print(placement["budget"]["total"])
    # start_adv
        referer_type = self.referer_types[3]
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        url2 = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/placement"
        count = 0
        h = 0
        response2 = None
        while count < 10:
            try:
                response2 = requests.put(
                    url,
                    headers=headers,
                    data=json.dumps(placement).encode("utf-8")
                )
                if response2.status_code == 200:
                    break
                elif response2.status_code in [429, 418]:
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response2.status_code in [401, 403]:
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response2.status_code}")
        print(response2.status_code)
        assert response2.status_code == 200, f"Unknown status code {response2.status_code}"


    def test_stop_adv_card_company(self):
        # Получить placement
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[3]
        url = f"https://cmp.wildberries.ru/backend/api/v2/carousel-auction/{company_id}/pause"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code for stop adv is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    print(f"status code for stop adv is {response.status_code}")
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    print(f"status code for stop adv is {response.status_code}")
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token for placement is {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"


    def test_get_full_company_stat(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[4]
        url = f"https://cmp.wildberries.ru/backend/api/v3/fullstat/{company_id}"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code for placement is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token for placement is {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"


    def test_get_expenses(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        referer_type = self.referer_types[5]
        url = f"https://cmp.wildberries.ru/backend/api/v1/upd"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": referer_type.format(company_id=company_id),
            "Cookie": f"WBToken={wb_token}; x-supplier-id-external={supplier_id}",
            "X-User-Id": f"{wb_user_id}"
        }
        count = 0
        h = 0
        response = None
        while count < 10:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                )
                if response.status_code == 200:
                    print(f"status code for placement is {response.status_code}")
                    break
                elif response.status_code in [429, 418]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    time.sleep(random.randint(10, 30))
                    continue
                elif response.status_code in [401, 403]:
                    print(f"status code for placement is {response.status_code}")
                    count = count + 1
                    h += 1
                    if h == 2:
                        raise print(f"Invalid token for placement is {wb_token} for {supplier_id}")
                    continue
            except:
                print(f"Unknown error, status is {response.status_code}")
        assert response.status_code == 200, f"Unknown status code {response.status_code}"








