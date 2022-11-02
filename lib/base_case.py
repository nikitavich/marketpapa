import json.decoder
from datetime import datetime

import requests
from requests import Response


class BaseCase:

    def get_id_from_token(self):
        response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                                headers={
                                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzUsImV4cCI6MTY2ODE1NjI5NH0.cbuYC3YGzrxZ74_YoX-10HAKjxeYIGBrJpjZfXSKu_k"})
        parsed_response_text = response.json()
        for element in parsed_response_text['items']:
            if element["key_name"] == "Василий":
                self.ids = element["id"]
        self.response_status_code = response.status_code
        return self.response_status_code, self.ids


    # def get_cookie(self, response: Response, cookie_name):
    #     assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
    #     return response.cookies[cookie_name]
    #
    # def get_header(self, response: Response, headers_name):
    #     assert headers_name in response.headers, f"Cannot find header with name  {headers_name} in the last response"
    #     return response.headers[headers_name]
    #
    # def get_json_value(self, response: Response, name):
    #     try:
    #         response_as_dict = response.json()
    #     except json.decoder.JSONDecodeError:
    #         assert False, f"Response is not in JSOM format. Response text is '{response.text}'"
    #
    #     assert name in response_as_dict, f"Response JSON doesnt have  kay '{name}'"
    #
    #     return response_as_dict[name]

    # def prepare_registration_data(self, email=None):
    #     if email is None:
    #         base_part = "learnqa"
    #         domain = "example.com"
    #         random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    #         email = f"{base_part}{random_part}@{domain}"
    #     return {
    #         'username': 'learnqa',
    #         'password': '123',
    #         'firstName': 'learnqa',
    #         'lastName': 'learnqa',
    #         'email': email
    #     }
