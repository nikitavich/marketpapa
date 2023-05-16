import json
import random
import time
from lib.base_case import update_wb_token1
from lib.proxies import PROXIES

import requests


def send_request(method, url, data=None, json=None, headers=None, files=None):
    with open('./wb_token.txt', 'r') as wb_token_from_file:
        wb_token = str(wb_token_from_file.readline().rstrip('\n'))
        wb_token_from_file.close()
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://marketpapa.ru/',
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + str(wb_token),
            'Origin': 'https://marketpapa.ru',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'TE': 'trailers'
        }
    url = url
    count = 0
    response = None
    while count < 5:
        proxy = random.choice(PROXIES)
        if method == "get":
            try:
                response = requests.get(url=url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=60)
            except requests.exceptions.ProxyError:
                count += 1
                time.sleep(1)
                continue
            except requests.exceptions.ReadTimeout:
                count += 1
                time.sleep(1)
                continue
            if response.status_code in [502, 500]:
                return response
            if response.status_code in [403]:
                update_wb_token1()
                return "Статус код 403!"
            if response.status_code in [429]:
                count += 1
                time.sleep(1)
                continue
            return response
        if method == "put":
            try:
                response = requests.put(url=url, headers=headers, data=data, proxies={"http": proxy, "https": proxy}, timeout=60)
            except requests.exceptions.ProxyError:
                count += 1
                time.sleep(1)
                continue
            except requests.exceptions.ReadTimeout:
                count += 1
                time.sleep(1)
                continue
            if response.status_code in [502, 500]:
                return response
            if response.status_code in [403]:
                update_wb_token1()
                return "Статус код 403!"
            if response.status_code in [429]:
                count += 1
                time.sleep(1)
                continue
            return response
        if method == "post":
            try:
                response = requests.post(url=url, headers=headers, data=data, files=files, proxies={"http": proxy, "https": proxy}, timeout=60)
            except requests.exceptions.ProxyError:
                count += 1
                time.sleep(1)
                continue
            except requests.exceptions.ReadTimeout:
                count += 1
                time.sleep(1)
                continue
            if response.status_code in [502, 500]:
                return response
            if response.status_code in [403]:
                update_wb_token1()
                return "Статус код 403!"
            if response.status_code in [429]:
                count += 1
                time.sleep(1)
                continue
            return response
    return response


if __name__ == '__main__':
    response = send_request(method='get',
                            url='https://api.marketpapa.ru/api/advertising-cabinet/compare_card_prices/3499821/')
    assert response.status_code == 200, f'Wrong response code! - {response.status_code}'
    print(response.status_code)
    print(response.text)
