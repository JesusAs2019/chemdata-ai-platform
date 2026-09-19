from chemdata_ai_platform.compliance import compliance_report, score_regulations


def test_remit_and_mar_can_match_inside_information_text():
    results = score_regulations("Potential inside information and market manipulation in wholesale energy trading")
    codes = [item["code"] for item in results]
    assert "REMIT" in codes
    assert "MAR" in codes


def test_compliance_report_returns_empty_match_when_irrelevant():
    report = compliance_report("General discussion about weather patterns and office planning")
    assert report["matches"] == []
