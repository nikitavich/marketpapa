import json
import pickle
import random
import string
import time
import datetime
import jwt
from webdriver_manager.chrome import ChromeDriverManager

from lib.authorization import Authorization

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from lib import settings
from lib.proxies import PROXIES
from selenium.common.exceptions import NoSuchElementException


class BaseCase:
    referer_types = {
        1: "https://cmp.wildberries.ru/campaigns/list/all?type=auction",
        2: "https://cmp.wildberries.ru/campaigns/list/all/edit/search/{company_id}",
        3: "https://cmp.wildberries.ru/campaigns/list/all/edit/carousel-auction/{company_id}",
        4: "https://cmp.wildberries.ru/statistics",
        5: "https://cmp.wildberries.ru/finance/upd"}

    # Получение ids токена
    def get_id_from_token(self, token):
        ids = None
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer " + str(token)
                                }
                                )
        parsed_response_text = response.json()
        for element in parsed_response_text['items']:
            if element["key_name"] == "NEW_ВАСИЛИЙ":
                ids = element["id"]
        response_status_code = response.status_code
        return response_status_code, ids

    def get_new_wb_token_by_wild_auth_new_and_supplier_id(self):
        headers = {
            "Host": "seller.wildberries.ru",
            "Connection": "keep-alive",
            "Content-Length": "22",
            "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            "sec-ch-ua-platform": '"macOS"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://seller.wildberries.ru",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://seller.wildberries.ru/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cookie": f"WILDAUTHNEW_V3={wild_auth_new};",
        }

        url = "https://seller.wildberries.ru/passport/api/v2/auth/wild_v3_upgrade"
        cookies = {"WILDAUTHNEW_V3": wild_auth_new}
        resp = None
        resp = requests.post(
            url,
            cookies=cookies,
            json={"device": "Macintosh"},
            headers=headers,
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
        for i in range(3):
            try:
                resp0 = requests.post(
                    url0,
                    cookies=cookies0,
                    headers=headers0,
                    timeout=3.0,
                )
                break
            except Exception as err:
                pass
        if not resp0:
            return
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
        resp1 = None
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
        if not resp1:
            return
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
        with open("./wb_token.txt", 'w') as wb_token:
            print(coken, file=wb_token)
        response_status_code = resp.status_code
        response0_status_code = resp0.status_code
        response1_status_code = resp1.status_code
        response2_status_code = resp2.status_code
        response3_status_code = resp3.status_code

        return coken, response_status_code, response0_status_code, response1_status_code, response2_status_code, response3_status_code

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(random.randint(8, 10)))
        return rand_string

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
        cookies = {"WBToken": settings.wb_token, "x-supplier-id-external": settings.supplier_id}
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
            "Cookie": f"WBToken={settings.wb_token}; x-supplier-id-external={settings.supplier_id}",
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

        keywords = ["одежда"]
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

    def save_cookies(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://marketpapa.ru/login')
        driver.find_element(By.XPATH, "//span[@class='sc-iJnaPW izGUBw']").click()
        time.sleep(5)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    def add_cookie_to_chrome(self, driver):
        driver.get("https://marketpapa.ru/news")
        time.sleep(1)
        for cookie in pickle.load(open("cookies.pkl", "rb")):
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.refresh()

    # Проверка добавления cookies
    # BaseCase().add_cookie_to_chrome()
    def update_token(self):
        headers = {
            "Host": "seller.wildberries.ru",
            "Connection": "keep-alive",
            "Content-Length": "22",
            "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            "sec-ch-ua-platform": '"macOS"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://seller.wildberries.ru",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://seller.wildberries.ru/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cookie": f"WILDAUTHNEW_V3={wild_auth_new};",
        }

        url = "https://seller.wildberries.ru/passport/api/v2/auth/wild_v3_upgrade"
        cookies = {"WILDAUTHNEW_V3": wild_auth_new}
        resp = None
        resp = requests.post(
            url,
            cookies=cookies,
            json={"device": "Macintosh"},
            headers=headers,
            timeout=5.0,
        )
        return resp


def update_wb_token():
    supplier_id = settings.supplier_id
    wild_auth_new = settings.wild_auth_new
    headers = {
        "Host": "seller.wildberries.ru",
        "Connection": "keep-alive",
        "Content-Length": "22",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-platform": '"macOS"',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://seller.wildberries.ru",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://seller.wildberries.ru/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cookie": f"WILDAUTHNEW_V3={wild_auth_new};",
    }

    url = "https://seller.wildberries.ru/passport/api/v2/auth/wild_v3_upgrade"
    cookies = {"WILDAUTHNEW_V3": wild_auth_new}
    resp = None
    resp = requests.post(
        url,
        cookies=cookies,
        json={"device": "Macintosh"},
        headers=headers,
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
    for i in range(3):
        try:
            resp0 = requests.post(
                url0,
                cookies=cookies0,
                headers=headers0,
                timeout=3.0,
            )
            break
        except Exception as err:
            pass
    if not resp0:
        return
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
    resp1 = None
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
    if not resp1:
        return
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
    with open("./wb_token.txt", 'w') as wb_token:
        print(coken, file=wb_token)
    response_status_code = resp.status_code
    response0_status_code = resp0.status_code
    response1_status_code = resp1.status_code
    response2_status_code = resp2.status_code
    response3_status_code = resp3.status_code

    return coken, response_status_code, response0_status_code, response1_status_code, response2_status_code, response3_status_code


def get_id_test_companies():
    count = 0
    response = None
    while count < 5:
        proxy = random.choice(PROXIES)
        with open('./WBToken', 'r') as wb_token_from_file:
            WBToken = str(wb_token_from_file.readline().rstrip('\n'))
            wb_token_from_file.close()
        url = "https://cmp.wildberries.ru/backend/api/v3/atrevds?pageNumber=1&pageSize=10&search=%D1%82%D0%B5%D1%81%D1%82%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5&status=%5B0,11,1,15,2,4,9,3,14,16,6,17,5,10,13,12,7,8%5D&order=createDate&direction=desc&type=%5B2,3,4,5,6,7%5D"
        payload = {}
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-control': 'no-store',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Content-Type': 'application/json',
            'Cookie': f'x-supplier-id-external=234dea95-0f26-48f5-8c4d-e0e0c35b2a8d; WBToken={WBToken}',
            'Origin': 'https://cmp.wildberries.ru',
            'Referer': 'https://cmp.wildberries.ru/campaigns/list/active',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-User-Id': '8082795',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload,
                                        proxies={"http": proxy, "https": proxy})
        except requests.exceptions.ProxyError:
            count += 1
            time.sleep(1)
            continue
        except requests.exceptions.SSLError:
            count += 1
            time.sleep(1)
            continue
        except requests.exceptions.ReadTimeout:
            count += 1
            time.sleep(1)
            continue
        if response.status_code in [429]:
            count += 1
            time.sleep(1)
            continue
        if response.status_code in [401]:
            update_wbtoken()
            time.sleep(1)
            continue
        break
    else:
        raise
    list_of_companies = []
    if response.text:
        dict = json.loads(response.text)
        for item in dict['content']:
            if item['campaignName'] == 'тест создание':
                list_of_companies.append(item['id'])
    return list_of_companies


def delete_test_companies():
    func = get_id_test_companies()
    with open('./WBToken', 'r') as wb_token_from_file:
        WBToken = str(wb_token_from_file.readline().rstrip('\n'))
        wb_token_from_file.close()
    if func:
        for company_id in func:
            count = 0
            timeout = 0
            proxy = 0
            while count < 5:
                proxy = random.choice(PROXIES)
                url = f"https://cmp.wildberries.ru/backend/api/v1/atrevd/{company_id}/to-delete"
                payload = {}
                headers = {
                    'Accept': 'application/json',
                    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Cache-control': 'no-store',
                    'Connection': 'keep-alive',
                    'Content-Length': '0',
                    'Content-Type': 'application/json',
                    'Cookie': f'x-supplier-id-external=234dea95-0f26-48f5-8c4d-e0e0c35b2a8d; WBToken={WBToken}',
                    'Origin': 'https://cmp.wildberries.ru',
                    'Referer': 'https://cmp.wildberries.ru/campaigns/list/active',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                    'X-User-Id': '8082795',
                    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"macOS"'
                }
                try:
                    response = requests.request("PUT", url, headers=headers, data=payload,
                                                proxies={"http": proxy, "https": proxy})
                    print(response)
                except requests.exceptions.ProxyError:
                    count += 1
                    proxy += 1
                    if proxy > 3:
                        return False
                    time.sleep(1)
                    continue
                except requests.exceptions.ReadTimeout:
                    count += 1
                    timeout += 1
                    if timeout > 3:
                        return False
                    time.sleep(1)
                    continue
                except requests.exceptions:
                    return False
                if response.status_code in [429]:
                    count += 1
                    time.sleep(1)
                    continue
                break
        return True
    else:
        return True


def update_wb_token1():
    dt = datetime.datetime.now() + datetime.timedelta(days=30)

    token = jwt.JWT.encode(payload=
    {
        'id': 35,
        'exp': int(dt.strftime('%s'))
    },

    token.encode('utf-8')
    with open('./wb_token.txt', 'w') as file:
        file.write(token)


def update_wbtoken():
    wb_token, resp2, resp1 = Authorization().get_wb_token_by_phone_number(phone_number='79998074678',
                                                                          wild_auth_new=settings.wild_auth_new)
    coken, res1, res2, resp3 = Authorization().get_new_wb_token_by_wb_token_and_supplier_id(wb_token=wb_token,
                                                                                            supplier_id=settings.supplier_id)
    with open('../WBToken', 'w') as file:
        file.write(coken)
        file.close()


def find_element_on_page(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False


if __name__ == '__main__':
    BaseCase().save_cookies()
