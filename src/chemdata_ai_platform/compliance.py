"""
ChemData AI Platform — Layer 02: Compliance Triage Engine
Deterministic, citation-aware regulatory mapping for Energy, Commodities, and Capital Markets.
Maps trade/operational scenarios to exact Articles and Clauses across ACER REMIT, MAR, MiFID II, and CFTC Dodd-Frank.
"""

from typing import List, Dict, Any, Optional
import re
from pydantic import BaseModel, Field


class RegulatoryCitation(BaseModel):
    framework: str = Field(..., description="Framework identifier, e.g. ACER REMIT, MAR, MiFID II, Dodd-Frank")
    clause: str = Field(..., description="Specific legal Article or Clause")
    title: str = Field(..., description="Title of the regulatory provision")
    reference_url: str = Field(..., description="Official regulatory link")
    rationale: str = Field(..., description="Why this scenario triggers this clause")


class ComplianceTriageResult(BaseModel):
    input_text: str
    is_flagged: bool
    summary: str
    matched_frameworks: List[str]
    citations: List[RegulatoryCitation]
    recommended_action: str


# Comprehensive Clause-Level Regulatory Catalog
REGULATORY_CATALOG = [
    {
        "framework": "ACER REMIT",
        "clause": "Article 3(1)(a) & Article 4",
        "title": "Prohibition of Insider Trading & Obligation to Publish Inside Information",
        "reference_url": "https://remitportal.acer.europa.eu/",
        "keywords": [
            r"outage", r"unplanned outage", r"non-public", r"inside information",
            r"gas facility", r"generation capacity", r"transmission capacity",
            r"power plant trip", r"pipeline disruption", r"before disclosure"
        ],
        "rationale": "Trading wholesale energy contracts with non-public material operational information before market-wide disclosure constitutes a potential REMIT Article 3 breach."
    },
    {
        "framework": "ACER REMIT",
        "clause": "Article 5",
        "title": "Prohibition of Market Manipulation in Wholesale Energy Markets",
        "reference_url": "https://remitportal.acer.europa.eu/",
        "keywords": [
            r"bidding behaviour", r"suspicious bidding", r"influence prices",
            r"tight supply", r"withholding capacity", r"artificial price",
            r"wash trade", r"layering", r"spoofing energy"
        ],
        "rationale": "Bidding strategies intended to distort wholesale electricity or gas benchmark settlement prices trigger market manipulation scrutiny under REMIT Article 5."
    },
    {
        "framework": "Market Abuse Regulation (MAR)",
        "clause": "Article 8 & Article 10",
        "title": "Prohibition of Insider Dealing and Unlawful Disclosure of Inside Information",
        "reference_url": "https://eur-lex.europa.eu/eli/reg/2014/596/oj/eng",
        "keywords": [
            r"insider dealing", r"unlawful disclosure", r"price-sensitive",
            r"confidential information", r"tipping", r"insider list",
            r"derivative on security", r"related financial instrument"
        ],
        "rationale": "Possessing price-sensitive confidential information regarding related financial instruments or traded equities triggers mandatory MAR Article 8 restrictions."
    },
    {
        "framework": "Market Abuse Regulation (MAR)",
        "clause": "Article 12",
        "title": "Definition and Prohibition of Market Manipulation",
        "reference_url": "https://eur-lex.europa.eu/eli/reg/2014/596/oj/eng",
        "keywords": [
            r"market manipulation", r"distort benchmark", r"fictitious device",
            r"collusion", r"misleading signals", r"cross-product manipulation"
        ],
        "rationale": "Entering orders or transactions that give false or misleading signals regarding the supply, demand, or price of financial instruments triggers MAR Article 12."
    },
    {
        "framework": "MiFID II Directive",
        "clause": "Article 17 & RTS 6",
        "title": "Algorithmic Trading Systems Governance, Pre-Trade Controls & Market Making",
        "reference_url": "https://eur-lex.europa.eu/eli/dir/2014/65/oj/eng",
        "keywords": [
            r"algorithmic", r"algo", r"execution algorithm", r"trading venue",
            r"pre-trade risk", r"kill switch", r"system governance",
            r"order-to-trade ratio", r"high frequency", r"hft", r"conformance testing"
        ],
        "rationale": "Deploying algorithmic execution models on EU trading venues requires documented governance, pre-trade kill-switches, and annual compliance reviews under MiFID II RTS 6."
    },
    {
        "framework": "CFTC Dodd-Frank Act",
        "clause": "Title VII (Section 731 / 17 CFR Part 23)",
        "title": "Swap Dealer Registration, Uncleared Swap Margin Obligations & Real-Time Reporting",
        "reference_url": "https://www.cftc.gov/LawRegulation/DoddFrankAct/index.htm",
        "keywords": [
            r"swap", r"swaps", r"uncleared swap", r"swap dealer",
            r"initial margin", r"variation margin", r"cftc", r"dodd-frank",
            r"sdr reporting", r"derivatives exposure", r"bilateral derivative"
        ],
        "rationale": "Bilateral derivatives and swap dealer activity trigger US CFTC Title VII compliance, mandatory margin rules for uncleared swaps, and swap data repository (SDR) trade reporting."
    }
]


def check_compliance_scenario(scenario_text: str) -> ComplianceTriageResult:
    """
    Evaluates free-text scenario against the regulatory catalog using deterministic regex keyword matching.
    Returns matched frameworks with exact Article/Clause citations and rationale.
    """
    if not scenario_text or not scenario_text.strip():
        return ComplianceTriageResult(
            input_text="",
            is_flagged=False,
            summary="Empty scenario provided.",
            matched_frameworks=[],
            citations=[],
            recommended_action="Provide a descriptive trade or operational scenario."
        )

    text_lower = scenario_text.lower()
    matched_citations: List[RegulatoryCitation] = []
    matched_framework_set = set()

    for item in REGULATORY_CATALOG:
        for pattern in item["keywords"]:
            if re.search(r"\b" + pattern + r"\b", text_lower, re.IGNORECASE):
                matched_citations.append(
                    RegulatoryCitation(
                        framework=item["framework"],
                        clause=item["clause"],
                        title=item["title"],
                        reference_url=item["reference_url"],
                        rationale=item["rationale"]
                    )
                )
                matched_framework_set.add(item["framework"])
                break  # Matched this catalog entry, continue to next rule

    if matched_citations:
        frameworks_list = sorted(list(matched_framework_set))
        summary = f"Flagged under {len(matched_citations)} regulatory clause(s) across: {', '.join(frameworks_list)}."
        rec_action = "Initiate formal trade review with Compliance/Legal. Log scenario in immutable audit ledger."
        is_flagged = True
    else:
        frameworks_list = []
        summary = "No immediate high-risk regulatory violation detected in the current catalog."
        rec_action = "Verify if scenario involves non-standard bespoke bilateral contracts or unlisted OTC products."
        is_flagged = False

    return ComplianceTriageResult(
        input_text=scenario_text.strip(),
        is_flagged=is_flagged,
        summary=summary,
        matched_frameworks=frameworks_list,
        citations=matched_citations,
        recommended_action=rec_action
    )
