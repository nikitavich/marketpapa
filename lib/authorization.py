import requests

import settings


class Authorization:

    def get_wb_token_by_phone_number(self, phone_number, wild_auth_new):
        headers = {
            "Host": "seller.wildberries.ru",
            "Connection": "keep-alive",
            "Content-Length": "63",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-platform": '"macOS"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://seller.wildberries.ru",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://seller.wildberries.ru/login/en?redirect_url=/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cookie": "locale=en; _wbauid=6177967871674286731",
        }
        payload = {"phone": phone_number, "is_terms_and_conditions_accepted": True}
        resp1 = None
        for i in range(7):
            try:
                resp1 = requests.post(
                    "https://seller.wildberries.ru/passport/api/v2/auth/login_by_phone",
                    headers=headers,
                    json=payload,
                    timeout=10,
                )
                break
            except Exception as err:
                print(err)
                pass
        token = resp1.json().get("token")
        headers = {
            "Host": "seller.wildberries.ru",
            "Connection": "keep-alive",
            "Content-Length": "198",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-platform": '"macOS"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://seller.wildberries.ru",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://seller.wildberries.ru/login/en?redirect_url=/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cookie": "locale=en; _wbauid=6177967871674286731",
        }
        notify_code = Authorization().get_code_from_wb_notification(
            wild_auth_new='7255F34755CDC024A4BE3B7EAF84A2A1D4B24AFE173C2748293673093E85236AFEFBB33C895B9F9EA3A6030DD60BFA3D973C05B2ED5706952413B3B9CA55BEB8C1877ECB417F1F5A88359A1C66FB3CA6C017A7E0DEE4EE8A31568DC287D0F53225D9253D48062EE01B64B4CDEA4A870E477630216A611BBB4B325D8DD7A0B4419AFF92961AF488E65391753AD240403914169716E95FB42C4E026B91D336624AD5E57B4FC601A51643F27188FF5830A90E4A88553302EB348517A3926B2C2315E8279C7AEFE1DAB6F0B6912BDEB43DEE6D83426CB2162D64C1CADC6C85E59ED13345ECFB0512D4C158E462ADA391176F56A8096F3F97B54B4B42FE3717100775F3F4743AF1BB67B326F37D69E3C6A44DAC27BA4FF0BF4662586A7AE40BBE0E6420522D38')
        payload = {
            "options": {
                "notify_code": notify_code},
            "token": token,
            "device": "тест",
        }
        resp2 = None
        for i in range(7):
            try:
                resp2 = requests.post(
                    "https://seller.wildberries.ru/passport/api/v2/auth/login",
                    headers=headers,
                    json=payload,
                    timeout=10,
                )
                break
            except:
                pass
        if resp2 is None:
            return
        wb_token = resp2.cookies.get("WBToken")
        return wb_token, resp2, resp1

    def get_code_from_wb_notification(self, wild_auth_new: str):
        headers = {
            "Host": "www.wildberries.ru",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "x-spa-version": "9.3.76",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"macOS"',
            "Accept": "*/*",
            "Origin": "https://www.wildberries.ru",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.wildberries.ru/lk/newsfeed/events",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cookie": f"WILDAUTHNEW_V3={wild_auth_new}",
        }
        resp = None
        for i in range(7):
            try:
                resp = requests.post(
                    "https://www.wildberries.ru/webapi/lk/newsfeed/events/data?",
                    headers=headers,
                    timeout=10,
                )
                break
            except:
                pass
        if resp is None:
            return
        if resp.status_code == 401:
            print('Ошибка: ' + str(resp.status_code))
        data = resp.json()
        # print(data)
        codes = []
        for notification in [x.get("message") for x in data.get("value").get("events")]:
            if "Код подтверждения:" in notification:
                codes.append(notification[320:326])
            elif "Ваш код аутентификации" in notification:
                codes.append(notification[327:333])
        return codes[0]

    def get_new_wb_token_by_wb_token_and_supplier_id(self, wb_token, supplier_id):
        WBToken = wb_token
        url0 = "https://seller.wildberries.ru/passport/api/v2/auth/grant"
        cookies0 = {"WBToken": WBToken}
        headers0 = {
            "Accept": "application/json, text/plain, */*",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache",
            "Host": "seller.wildberries.ru",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
            # "Accept-Language": "en-GB,en;q=0.9",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Connection": "keep-alive",
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
                print(err)
                pass
        if not resp0:
            print(1)
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
        for i in range(7):
            try:
                resp1 = requests.post(
                    url1,
                    headers=headers1,
                    json=json1,
                    timeout=3.0,
                )
                break
            except Exception as err:
                print(err)
                pass
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
        for i in range(7):
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
        return coken, resp1, resp2, resp3


wb_token, resp2, resp1 = Authorization().get_wb_token_by_phone_number(phone_number='79998074678',
                                                                      wild_auth_new=settings.wild_auth_new)
print(wb_token)
coken, res1, res2, resp3 = Authorization().get_new_wb_token_by_wb_token_and_supplier_id(wb_token=wb_token,
                                                                                        supplier_id=settings.supplier_id)
print(res1.status_code)
print(res2.status_code)
print(resp3.status_code)
print(coken)
