from __future__ import annotations

import argparse
import json
from pathlib import Path

from .compliance import compliance_report
from .market_intelligence import market_intelligence_pack
from .models import FixedPriceContract
from .prompts import prompt_bundle
from .valuation import curve_sensitivity, load_forward_curve_csv, price_fixed_contract


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_curve_path() -> Path:
    return repo_root() / "data" / "sample_forward_curve.csv"


def handle_valuation(args):
    contract = FixedPriceContract(
        name=args.name,
        monthly_volume_mwh=args.volume,
        fixed_price_usd_per_mwh=args.fixed_price,
        annual_discount_rate=args.discount_rate,
    )
    curve = load_forward_curve_csv(args.curve_file)
    result = price_fixed_contract(contract, curve)

    if args.bump is not None:
        result["sensitivity"] = curve_sensitivity(contract, curve, args.bump)

    print(json.dumps(result, indent=2))


def handle_compliance(args):
    result = compliance_report(args.text)
    print(json.dumps(result, indent=2))


def handle_prompts(_args):
    print(json.dumps(prompt_bundle(), indent=2))


def handle_market_intel(args):
    result = market_intelligence_pack(args.text)
    print(json.dumps(result, indent=2))


def run():
    parser = argparse.ArgumentParser(prog="chemdata-platform")
    subparsers = parser.add_subparsers(dest="command", required=True)

    valuation_parser = subparsers.add_parser("valuation", help="Price a fixed-price contract")
    valuation_parser.add_argument("--name", default="Demo Power Contract")
    valuation_parser.add_argument("--curve-file", default=str(default_curve_path()))
    valuation_parser.add_argument("--volume", type=float, default=5000)
    valuation_parser.add_argument("--fixed-price", type=float, default=78.0)
    valuation_parser.add_argument("--discount-rate", type=float, default=0.08)
    valuation_parser.add_argument("--bump", type=float, default=None)
    valuation_parser.set_defaults(func=handle_valuation)

    compliance_parser = subparsers.add_parser("compliance", help="Map scenario text to regulation references")
    compliance_parser.add_argument("--text", required=True)
    compliance_parser.set_defaults(func=handle_compliance)

    prompts_parser = subparsers.add_parser("prompts", help="Print workflow prompt pack")
    prompts_parser.set_defaults(func=handle_prompts)

    intel_parser = subparsers.add_parser("market-intel", help="Generate a structured market intelligence pack")
    intel_parser.add_argument("--text", required=True)
    intel_parser.set_defaults(func=handle_market_intel)

    args = parser.parse_args()
    args.func(args)
