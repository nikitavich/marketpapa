from lib.new_adv_cabinet import *


class TestNewAdvCabinet:
    # Кампания для автотестов поиск = 3499821
    # Кампания для автотестов карточка товара = 3501540
    def test_get_all_company(self):
        response = get_all_company()
        assert response.status_code == 200, f'Wrong status code, code is {response.status_code}'

    def test_get_list_company(self):
        response = get_list_company()
        assert response.status_code == 200, f'Wrong status code, code is {response.status_code}'

    def test_get_info_about_company(self):
        response = get_info_about_company(3499821)
        assert response.status_code == 200, f'Wrong status code, code is {response.status_code}'

    # def test_start_company(self):
    #     response = start_company(3501540)
    #     print(response.status_code)
    #     print(response.text)
    #     assert response.status_code == 200, f'Wrong status code, code is {response.status_code}'
    #
    # def test_stop_company(self):
    #     response = stop_company(3501540)
    #     assert response.status_code == 200, f'Wrong status code, code is {response.status_code}'

    def test_get_info_about_bet(self):
        response = get_info_about_bet()
        assert response.status_code == 200, f'Wrong status code, code is {response.status_code}'
