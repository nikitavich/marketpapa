from lib.adv_endpoints import AdvEndpoints


class TestDeposit(AdvEndpoints):
    def test_deposit(self):
        response = AdvEndpoints().deposit(company_id=3499821, deposit=100, balance_type=1)
        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"