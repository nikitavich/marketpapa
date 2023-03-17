import time

from lib.adv_endpoints import AdvEndpoints


class TestAdvEndpoints:
    # Кампания для автотестов поиск = 3499821
    # Кампания для автотестов карточка товара = 3501540
    def setup(self):
        self.advendpoints = AdvEndpoints()

    def test_get_company_info(self):
        response = self.advendpoints.get_company_info(company_id=3499821)
        data = response.json()
        id_field = 'id'
        name_field = 'name'
        type_field = 'type'
        statusId_field = 'statusId'
        text_field = 'text'
        url_field = 'url'
        urlType_field = 'urlType'
        siteUuid_field = 'siteUuid'
        imagePath_filed = 'imagePath'
        imgSrc_field = 'imgSrc'
        formatId_field = 'formatId'
        categoryUid_field = 'categoryUid'
        campaignId_field = 'campaignId'
        campaignName_field = 'campaignName'
        brandId_field = 'brandId'
        brandName_field = 'brandName'
        supplierId_field = 'supplierId'
        supplierName_field = 'supplierName'
        createDate_field = 'createDate'
        updateDate_field = 'updateDate'
        cancelDate_field = 'cancelDate'
        startDate_field = 'startDate'
        finishDate_field = 'finishDate'
        position_field = 'position'
        sum_field_field = 'sum'
        placementType_field = 'placementType'
        predictedDuration_field = 'predictedDuration'
        predictedStartDate_field = 'predictedStartDate'
        predictedEndDate_field = 'predictedEndDate'
        excludedBrands_field = 'excludedBrands'
        nomenclatures_field = 'nomenclatures'
        carouselCard_field = 'carouselCard'
        products_field = 'products'
        PromoSetId_field = 'PromoSetId'
        products_nm_fiend = 'nm'
        products_name_field = 'name'
        subject_field = 'subject'
        subject_id_field = 'id'
        subject_name_field = 'name'
        products_brand_field = 'brand'
        brand_id_field = 'id'
        brand_name_field = 'name'
        products_kind_field = 'kind'
        kind_id = 'id'
        kind_name = 'name'
        products_categories = 'categories'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert id_field in data, f"Key {id_field} doesn't exist in the dictionary"
        assert name_field in data, f"Key {name_field} doesn't exist in the dictionary"
        assert type_field in data, f"Key {type_field} doesn't exist in the dictionary"
        assert statusId_field in data, f"Key {statusId_field} doesn't exist in the dictionary"
        assert text_field in data, f"Key {text_field} doesn't exist in the dictionary"
        assert url_field in data, f"Key {url_field} doesn't exist in the dictionary"
        assert urlType_field in data, f"Key {urlType_field} doesn't exist in the dictionary"
        assert siteUuid_field in data, f"Key {siteUuid_field} doesn't exist in the dictionary"
        assert imagePath_filed in data, f"Key {imagePath_filed} doesn't exist in the dictionary"
        assert imgSrc_field in data, f"Key {imgSrc_field} doesn't exist in the dictionary"
        assert formatId_field in data, f"Key {formatId_field} doesn't exist in the dictionary"
        assert categoryUid_field in data, f"Key {categoryUid_field} doesn't exist in the dictionary"
        assert campaignId_field in data, f"Key {campaignId_field} doesn't exist in the dictionary"
        assert campaignName_field in data, f"Key {campaignName_field} doesn't exist in the dictionary"
        assert brandId_field in data, f"Key {brandId_field} doesn't exist in the dictionary"
        assert brandName_field in data, f"Key {brandName_field} doesn't exist in the dictionary"
        assert supplierId_field in data, f"Key {supplierId_field} doesn't exist in the dictionary"
        assert createDate_field in data, f"Key {createDate_field} doesn't exist in the dictionary"
        assert updateDate_field in data, f"Key {updateDate_field} doesn't exist in the dictionary"
        assert cancelDate_field in data, f"Key {cancelDate_field} doesn't exist in the dictionary"
        assert startDate_field in data, f"Key {startDate_field} doesn't exist in the dictionary"
        assert finishDate_field in data, f"Key {finishDate_field} doesn't exist in the dictionary"
        assert position_field in data, f"Key {position_field} doesn't exist in the dictionary"
        assert sum_field_field in data, f"Key {sum_field_field} doesn't exist in the dictionary"
        assert predictedDuration_field in data, f"Key {predictedDuration_field} doesn't exist in the dictionary"
        assert predictedStartDate_field in data, f"Key {predictedStartDate_field} doesn't exist in the dictionary"
        assert predictedEndDate_field in data, f"Key {predictedEndDate_field} doesn't exist in the dictionary"
        assert excludedBrands_field in data, f"Key {excludedBrands_field} doesn't exist in the dictionary"
        assert supplierName_field in data, f"Key {supplierName_field} doesn't exist in the dictionary"
        assert placementType_field in data, f"Key {placementType_field} doesn't exist in the dictionary"
        assert nomenclatures_field in data, f"Key {nomenclatures_field} doesn't exist in the dictionary"
        assert carouselCard_field in data, f"Key {carouselCard_field} doesn't exist in the dictionary"
        assert products_field in data, f"Key {products_field} doesn't exist in the dictionary"
        assert PromoSetId_field in data, f"Key {PromoSetId_field} doesn't exist in the dictionary"
        assert products_nm_fiend in data['products'][0], f"Key {products_nm_fiend} doesn't exist in the dictionary"
        assert products_name_field in data['products'][0], f"Key {products_name_field} doesn't exist in the dictionary"
        assert subject_field in data['products'][0], f"Key {subject_field} doesn't exist in the dictionary"
        assert subject_id_field in data['products'][0][
            'subject'], f"Key {subject_id_field} doesn't exist in the dictionary"
        assert subject_name_field in data['products'][0][
            'subject'], f"Key {subject_name_field} doesn't exist in the dictionary"
        assert products_brand_field in data['products'][
            0], f"Key {products_brand_field} doesn't exist in the dictionary"
        assert brand_id_field in data['products'][0]['brand'], f"Key {brand_id_field} doesn't exist in the dictionary"
        assert brand_name_field in data['products'][0][
            'brand'], f"Key {brand_name_field} doesn't exist in the dictionary"
        assert products_kind_field in data['products'][0], f"Key {products_kind_field} doesn't exist in the dictionary"
        assert kind_id in data['products'][0]['kind'], f"Key {kind_id} doesn't exist in the dictionary"
        assert kind_name in data['products'][0]['kind'], f"Key {kind_name} doesn't exist in the dictionary"
        assert products_categories in data['products'][0], f"Key {products_categories} doesn't exist in the dictionary"

    def test_get_placement_info(self):
        response = self.advendpoints.get_placement_info(company_id=3499821)
        data = response.json()

        budget_field = 'budget'
        budget_total_field = 'total'
        budget_dailyMax_field = 'dailyMax'
        minCPM_field = 'minCPM'
        stepCPM_field = 'stepCPM'
        locale_field = 'locale'
        place_field = 'place'
        place_keyWord_field = 'keyWord'
        place_subjectId_field = 'subjectId'
        place_price_field = 'price'
        place_placesInfo_field = 'placesInfo'
        placesInfo_estimatedPlaces_field = 'estimatedPlaces'
        placesInfo_entryPrices_field = 'entryPrices'
        placesInfo_info_field = 'info'
        info_place_field = 'place'
        info_price_field = 'price'
        info_count_field = 'count'
        place_searchElements_field = 'searchElements'
        searchElements_nm_field = 'nm'
        searchElements_name_field = 'name'
        searchElements_brand_field = 'brand'
        searchElements_active_field = 'active'
        searchElements_stock_field = 'stock'
        place_dailyBudget_field = 'dailyBudget'
        place_intervals_field = 'intervals'
        place_excludedWords_field = 'excludedWords'
        limited_field = 'limited'
        nmsCount_field = 'nmsCount'
        name_field = 'name'
        status_field = 'status'
        fixed_field = 'fixed'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

        assert budget_field in data, f"Key {budget_field} doesn't exist in the dictionary"
        assert budget_total_field in data['budget'], f"Key {budget_total_field} doesn't exist in the dictionary"
        assert budget_dailyMax_field in data['budget'], f"Key {budget_dailyMax_field} doesn't exist in the dictionary"
        assert minCPM_field in data, f"Key {minCPM_field} doesn't exist in the dictionary"
        assert stepCPM_field in data, f"Key {stepCPM_field} doesn't exist in the dictionary"
        assert locale_field in data, f"Key {locale_field} doesn't exist in the dictionary"
        assert place_field in data, f"Key {place_field} doesn't exist in the dictionary"
        assert place_keyWord_field in data['place'][0], f"Key {place_keyWord_field} doesn't exist in the dictionary"
        assert place_subjectId_field in data['place'][0], f"Key {place_subjectId_field} doesn't exist in the dictionary"
        assert place_price_field in data['place'][0], f"Key {place_price_field} doesn't exist in the dictionary"
        assert place_placesInfo_field in data['place'][
            0], f"Key {place_placesInfo_field} doesn't exist in the dictionary"
        assert placesInfo_estimatedPlaces_field in data['place'][0][
            'placesInfo'], f"Key {placesInfo_estimatedPlaces_field} doesn't exist in the dictionary"
        assert placesInfo_entryPrices_field in data['place'][0][
            'placesInfo'], f"Key {placesInfo_entryPrices_field} doesn't exist in the dictionary"
        assert placesInfo_info_field in data['place'][0][
            'placesInfo'], f"Key {placesInfo_info_field} doesn't exist in the dictionary"
        assert info_place_field in data['place'][0]['placesInfo']['info'][
            0], f"Key {info_place_field} doesn't exist in the dictionary"
        assert info_price_field in data['place'][0]['placesInfo']['info'][
            0], f"Key {info_price_field} doesn't exist in the dictionary"
        assert info_count_field in data['place'][0]['placesInfo']['info'][
            0], f"Key {info_count_field} doesn't exist in the dictionary"
        assert place_searchElements_field in data['place'][
            0], f"Key {place_searchElements_field} doesn't exist in the dictionary"
        assert searchElements_nm_field in data['place'][0]['searchElements'][
            0], f"Key {searchElements_nm_field} doesn't exist in the dictionary"
        assert searchElements_name_field in data['place'][0]['searchElements'][
            0], f"Key {searchElements_name_field} doesn't exist in the dictionary"
        assert searchElements_brand_field in data['place'][0]['searchElements'][
            0], f"Key {searchElements_brand_field} doesn't exist in the dictionary"
        assert searchElements_active_field in data['place'][0]['searchElements'][
            0], f"Key {searchElements_active_field} doesn't exist in the dictionary"
        assert searchElements_stock_field in data['place'][0]['searchElements'][
            0], f"Key {searchElements_stock_field} doesn't exist in the dictionary"
        assert place_dailyBudget_field in data['place'][
            0], f"Key {place_dailyBudget_field} doesn't exist in the dictionary"
        assert place_intervals_field in data['place'][0], f"Key {place_intervals_field} doesn't exist in the dictionary"
        assert limited_field in data, f"Key {limited_field} doesn't exist in the dictionary"
        assert nmsCount_field in data, f"Key {nmsCount_field} doesn't exist in the dictionary"
        assert name_field in data, f"Key {name_field} doesn't exist in the dictionary"
        assert status_field in data, f"Key {status_field} doesn't exist in the dictionary"
        assert fixed_field in data, f"Key {fixed_field} doesn't exist in the dictionary"
        assert place_excludedWords_field in data['place'][
            0], f"Key {place_excludedWords_field} doesn't exist in the dictionary"

    def test_set_excluded_keywords(self):
        response = self.advendpoints.set_excluded_keywords(company_id=3499821, keywords=["одежда"])
        print(response.status_code)
        print(response.text)

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

        cash_field = 'cash'
        netting_field = 'netting'
        total_field = 'total'
        daily_budget_field = 'daily_budget'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert cash_field in data, f"Key {cash_field} doesn't exist in the dictionary"
        assert netting_field in data, f"Key {netting_field} doesn't exist in the dictionary"
        assert total_field in data, f"Key {total_field} doesn't exist in the dictionary"
        assert daily_budget_field in data, f"Key {daily_budget_field} doesn't exist in the dictionary"

    def test_get_card_placement(self):
        response = self.advendpoints.get_card_placement(company_id=3501540)
        data = response.json()

        budget_field = 'budget'
        budget_total_field = 'total'
        budget_dailyMax_field = 'dailyMax'
        minCPM_field = 'minCPM'
        stepCPM_field = 'stepCPM'
        excludedBrands_field = 'excludedBrands'
        locale_field = 'locale'
        place_field = 'place'
        place_subjectId_field = 'subjectId'
        place_subject_field = 'subject'
        place_kindId_field = 'kindId'
        place_kind_field = 'kind'
        place_price_field = 'price'
        place_placesInfo_field = 'placesInfo'
        placesInfo_estimatedPlaces_field = 'estimatedPlaces'
        placesInfo_entryPrices_field = 'entryPrices'
        place_carouselElements_field = 'carouselElements'
        carouselElements_nm_field = 'nm'
        carouselElements_name_field = 'name'
        carouselElements_brand_field = 'brand'
        carouselElements_active_field = 'active'
        place_intervals_field = 'intervals'
        limited_field = 'limited'
        nmsCount_field = 'nmsCount'
        name_field = 'name'
        status_field = 'status'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

        assert budget_field in data, f"Key {budget_field} doesn't exist in the dictionary"
        assert budget_total_field in data['budget'], f"Key {budget_total_field} doesn't exist in the dictionary"
        assert budget_dailyMax_field in data['budget'], f"Key {budget_dailyMax_field} doesn't exist in the dictionary"
        assert minCPM_field in data, f"Key {minCPM_field} doesn't exist in the dictionary"
        assert stepCPM_field in data, f"Key {stepCPM_field} doesn't exist in the dictionary"
        assert excludedBrands_field in data, f"Key {excludedBrands_field} doesn't exist in the dictionary"
        assert locale_field in data, f"Key {locale_field} doesn't exist in the dictionary"
        assert place_field in data, f"Key {place_field} doesn't exist in the dictionary"
        assert place_subjectId_field in data['place'][0], f"Key {place_subjectId_field} doesn't exist in the dictionary"
        assert place_subject_field in data['place'][0], f"Key {place_subject_field} doesn't exist in the dictionary"
        assert place_kindId_field in data['place'][0], f"Key {place_kindId_field} doesn't exist in the dictionary"
        assert place_kind_field in data['place'][0], f"Key {place_kind_field} doesn't exist in the dictionary"
        assert place_price_field in data['place'][0], f"Key {place_price_field} doesn't exist in the dictionary"
        assert place_placesInfo_field in data['place'][
            0], f"Key {place_placesInfo_field} doesn't exist in the dictionary"
        assert placesInfo_estimatedPlaces_field in data['place'][0][
            'placesInfo'], f"Key {placesInfo_estimatedPlaces_field} doesn't exist in the dictionary"
        assert placesInfo_entryPrices_field in data['place'][0][
            'placesInfo'], f"Key {placesInfo_entryPrices_field} doesn't exist in the dictionary"
        assert place_carouselElements_field in data['place'][
            0], f"Key {place_carouselElements_field} doesn't exist in the dictionary"
        assert carouselElements_nm_field in data['place'][0]['carouselElements'][
            0], f"Key {carouselElements_nm_field} doesn't exist in the dictionary"
        assert carouselElements_name_field in data['place'][0]['carouselElements'][
            0], f"Key {carouselElements_name_field} doesn't exist in the dictionary"
        assert carouselElements_brand_field in data['place'][0]['carouselElements'][
            0], f"Key {carouselElements_brand_field} doesn't exist in the dictionary"
        assert carouselElements_active_field in data['place'][0]['carouselElements'][
            0], f"Key {carouselElements_active_field} doesn't exist in the dictionary"
        assert place_intervals_field in data['place'][0], f"Key {place_intervals_field} doesn't exist in the dictionary"
        assert limited_field in data, f"Key {limited_field} doesn't exist in the dictionary"
        assert nmsCount_field in data, f"Key {nmsCount_field} doesn't exist in the dictionary"
        assert name_field in data, f"Key {name_field} doesn't exist in the dictionary"
        assert status_field in data, f"Key {status_field} doesn't exist in the dictionary"

    def test_get_card_budget(self):
        response, data = self.advendpoints.get_card_budget(company_id=3501540)
        cash_field = 'cash'
        netting_field = 'netting'
        total_field = 'total'
        daily_budget_field = 'daily_budget'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"
        assert cash_field in data, f"Key {cash_field} doesn't exist in the dictionary"
        assert netting_field in data, f"Key {netting_field} doesn't exist in the dictionary"
        assert total_field in data, f"Key {total_field} doesn't exist in the dictionary"
        assert daily_budget_field in data, f"Key {daily_budget_field} doesn't exist in the dictionary"

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

    def test_get_balance(self):
        response = self.advendpoints.get_balance()
        data = response.json()

        httpStatus_field = 'httpStatus'
        error_field = 'error'
        code_field = 'code'
        totalCount_field = 'totalCount'
        pageCount_field = 'pageCount'
        content_field = 'content'
        content_balance_field = 'balance'
        content_net_field = 'net'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

        assert httpStatus_field in data, f"Key {httpStatus_field} doesn't exist in the dictionary"
        assert error_field in data, f"Key {error_field} doesn't exist in the dictionary"
        assert code_field in data, f"Key {code_field} doesn't exist in the dictionary"
        assert pageCount_field in data, f"Key {pageCount_field} doesn't exist in the dictionary"
        assert content_field in data, f"Key {content_field} doesn't exist in the dictionary"
        assert totalCount_field in data, f"Key {totalCount_field} doesn't exist in the dictionary"
        assert content_balance_field in data['content'], f"Key {content_balance_field} doesn't exist in the dictionary"
        assert content_net_field in data['content'], f"Key {content_net_field} doesn't exist in the dictionary"

    def test_get_search_stats(self):
        response = self.advendpoints.get_search_stats(company_id=3499821)
        data = response.json()

        advertId_field = 'advertId'
        keyword_field = 'keyword'
        advertName_field = 'advertName'
        campaignName_field = 'campaignName'
        begin_field = 'begin'
        end_field = 'end'
        views_field = 'views'
        clicks_field = 'clicks'
        frq_field = 'frq'
        ctr_field = 'ctr'
        cpc_field = 'cpc'
        duration_field = 'duration'
        sum_field = 'sum'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

        assert advertId_field in data[0], f"Key {advertId_field} doesn't exist in the dictionary"
        assert keyword_field in data[0], f"Key {keyword_field} doesn't exist in the dictionary"
        assert advertName_field in data[0], f"Key {advertName_field} doesn't exist in the dictionary"
        assert campaignName_field in data[0], f"Key {campaignName_field} doesn't exist in the dictionary"
        assert begin_field in data[0], f"Key {begin_field} doesn't exist in the dictionary"
        assert end_field in data[0], f"Key {end_field} doesn't exist in the dictionary"
        assert views_field in data[0], f"Key {views_field} doesn't exist in the dictionary"
        assert clicks_field in data[0], f"Key {clicks_field} doesn't exist in the dictionary"
        assert frq_field in data[0], f"Key {frq_field} doesn't exist in the dictionary"
        assert ctr_field in data[0], f"Key {ctr_field} doesn't exist in the dictionary"
        assert cpc_field in data[0], f"Key {cpc_field} doesn't exist in the dictionary"
        assert duration_field in data[0], f"Key {duration_field} doesn't exist in the dictionary"
        assert sum_field in data[0], f"Key {sum_field} doesn't exist in the dictionary"

    def test_get_card_stats(self):
        response = self.advendpoints.get_card_stats(company_id=3501540)
        data = response.json()

        advertId_field = 'advertId'
        kind_field = 'kind'
        subject_field = 'subject'
        advertName_field = 'advertName'
        campaignName_field = 'campaignName'
        begin_field = 'begin'
        end_field = 'end'
        views_field = 'views'
        clicks_field = 'clicks'
        frq_field = 'frq'
        ctr_field = 'ctr'
        cpc_field = 'cpc'
        duration_field = 'duration'
        sum_field = 'sum'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

        assert advertId_field in data[0], f"Key {advertId_field} doesn't exist in the dictionary"
        assert kind_field in data[0], f"Key {kind_field} doesn't exist in the dictionary"
        assert subject_field in data[0], f"Key {subject_field} doesn't exist in the dictionary"
        assert advertName_field in data[0], f"Key {advertName_field} doesn't exist in the dictionary"
        assert campaignName_field in data[0], f"Key {campaignName_field} doesn't exist in the dictionary"
        assert begin_field in data[0], f"Key {begin_field} doesn't exist in the dictionary"
        assert end_field in data[0], f"Key {end_field} doesn't exist in the dictionary"
        assert views_field in data[0], f"Key {views_field} doesn't exist in the dictionary"
        assert clicks_field in data[0], f"Key {clicks_field} doesn't exist in the dictionary"
        assert frq_field in data[0], f"Key {frq_field} doesn't exist in the dictionary"
        assert ctr_field in data[0], f"Key {ctr_field} doesn't exist in the dictionary"
        assert cpc_field in data[0], f"Key {cpc_field} doesn't exist in the dictionary"
        assert duration_field in data[0], f"Key {duration_field} doesn't exist in the dictionary"
        assert sum_field in data[0], f"Key {sum_field} doesn't exist in the dictionary"

    def test_get_supplier_info(self):
        response = self.advendpoints.get_supplier_info()
        data = response.json()

        isExcluded_field = 'isExcluded'
        isSpecial_field = 'isSpecial'
        supplier_field = 'supplier'
        supplier_id_field = 'id'
        supplier_address_field = 'address'
        supplier_bankAccount_field = 'bankAccount'
        supplier_bic_field = 'bic'
        supplier_correspondentAccount_field = 'correspondentAccount'
        supplier_email_field = 'email'
        supplier_fullName_field = 'fullName'
        supplier_inn_field = 'inn'
        supplier_kpp_field = 'kpp'
        supplier_manager_field = 'manager'
        supplier_shortName_field = 'shortName'
        supplier_ogrn_field = 'ogrn'
        supplier_phone_field = 'phone'
        supplier_mainContractId_field = 'mainContractId'
        supplier_changeDate_field = 'changeDate'
        supplier_notificationEmail_field = 'notificationEmail'
        supplier_notificationPhone_field = 'notificationPhone'
        supplier_isSpecial_field = 'isSpecial'
        supplier_isAgency_field = 'isAgency'
        contract_field = 'contract'
        contract_ContractId_field = 'ContractId'
        contract_SupplierId_field = 'SupplierId'
        contract_Date_field = 'Date'
        contract_Code_field = 'Code'

        assert response.status_code == 200, f"Wrong status code! Status code is {response.status_code}"

        assert isExcluded_field in data, f"Key {isExcluded_field} doesn't exist in the dictionary"
        assert isSpecial_field in data, f"Key {isSpecial_field} doesn't exist in the dictionary"
        assert supplier_field in data, f"Key {supplier_field} doesn't exist in the dictionary"
        assert supplier_id_field in data['supplier'], f"Key {supplier_id_field} doesn't exist in the dictionary"
        assert supplier_address_field in data[
            'supplier'], f"Key {supplier_address_field} doesn't exist in the dictionary"
        assert supplier_bankAccount_field in data[
            'supplier'], f"Key {supplier_bankAccount_field} doesn't exist in the dictionary"
        assert supplier_bic_field in data['supplier'], f"Key {supplier_bic_field} doesn't exist in the dictionary"
        assert supplier_correspondentAccount_field in data[
            'supplier'], f"Key {supplier_correspondentAccount_field} doesn't exist in the dictionary"
        assert supplier_email_field in data['supplier'], f"Key {supplier_email_field} doesn't exist in the dictionary"
        assert supplier_fullName_field in data[
            'supplier'], f"Key {supplier_fullName_field} doesn't exist in the dictionary"
        assert supplier_inn_field in data['supplier'], f"Key {supplier_inn_field} doesn't exist in the dictionary"
        assert supplier_kpp_field in data['supplier'], f"Key {supplier_kpp_field} doesn't exist in the dictionary"
        assert supplier_manager_field in data[
            'supplier'], f"Key {supplier_manager_field} doesn't exist in the dictionary"
        assert supplier_shortName_field in data[
            'supplier'], f"Key {supplier_shortName_field} doesn't exist in the dictionary"
        assert supplier_ogrn_field in data['supplier'], f"Key {supplier_ogrn_field} doesn't exist in the dictionary"
        assert supplier_phone_field in data['supplier'], f"Key {supplier_phone_field} doesn't exist in the dictionary"
        assert supplier_mainContractId_field in data[
            'supplier'], f"Key {supplier_mainContractId_field} doesn't exist in the dictionary"
        assert supplier_changeDate_field in data[
            'supplier'], f"Key {supplier_changeDate_field} doesn't exist in the dictionary"
        assert supplier_notificationEmail_field in data[
            'supplier'], f"Key {supplier_notificationEmail_field} doesn't exist in the dictionary"
        assert supplier_notificationPhone_field in data[
            'supplier'], f"Key {supplier_notificationPhone_field} doesn't exist in the dictionary"
        assert supplier_isSpecial_field in data[
            'supplier'], f"Key {supplier_isSpecial_field} doesn't exist in the dictionary"
        assert supplier_isAgency_field in data[
            'supplier'], f"Key {supplier_isAgency_field} doesn't exist in the dictionary"
        assert contract_field in data, f"Key {contract_field} doesn't exist in the dictionary"
        assert contract_ContractId_field in data[
            'contract'], f"Key {contract_ContractId_field} doesn't exist in the dictionary"
        assert contract_SupplierId_field in data[
            'contract'], f"Key {contract_SupplierId_field} doesn't exist in the dictionary"
        assert contract_Date_field in data['contract'], f"Key {contract_Date_field} doesn't exist in the dictionary"
        assert contract_Code_field in data['contract'], f"Key {contract_Code_field} doesn't exist in the dictionary"

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
