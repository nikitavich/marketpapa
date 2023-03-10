from pydantic import BaseModel


class CompanyInfo(BaseModel):
    id: int
    name: str
    type: int
    statusId: int
    text: str
    url: str
    urlType: str
    siteUuid: str
    imagePath: str
    imgSrc: str
    formatId: str
    categoryUid: str
    campaignId: str
    campaignName: str
    brandId: str
    brandName: str
    supplierId: str
    supplierName: str
    createDate: str
    updateDate: str
    cancelDate: str
    startDate: str
    finishDate: str
    position: str
    sum: str
    placementType: str
    predictedDuration: str
    predictedStartDate: str
    predictedEndDate: str
    excludedBrands: str
    nomenclatures: str
    carouselCard: str
    products: str
    PromoSetId: str
    nm: str
    name: str
    subject: str
    subject: str
    id: str
    name: str
    brand: str
    id: str
    name: str
    kind: str
    id: str
    name: str
    categories: str


class Comp(BaseModel):
    pass
