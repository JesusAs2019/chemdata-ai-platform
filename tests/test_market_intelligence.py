from chemdata_ai_platform.market_intelligence import market_intelligence_pack
from chemdata_ai_platform.prompts import prompt_bundle


def test_market_intelligence_pack_detects_gas_theme():
    pack = market_intelligence_pack("Gas supply disruption and LNG import pressure drive volatility")
    assert pack["theme"] == "gas"
    assert "recommendation" in pack


def test_prompt_bundle_contains_required_roles():
    prompts = prompt_bundle()
    assert "market_strategist" in prompts
    assert "risk_reviewer" in prompts
    assert "compliance_reviewer" in prompts
    assert "investment_committee_memo" in prompts
