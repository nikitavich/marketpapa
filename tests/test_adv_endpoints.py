import time

from lib.adv_endpoints import AdvEndpoints


class TestAdvEndpoints(AdvEndpoints):

    # Кампания для автотестов поиск = 3499821
    # Кампания для автотестов карточка товара = 3501540
    def test_get_keywords_new(self):
        response = AdvEndpoints().get_keywords_new(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_company_info(self):
        response = AdvEndpoints().get_company_info(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_placement_info(self):
        response = AdvEndpoints().get_placement_info(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_set_excluded_keywords(self):
        response = AdvEndpoints().set_excluded_keywords(company_id=3499821, keywords=["одежда"])
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_set_new_price(self):
        response = AdvEndpoints().set_new_price(company_id=3499821, price=583)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_stop_adv_company(self):
        response = AdvEndpoints().get_placement_info(company_id=3499821)
        jsondata = response.json()
        current_status = jsondata['status']
        if current_status == 11:
            AdvEndpoints().start_adv_company(company_id=3499821)
            time.sleep(2)
        response1 = AdvEndpoints().stop_adv_company(company_id=3499821)
        assert response1.status_code == 200, f"Wrong status code! Status code is {response1.status_code}"

    def test_start_adv_company(self):
        response = AdvEndpoints().get_placement_info(company_id=3499821)
        jsondata = response.json()
        current_status = jsondata['status']
        if current_status == 9:
            AdvEndpoints().stop_adv_company(company_id=3499821)
            time.sleep(2)
        response = AdvEndpoints().start_adv_company(company_id=3499821)
        time.sleep(2)
        response1 = AdvEndpoints().stop_adv_company(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert response1.status_code == 200, f"Wrong status code! Status code is {response1.status_code}"

    def test_get_budget(self):
        response, data = AdvEndpoints().get_budget(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_card_placement(self):
        response = AdvEndpoints().get_card_placement(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_card_budget(self):
        response, data = AdvEndpoints().get_card_budget(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_balance(self):
        response = AdvEndpoints().get_balance()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_search_stats(self):
        response = AdvEndpoints().get_search_stats(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_card_stats(self):
        response = AdvEndpoints().get_card_stats(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_supplier_info(self):
        response = AdvEndpoints().get_supplier_info()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_order_stat(self):
        response = AdvEndpoints().get_order_stat()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_set_new_card_price(self):
        response = AdvEndpoints().set_new_card_price(company_id=3501540, price=400)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_start_adv_card_company(self):
        response = AdvEndpoints().get_card_placement(company_id=3501540)
        jsondata = response.json()
        current_status = jsondata['status']
        if current_status == 9:
            AdvEndpoints().stop_adv_card_company(company_id=3501540)
            time.sleep(2)
        response = AdvEndpoints().start_adv_card_company(company_id=3501540)
        response1 = AdvEndpoints().stop_adv_card_company(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert response1.status_code == 200, f"Wrong status code! Status code is {response1.status_code}"

    def test_get_full_company_stat(self):
        response = AdvEndpoints().get_full_company_stat(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_expenses(self):
        response = AdvEndpoints().get_expenses()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_companies(self):
        response = AdvEndpoints().get_companies()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

