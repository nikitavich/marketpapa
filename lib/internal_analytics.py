import json

import requests


def send_request(method, url, data=None, json=None, headers=None):
    with open('wb_token.txt', 'r') as wb_token_from_file:
        wb_token = str(wb_token_from_file.readline().rstrip('\n'))
        wb_token_from_file.close()
    if headers is None:
        headers = {
            'authority': 'api.marketpapa.ru',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer ' + str(wb_token),
            'content-type': 'application/json',
            'origin': 'https://dev.marketpapa.ru',
            'referer': 'https://dev.marketpapa.ru/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
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
