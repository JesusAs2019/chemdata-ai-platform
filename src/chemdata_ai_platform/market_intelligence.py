from __future__ import annotations

from .compliance import compliance_report


def _detect_theme(text: str) -> str:
    text_lower = text.lower()
    if any(word in text_lower for word in ["gas", "lng"]):
        return "gas"
    if any(word in text_lower for word in ["power", "electricity", "baseload", "peakload"]):
        return "power"
    if any(word in text_lower for word in ["oil", "crude", "refinery"]):
        return "oil"
    return "cross-commodity"


def _market_view(theme: str) -> str:
    mapping = {
        "gas": "Watch storage, weather, outage risk, and import optionality as primary price drivers.",
        "power": "Watch generation mix, weather, outages, and fuel pass-through for near-curve volatility.",
        "oil": "Watch supply disruptions, inventory changes, and refinery utilisation as core market catalysts.",
        "cross-commodity": "Assess curve dislocation, liquidity conditions, and macro transmission across related markets.",
    }
    return mapping[theme]


def _risk_view(theme: str) -> list[str]:
    common = [
        "Valuation risk: review sensitivity to curve moves and data-quality assumptions.",
        "Liquidity risk: assess executable depth across relevant tenors.",
        "Operational risk: confirm control points for market data, approvals, and escalation.",
    ]
    extras = {
        "gas": "Basis risk: review hub differentials, transport constraints, and seasonal storage optionality.",
        "power": "Shape risk: review hourly profile differences against monthly baseload assumptions.",
        "oil": "Crack-spread risk: review product exposure versus crude input assumptions.",
        "cross-commodity": "Correlation risk: test assumptions linking related commodity curves.",
    }
    return common + [extras[theme]]


def market_intelligence_pack(text: str) -> dict:
    theme = _detect_theme(text)
    compliance = compliance_report(text)

    recommendation = (
        "Escalate for structured review before action if conduct, disclosure, or market-integrity concerns are present."
        if compliance["matches"]
        else "Proceed with commercial review and expand scenario detail before formal escalation."
    )

    return {
        "scenario": text,
        "theme": theme,
        "market_strategist_summary": _market_view(theme),
        "risk_summary": _risk_view(theme),
        "compliance_summary": compliance["summary"],
        "recommendation": recommendation,
        "compliance_matches": compliance["matches"],
        "investment_committee_memo": {
            "commercial_context": text,
            "valuation_implications": "Review contract economics against relevant forward curves and sensitivity assumptions.",
            "risk_considerations": _risk_view(theme),
            "compliance_considerations": compliance["summary"],
            "recommendation": recommendation,
        },
    }
