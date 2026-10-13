"""Unit tests for Layer 02: Compliance Triage Engine."""

from chemdata_ai_platform.compliance import check_compliance_scenario


def test_remit_insider_trading_scenario():
    scenario = "A trader receives non-public information about an unplanned outage at a major European gas facility and enters positions in wholesale gas contracts before disclosure."
    res = check_compliance_scenario(scenario)
    assert res.is_flagged is True
    assert "ACER REMIT" in res.matched_frameworks
    assert any("Article 3" in c.clause for c in res.citations)


def test_mifid_algo_trading_scenario():
    scenario = "An investment firm uses algorithmic execution strategies on an EU trading venue and needs pre-trade risk controls."
    res = check_compliance_scenario(scenario)
    assert res.is_flagged is True
    assert "MiFID II Directive" in res.matched_frameworks


def test_dodd_frank_swaps_scenario():
    scenario = "A derivatives desk is reviewing uncleared swap activity, margin obligations, and whether the firm's swap dealer controls align with US expectations."
    res = check_compliance_scenario(scenario)
    assert res.is_flagged is True
    assert "CFTC Dodd-Frank Act" in res.matched_frameworks
