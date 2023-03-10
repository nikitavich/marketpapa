import requests
import random
from urllib import parse

ADS_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjIwNzYzMWE1LWQzMTctNGViNi05Mjc3LWJkYTZjZmNlMGEwZCJ9.RfQQJfm_r1B2JYJ7TzuZIBbkdDaZsKl7O9I1lMaBjL8"
HEADERS = {
    "Authorization": ADS_KEY
}


def do_request(url, method):
    counter = 0
    while counter < 5:
        counter += 1
        try:
            res = requests.request(
                method=method,
                url=url,
                headers=HEADERS,
            )
            return res
        except Exception as ex:
            print(ex)


def get_all_company():
    url = "https://advert-api.wb.ru/adv/v0/count"
    res = do_request(url, "get")
    return res


def get_list_company():
    url = "https://advert-api.wb.ru/adv/v0/adverts?order=create&direction=desc"
    res = do_request(url, "get")
    return res


def get_info_about_company(company_id):
    url = f"https://advert-api.wb.ru/adv/v0/advert?id={company_id}"
    response = do_request(url, "get")
    return response


def start_company(company_id):
    url = f"https://advert-api.wb.ru/adv/v0/start?id={company_id}"
    response = do_request(url, method="get")
    return response


def stop_company(company_id):
    url = f"https://advert-api.wb.ru/adv/v0/pause?id={company_id}"
    response = do_request(url, method="get")
    return response


def get_info_about_bet(type_company=6, param=11):
    url = f"https://advert-api.wb.ru/adv/v0/cpm?type={type_company}&param={param}"
    response = do_request(url, "get")
    return response




# if __name__ == '__main__':
#     res = get_info_about_company(4405725)
#     res1 = get_all_company()
#     res2 = get_list_company()
#     res3 = get_info_about_company(3499821)
#     res4 = start_company(3499821)
#     res5 = stop_company(3499821)
#     res6 = get_info_about_bet()