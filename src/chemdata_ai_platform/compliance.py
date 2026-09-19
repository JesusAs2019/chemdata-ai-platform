from __future__ import annotations

from .models import RegulationRef

REGULATION_CATALOG = [
    RegulationRef(
        code="REMIT",
        title="Regulation on Wholesale Energy Market Integrity and Transparency",
        jurisdiction="EU Energy",
        url="https://remitportal.acer.europa.eu/",
        keywords=[
            "energy market manipulation",
            "wholesale energy",
            "inside information",
            "physical power",
            "gas trading",
            "market participant",
            "remit",
        ],
    ),
    RegulationRef(
        code="MiFID II",
        title="Markets in Financial Instruments Directive",
        jurisdiction="EU Financial Markets",
        url="https://eur-lex.europa.eu/eli/dir/2014/65/oj/eng",
        keywords=[
            "investment firm",
            "financial instrument",
            "execution",
            "client order",
            "trading venue",
            "algorithmic trading",
            "mifid",
        ],
    ),
    RegulationRef(
        code="MAR",
        title="Market Abuse Regulation",
        jurisdiction="EU Financial Markets",
        url="https://eur-lex.europa.eu/eli/reg/2014/596/oj/eng",
        keywords=[
            "market abuse",
            "inside information",
            "insider dealing",
            "unlawful disclosure",
            "market manipulation",
            "mar",
        ],
    ),
    RegulationRef(
        code="Dodd-Frank",
        title="Dodd-Frank swaps regulatory framework",
        jurisdiction="US Derivatives",
        url="https://www.cftc.gov/LawRegulation/DoddFrankAct/index.htm",
        keywords=[
            "swap",
            "swaps",
            "derivative",
            "clearing",
            "swap dealer",
            "margin",
            "dodd-frank",
            "cftc",
        ],
    ),
]


def score_regulations(text: str) -> list[dict]:
    text_lower = text.lower()
    results = []

    for reg in REGULATION_CATALOG:
        matched = [kw for kw in reg.keywords if kw.lower() in text_lower]
        if matched:
            results.append(
                {
                    "code": reg.code,
                    "title": reg.title,
                    "jurisdiction": reg.jurisdiction,
                    "url": str(reg.url),
                    "matched_keywords": matched,
                    "score": len(matched),
                }
            )

    return sorted(results, key=lambda x: x["score"], reverse=True)


def compliance_report(text: str) -> dict:
    matches = score_regulations(text)

    if not matches:
        return {
            "input_text": text,
            "summary": "No strong regulation match found from the current catalog.",
            "matches": [],
            "next_step": "Expand the catalog or refine the scenario wording.",
        }

    top_codes = ", ".join(item["code"] for item in matches[:3])

    return {
        "input_text": text,
        "summary": f"Potentially relevant frameworks: {top_codes}.",
        "matches": matches,
        "next_step": "Use the top matched frameworks as the starting point for legal/compliance review.",
    }
