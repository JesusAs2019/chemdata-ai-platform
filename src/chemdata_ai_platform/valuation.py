from __future__ import annotations

import csv
from pathlib import Path

from .models import FixedPriceContract, ForwardPoint


def load_forward_curve_csv(file_path: str | Path) -> list[ForwardPoint]:
    file_path = Path(file_path)
    curve: list[ForwardPoint] = []

    with file_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            curve.append(
                ForwardPoint(
                    month=row["month"],
                    price_usd_per_mwh=float(row["price_usd_per_mwh"]),
                )
            )
    return curve


def discount_factor(month_index: int, annual_discount_rate: float) -> float:
    monthly_rate = annual_discount_rate / 12
    return 1 / ((1 + monthly_rate) ** month_index)


def price_fixed_contract(contract: FixedPriceContract, curve: list[ForwardPoint]) -> dict:
    rows = []
    total_pv = 0.0
    total_undiscounted = 0.0

    for i, point in enumerate(curve, start=1):
        spread = point.price_usd_per_mwh - contract.fixed_price_usd_per_mwh
        undiscounted_cf = spread * contract.monthly_volume_mwh
        df = discount_factor(i, contract.annual_discount_rate)
        pv = undiscounted_cf * df

        rows.append(
            {
                "month": point.month,
                "forward_price": round(point.price_usd_per_mwh, 2),
                "spread": round(spread, 2),
                "undiscounted_cashflow": round(undiscounted_cf, 2),
                "discount_factor": round(df, 6),
                "present_value": round(pv, 2),
            }
        )
        total_undiscounted += undiscounted_cf
        total_pv += pv

    avg_forward = sum(p.price_usd_per_mwh for p in curve) / len(curve)

    return {
        "contract_name": contract.name,
        "months": len(curve),
        "monthly_volume_mwh": contract.monthly_volume_mwh,
        "fixed_price_usd_per_mwh": contract.fixed_price_usd_per_mwh,
        "average_forward_price": round(avg_forward, 2),
        "total_undiscounted_value": round(total_undiscounted, 2),
        "mark_to_market_pv": round(total_pv, 2),
        "cashflows": rows,
    }


def curve_sensitivity(contract: FixedPriceContract, curve: list[ForwardPoint], bump_usd_per_mwh: float) -> dict:
    bumped_curve = [
        ForwardPoint(
            month=point.month,
            price_usd_per_mwh=point.price_usd_per_mwh + bump_usd_per_mwh,
        )
        for point in curve
    ]

    base = price_fixed_contract(contract, curve)
    bumped = price_fixed_contract(contract, bumped_curve)

    return {
        "base_mtm": base["mark_to_market_pv"],
        "bumped_mtm": bumped["mark_to_market_pv"],
        "delta": round(bumped["mark_to_market_pv"] - base["mark_to_market_pv"], 2),
        "bump_usd_per_mwh": bump_usd_per_mwh,
    }
