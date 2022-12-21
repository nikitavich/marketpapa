import pytest
import requests

from environment import token


@pytest.fixture(scope="session")
def get_id_from_token():
    response = requests.get("https://api.marketpapa.ru/api/internal-analytics/token/",
                            headers={
                                "Authorization": "Bearer " + str(token)
                            }
                            )
    parsed_response_text = response.json()
    ids = None
    for element in parsed_response_text['items']:
        if element["key_name"] == "Василий":
            ids = element["id"]
    response_status_code = response.status_code
    return response_status_code, ids
