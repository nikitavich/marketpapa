import random

import requests
import time
import requests


class BaseCase:
    referer_types = {
        1: "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
        2: "https://cmp.wildberries.ru/campaigns/list/all/edit/search/{company_id}",
        3: "https://cmp.wildberries.ru/campaigns/list/all/edit/carousel-auction/{company_id}",
        4: "https://cmp.wildberries.ru/statistics",
        5: "https://cmp.wildberries.ru/finance/upd"}

    def __init__(self):
        self.supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        self.wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        self.wb_user_id = "8082795"
    # Получение ids токена
    def get_id_from_token(self):
        ids = None
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        for element in parsed_response_text['items']:
            if element["key_name"] == "Василий":
                ids = element["id"]
        response_status_code = response.status_code
        return response_status_code, ids

    def get_new_wb_token_by_wild_auth_new_and_supplier_id(self):
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        url = "https://seller.wildberries.ru/passport/api/v2/auth/wild_v3_upgrade"
        wild_auth_new = "ADAE31160B93B82E84E65E48E2F6750AC0F83548B13EED70696340D540F6BDF8BDF931CAC8D3ED1488B213146CC446FFD0648F7D3CC1BDF63A62911BEA312968E4998DD131693D206F740AE44689E6DF084DA5A7916B58BA47929F986FDABD5282EAEB289A08080E59D2D4DE0190C7FED7326E020E735628A82D22CA30331BD6F1F5D74E2B56E265D07B9AA677860D8387CB5478DAC232B69EA0A17C5F04CCD41FC7C522249E1C071472DA9AF88BD83787828D213906585944C5849427CD677ECF190F3DB1F452FFE70FF1CDE64809FFCF4D65ED54E270878C17F523DB32B2D4D26AC2A8AE6792147229F8399232A2E63C06C209E795F26EDD872DD9B038FADB411E4DBD1024C4A3303C22E14D7C51CF25C01D8C4BBABFFE42AD494EACD284F3D5C0A24FE19D4438606F8FEC89F8541EEC01E6EB3364ADBD197F22241A89B9ACDABB19D6ED80462DB8B4C4472BC95F2AA21B8443"
        cookies = {"WILDAUTHNEW_V3": wild_auth_new}
        resp = None
        resp = requests.post(
            url,
            cookies=cookies,
            json={"device": "Macintosh,Google Chrome 104.0"},
            timeout=5.0,
        )
        WBToken = resp.cookies.get("WBToken")
        url0 = "https://seller.wildberries.ru/passport/api/v2/auth/grant"
        cookies0 = {"WBToken": WBToken}
        headers0 = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "seller.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://seller.wildberries.ru/login/en?redirect_url=/",
            "Cookie": f"WBToken={WBToken}",
        }
        resp0 = None
        try:
            resp0 = requests.post(
                url0,
                cookies=cookies0,
                headers=headers0,
                timeout=3.0,
            )
        except Exception as err:
            # print(err)
            pass
        WBToken = resp0.json().get("token")
        url1 = "https://passport.wildberries.ru/api/v2/auth/login"
        json1 = {"token": WBToken, "device": "Macintosh,Google Chrome 104.0"}
        headers1 = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "passport.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://seller.wildberries.ru/",
        }
        for i in range(3):
            try:
                resp1 = requests.post(
                    url1,
                    headers=headers1,
                    json=json1,
                    timeout=3.0,
                )
                break
            except Exception as err:
                pass
                # print(err)
        wb_token_temp1 = resp1.cookies.get("WBToken")
        url2 = "https://passport.wildberries.ru/api/v2/auth/grant"
        json2 = {}
        headers2 = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "passport.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://cmp.wildberries.ru/",
            "Cookie": f"WBToken={wb_token_temp1}; x-supplier-id-external={supplier_id}",
        }
        resp2 = None
        for i in range(3):
            try:
                resp2 = requests.post(
                    url2,
                    headers=headers2,
                    json=json2,
                    timeout=3.0,
                )
                break
            except Exception as err:
                pass
                # print(err)
        if not resp2:
            return
        wb_token_temp2 = resp2.json().get("token")
        url3 = "https://cmp.wildberries.ru/passport/api/v2/auth/login"
        cookies3 = {"x-supplier-id-external": supplier_id}
        headers3 = {
            "Accept": "application/json, text/plain, */*",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Host": "cmp.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            "Accept-Language": "en-GB,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://cmp.wildberries.ru/",
            "Cookie": f"x-supplier-id-external={supplier_id}",
        }
        json3 = {"token": wb_token_temp2, "device": "Macintosh, Chrome 104.0"}
        resp3 = None
        for i in range(3):
            try:
                resp3 = requests.post(
                    url3,
                    cookies=cookies3,
                    headers=headers3,
                    json=json3,
                    timeout=3.0,
                )
                break
            except Exception as err:
                # print(err)
                pass
        if not resp3:
            return
        coken = resp3.cookies.get("WBToken")
        response_status_code = resp.status_code
        response0_status_code = resp0.status_code
        response1_status_code = resp1.status_code
        response2_status_code = resp2.status_code
        response3_status_code = resp3.status_code

        return coken, response_status_code, response0_status_code, response1_status_code, response2_status_code, response3_status_code

    # Получение company_id
    # def get_companies(self, *args):
    #     BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
    #
    #     headers = {
    #         "Accept": "application/json, text/plain, */*",
    #         "Pragma": "no-cache",
    #         "Cache-Control": "no-cache",
    #         "Host": "cmp.wildberries.ru",
    #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
    #         "Accept-Language": "en-GB,en;q=0.9",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Connection": "keep-alive",
    #         "Referer": "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
    #         "Cookie": f"WBToken={self.coken}; x-supplier-id-external={self.supplier_id}",
    #         "X-User-Id": f"{self.wb_user_id}"
    #     }
    #     response = requests.get("https://cmp.wildberries.ru/backend/api/v3/atrevds?pageNumber=1&pageSize=100&search=&status=%5B0,11,1,15,2,4,9,3,14,16,6,17,5,10,13,12,7,8%5D&order=createDate&direction=desc&type=%5B2,3,4,5,6,7%5",
    #                             headers=headers)
    #     print(response.status_code)
    #     print(response.text)
    #     return

    def get_wb_user_id(self):
        url = "https://cmp.wildberries.ru/passport/api/v2/auth/introspect"
        cookies = {"WBToken": self.wb_token, "x-supplier-id-external": self.supplier_id}
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
        }
        for i in range(5):
            try:
                resp = requests.get(
                    url, cookies=cookies, headers=headers, timeout=10
                )
                return resp.json().get("userID")
            except:
                pass
    def get_keywords_new(self):
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

        return response.status_code, response.text, response.json()

    def get_placement_info(self):
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
        while count < 5:
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
                    time.sleep(random.randint(1, 5))
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
        return response

    def set_excluded_keywords(self):
        wb_token = "Auuq7QPwg5S2DPDhyLYMMs0njfdAkR_sXec77qztRB7X25NAYEk4uTsvbG1-ESzbp5CrRMKbWsZo-rwAhIdxDvZq"
        supplier_id = "234dea95-0f26-48f5-8c4d-e0e0c35b2a8d"
        wb_user_id = "8082795"
        company_id = 2798829
        keywords= ["одежда"]
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
        while count < 5:
            try:
                response = requests.get(
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
                    time.sleep(random.randint(1, 5))
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
        return response



# test = BaseCase().get_wb_user_id()
# test1 = BaseCase().get_new_wb_token_by_wild_auth_new_and_supplier_id()
# test2 = BaseCase().get_id_from_token()
# test3 = BaseCase().get_wb_user_id()
# # test4 = BaseCase().get_companies()
# print(test)
# print(test1)
# print(test2)
# print(test3)
# # print(test4)
