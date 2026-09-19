# ChemData AI Platform

A dedicated platform repository for the practice's energy, commodity, and capital-markets tooling — deterministic valuation engines, trading architecture workflows, and compliance-aware retrieval systems.

## Platform focus

ChemData AI Platform is designed as a portfolio-grade technical repository for demonstrating how commercial valuation, structured market workflows, and compliance-aware reasoning can be combined in one explainable Python project.

The current version showcases four layers:

1. **Deterministic valuation engines** for simple power and commodity contract economics.
2. **Market-intelligence workflow scaffolding** for strategist, risk, compliance, and investment-committee style outputs.
3. **Compliance-aware retrieval logic** mapped to official framework references such as ACER REMIT, MiFID II, MAR, and CFTC Dodd-Frank.
4. **Version 2 Streamlit interface** for interactive scenario testing, valuation review, and compliance triage.

## Repository structure

```text
chemdata-ai-platform/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ pyproject.toml
├─ data/
│  └─ sample_forward_curve.csv
├─ docs/
│  ├─ ARCHITECTURE_OVERVIEW.md
│  └─ REPOSITORY_REPORT.md
├─ prompts/
│  └─ market_workflows.md
├─ src/
│  └─ chemdata_ai_platform/
│     ├─ __init__.py
│     ├─ app.py
│     ├─ compliance.py
│     ├─ main.py
│     ├─ market_intelligence.py
│     ├─ models.py
│     ├─ prompts.py
│     └─ valuation.py
└─ tests/
   ├─ test_compliance.py
   ├─ test_market_intelligence.py
   └─ test_valuation.py
```

## Tech stack

- **Python 3.10+** for the application core
- **Pydantic** for type-safe business and regulation models
- **Pandas** for lightweight tabular presentation in the dashboard
- **Plotly** for valuation and cashflow visualisation
- **Streamlit** for an interactive portfolio-facing front end
- **Pytest** for deterministic unit tests

## What the repository demonstrates

### 1) Deterministic valuation
The valuation engine prices a simple fixed-price energy or commodity contract against a monthly forward curve. It returns period-level spreads, undiscounted cashflows, discounted present values, aggregate MTM, and curve-bump sensitivity.

### 2) Compliance-aware retrieval
The compliance module uses a transparent keyword-matching approach to map a scenario description to potentially relevant market frameworks. This is deliberately explainable rather than opaque, making it suitable for demonstration, prototyping, and future expansion into retrieval-augmented compliance workflows.

### 3) Market-intelligence workflow design
The platform includes reusable prompts and deterministic memo scaffolding for:
- market strategist review
- risk scrutiny
- compliance review
- investment committee memo preparation

### 4) Version 2 dashboard
The Streamlit application allows a user to:
- adjust contract parameters
- run valuation and sensitivity
- inspect period cashflows and charts
- paste a market or conduct scenario
- see which frameworks may be relevant
- generate a structured market-intelligence summary pack

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## CLI usage

### Valuation
```bash
chemdata-platform valuation --name "Q1 Baseload Hedge" --volume 5000 --fixed-price 78 --bump 5
```

### Compliance scenario check
```bash
chemdata-platform compliance --text "Possible inside information in wholesale gas trading and unusual price movement before public disclosure."
```

### Market-intelligence summary
```bash
chemdata-platform market-intel --text "European gas prices rise after unplanned outages and increased winter demand expectations."
```

### Prompt bundle
```bash
chemdata-platform prompts
```

## Streamlit dashboard

Run the interface locally:

```bash
streamlit run src/chemdata_ai_platform/app.py
```

## Suggested positioning on ChemDataAI.com

**ChemData AI Platform** can be presented as:

> A portfolio-grade repository for energy, commodities, and capital-markets tooling — combining deterministic valuation engines, market-intelligence workflow design, and compliance-aware retrieval systems.

## Official framework references used in the repository

- ACER REMIT Portal: https://remitportal.acer.europa.eu/
- MiFID II: https://eur-lex.europa.eu/eli/dir/2014/65/oj/eng
- Market Abuse Regulation: https://eur-lex.europa.eu/eli/reg/2014/596/oj/eng
- CFTC Dodd-Frank swaps framework: https://www.cftc.gov/LawRegulation/DoddFrankAct/index.htm

## Next expansion ideas

- scenario libraries for LNG, power, emissions, and refinery economics
- optional FastAPI service layer
- vector or citation-backed compliance retrieval
- counterparty exposure and stress testing modules
- downloadable committee memo exports

