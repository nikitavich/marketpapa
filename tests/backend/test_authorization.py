from lib.authorization import Authorization
import settings


class TestAuthorization:
    def test_get_wb_token_by_phone_number(self):
        wb_token, resp2, resp1 = Authorization().get_wb_token_by_phone_number(phone_number='79998074678', wild_auth_new=settings.wild_auth_new)
        assert resp2.status_code == 200, f'Wrong status code, {resp2.status_code}'
        assert resp1.status_code == 200, f'Wrong status code, {resp1.status_code}'



    def test_get_new_wb_token_by_wb_token_and_supplier_id(self):
        wb_token, resp2, resp1 = Authorization().get_wb_token_by_phone_number(phone_number='79998074678', wild_auth_new=settings.wild_auth_new)
        coken, res1, res2, resp3 = Authorization().get_new_wb_token_by_wb_token_and_supplier_id(wb_token=wb_token, supplier_id=settings.supplier_id)
        assert res1.status_code == 200, f'Wrong status code, {res1.status_code}'
        assert res2.status_code == 200, f'Wrong status code, {res2.status_code}'
        assert resp3.status_code == 200, f'Wrong status code, {resp3.status_code}'

