import json

import requests


def send_request(method, url, data=None, json=None, headers=None):
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
            'Authorization': 'Bearer ' + str(wb_token),
            'Origin': 'https://dev.marketpapa.ru',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'TE': 'trailers'
        }
    url = url
    if method == "get":
        response = requests.get(url=url, headers=headers)
        return response
    if method == "put":
        response = requests.put(url=url, headers=headers, data=data)
        return response
    if method == "post":
        response = requests.post(url=url, headers=headers, data=data)
        return response


if __name__ == '__main__':
    response = send_request(method='put',
                 url='https://api.marketpapa.ru/api/internal-analytics/orders-self-purchase/',
                 data=json.dumps({
                     "ids": [
                         15625
                     ],
                     "items": [
                         {
                             "odid": 9002248958959,
                             "self_purchase": True
                         }
                     ]
                 })
                 )
    print(response.status_code)
    print(response.text)
