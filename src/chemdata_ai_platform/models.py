from pydantic import BaseModel, Field, HttpUrl


class ForwardPoint(BaseModel):
    month: str
    price_usd_per_mwh: float = Field(gt=0)


class FixedPriceContract(BaseModel):
    name: str = "Base Load Power Contract"
    monthly_volume_mwh: float = Field(gt=0)
    fixed_price_usd_per_mwh: float = Field(gt=0)
    annual_discount_rate: float = Field(ge=0, le=1, default=0.08)


class RegulationRef(BaseModel):
    code: str
    title: str
    jurisdiction: str
    url: HttpUrl
    keywords: list[str]
