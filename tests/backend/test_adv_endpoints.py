import time

from lib.adv_endpoints import AdvEndpoints


class TestAdvEndpoints:
    # Кампания для автотестов поиск = 3499821
    # Кампания для автотестов карточка товара = 3501540
    def setup(self):
        self.advendpoints = AdvEndpoints()

    def test_get_company_info(self):
        response = self.advendpoints.get_company_info(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_placement_info(self):
        response = self.advendpoints.get_placement_info(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_set_excluded_keywords(self):
        response = self.advendpoints.set_excluded_keywords(company_id=3499821, keywords=["одежда"])
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_set_new_price(self):
        response = self.advendpoints.set_new_price(company_id=3499821, price=583)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_stop_adv_company(self):
        response = self.advendpoints.get_placement_info(company_id=3499821)
        jsondata = response.json()
        current_status = jsondata['status']
        if current_status == 11:
            self.advendpoints.start_adv_company(company_id=3499821)
            time.sleep(2)
        response1 = self.advendpoints.stop_adv_company(company_id=3499821)
        assert response1.status_code == 200, f"Wrong status code! Status code is {response1.status_code}"

    def test_start_adv_company(self):
        response = self.advendpoints.get_placement_info(company_id=3499821)
        jsondata = response.json()
        current_status = jsondata['status']
        if current_status == 9:
            self.advendpoints.stop_adv_company(company_id=3499821)
            time.sleep(2)
        response = self.advendpoints.start_adv_company(company_id=3499821)
        time.sleep(2)
        response1 = self.advendpoints.stop_adv_company(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert response1.status_code == 200, f"Wrong status code! Status code is {response1.status_code}"

    def test_get_budget(self):
        response, data = self.advendpoints.get_budget(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_card_placement(self):
        response = self.advendpoints.get_card_placement(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_card_budget(self):
        response, data = self.advendpoints.get_card_budget(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_balance(self):
        response = self.advendpoints.get_balance()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_search_stats(self):
        response = self.advendpoints.get_search_stats(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_card_stats(self):
        response = self.advendpoints.get_card_stats(company_id=3499821)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_supplier_info(self):
        response = self.advendpoints.get_supplier_info()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_order_stat(self):
        response = self.advendpoints.get_order_stat()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_set_new_card_price(self):
        response = self.advendpoints.set_new_card_price(company_id=3501540, price=400)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_start_adv_card_company(self):
        response = self.advendpoints.get_card_placement(company_id=3501540)
        jsondata = response.json()
        current_status = jsondata['status']
        if current_status == 9:
            self.advendpoints.stop_adv_card_company(company_id=3501540)
            time.sleep(2)
        response = self.advendpoints.start_adv_card_company(company_id=3501540)
        response1 = self.advendpoints.stop_adv_card_company(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert response1.status_code == 200, f"Wrong status code! Status code is {response1.status_code}"

    def test_get_full_company_stat(self):
        response = self.advendpoints.get_full_company_stat(company_id=3501540)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_expenses(self):
        response = self.advendpoints.get_expenses()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_companies(self):
        response = self.advendpoints.get_companies()
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
