from chemdata_ai_platform.models import FixedPriceContract, ForwardPoint
from chemdata_ai_platform.valuation import curve_sensitivity, discount_factor, price_fixed_contract


def test_discount_factor_decreases_over_time():
    assert discount_factor(2, 0.12) < discount_factor(1, 0.12)


def test_fixed_contract_valuation_runs():
    contract = FixedPriceContract(
        monthly_volume_mwh=1000,
        fixed_price_usd_per_mwh=80,
        annual_discount_rate=0.06,
    )

    curve = [
        ForwardPoint(month="2026-10", price_usd_per_mwh=82),
        ForwardPoint(month="2026-11", price_usd_per_mwh=81),
        ForwardPoint(month="2026-12", price_usd_per_mwh=79),
    ]

    result = price_fixed_contract(contract, curve)

    assert result["months"] == 3
    assert "mark_to_market_pv" in result
    assert len(result["cashflows"]) == 3


def test_curve_sensitivity_responds_to_positive_bump():
    contract = FixedPriceContract(monthly_volume_mwh=1000, fixed_price_usd_per_mwh=75)
    curve = [
        ForwardPoint(month="2026-10", price_usd_per_mwh=76),
        ForwardPoint(month="2026-11", price_usd_per_mwh=77),
    ]
    result = curve_sensitivity(contract, curve, 3)
    assert result["delta"] > 0
