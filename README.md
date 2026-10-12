# **CHEMDATA AI PLATFORM — Energy & Capital Markets Suite**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chemdata-ai-platform.streamlit.app/)

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

[![Tests](https://img.shields.io/badge/pytest-100%25%20passed%20(7%2F7)-success.svg)](tests/)

[![Regulatory Mapping](https://img.shields.io/badge/compliance-REMIT%20%7C%20MAR%20%7C%20MiFID%20II%20%7C%20Dodd--Frank-emerald.svg)](src/chemdata_ai_platform/compliance.py)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## **ChemData AI Platform**

> **ChemData AI Platform is an enterprise-grade repository hosting deterministic, audit-ready quantitative valuation engines and proprietary trading architecture workflows for energy, commodities, and capital markets. Built for institutional trading desks, the platform integrates high-precision market intelligence with compliance-aware retrieval systems to automate complex scenario triage and risk mitigation.**

### **Why ChemData AI Matters**

+ Institutional Valuation & Intelligence: Delivers deterministic, audit-ready pricing and valuation engines alongside real-time market intelligence tailored for highly volatile energy and commodity sectors.
+ Production-Ready Trading Architecture: Centralizes critical quantitative tooling and high-throughput workflows into a single, scalable repository.
+ Automated Compliance Triage: Deploys sophisticated, compliance-aware retrieval systems to instantly triage legal, regulatory, and operational risk scenarios.

🌐 **Live Production App:** [https://chemdata-ai-platform.streamlit.app/](https://chemdata-ai-platform.streamlit.app/)  
📄 **Institutional QA Memo:** [Download Verification Report (PDF)](https://www.genspark.ai/api/files/s/He96QVQf)

---

## 🏛️ 5-Layer Institutional Architecture

The current version showcases Five layers:

1. **Deterministic valuation engines** for simple power and commodity contract economics.
2. **Market-intelligence workflow scaffolding** for strategist, risk, compliance, and investment-committee style outputs.
3. **Compliance-aware retrieval logic** mapped to official framework references such as ACER REMIT, MiFID II, MAR, and CFTC Dodd-Frank.
4. **Version 2 Streamlit interface** for interactive scenario testing, valuation review, and compliance triage.
5. **Operator surface and reporting suite** featuring a multi-tab Streamlit interface for interactive scenario testing alongside an automated PDF engine for audit-ready compliance exports.

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐ │ 5-LAYER SYSTEM STACK │ ├─────────────────────────────────────────────────────────────────────────────────────────────────┤ │ Layer 05: Operator Surface │ Multi-tab Streamlit Suite & PDF Audit Exporter │ │ Layer 04: Workflow Orchestration │ Audience-aware scenario formatting (CRO / Desk / Committee) │ │ Layer 03: Deterministic Engines │ Forward Curve Cashflow Discounting & Sensitivity Bumping │ │ Layer 02: Compliance Triage │ Citation-aware mapping (ACER REMIT, MAR, MiFID II, CFTC) │ │ Layer 01: Reference Data │ Pydantic v2 schemas & immutable audit records │ └─────────────────────────────────────────────────────────────────────────────────────────────────┘

---

## ⚡ Core Modules & Capabilities

### 1. Deterministic Valuation Engine (`chemdata_ai_platform.valuation`)

Prices fixed-price energy and commodity contracts against a monthly forward curve.

* **Cashflow Discounting:** Computes period-level spreads, undiscounted 
cashflows, and discounted present values (MTM PV) using exact compound discount factor curves.

* **Parallel Sensitivity Bumping:** Calculates base MTM, bumped MTM, and net sensitivity delta ($/MWh) for yield/price shifts.
* **Cashflow Scheduling:** Generates clean, auditable monthly payment breakdown tables and Plotly visualizations.

### 2. Compliance-Aware Scenario Triage (`chemdata_ai_platform.compliance`)

A deterministic, explainable scenario triage engine mapping free-text trading and physical operations to major European and US regulatory frameworks:

* **ACER REMIT:** Article 3 (Insider Trading) & Article 5 (Wholesale Energy Market Manipulation).

* **Market Abuse Regulation (MAR):** Article 8 (Insider Dealing) & Article 12 (Market Manipulation).
* **MiFID II Directive:** Article 17 & RTS 6 (Algorithmic Trading, Pre-trade Risk Limits & Governance).
* **CFTC Dodd-Frank Act:** Title VII (Uncleared Swaps, Mandatory Margin Obligations & Trade Reporting).

### 3. Market Intelligence & Workflow Scaffolding (`chemdata_ai_platform.market_intelligence`)

Generates structured, audience-aware memos and prompt bundles for:

* Market strategist reviews (power outages, gas storage deficit, fuel switching)
* Risk management scrutiny & sensitivity assessments
* Compliance review & regulatory audit trails
* Investment committee memo preparation

---

## 📂 Repository Structure

```text
chemdata-ai-platform/
├─ README.md
├─ LICENSE
├─ pyproject.toml
├─ requirements.txt
├─ packages.txt
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
│     ├─ app.py                 # Multi-tab Streamlit Operator Suite
│     ├─ compliance.py          # Regulatory keyword triage engine
│     ├─ main.py                # Unified CLI entrypoint
│     ├─ market_intelligence.py # Macro scenario summarizer
│     ├─ models.py              # Pydantic v2 data models
│     ├─ prompts.py             # Strategic prompt scaffolding
│     └─ valuation.py           # Forward curve discount & bump math
└─ tests/
   ├─ test_compliance.py
   ├─ test_market_intelligence.py
   └─ test_valuation.py

```

## 🛠️ **Tech Stack & Engineering Standards**

**Language**: Python 3.12+ (for the application core, type-annotated, modern packaging)
**Data Schemas & Validation**: Pydantic v2 (for type-safe business and regulation models)
**Data Manipulation**: Pandas & NumPy (for lightweight tabular presentation in the dashboard)
**Visualizations**: Plotly Interactive Charts (for valuation and cashflow visualisation)
**User Interface**: Streamlit (Multi-Tab Operator Suite, for an interactive portfolio-facing front end)
**Testing**: Pytest (for deterministic unit tests: 100% deterministic test pass across all modules)

## 💻 **CLI Usage & Quickstart**

### 1. **Installation & Environment Setup**

## **Clone repository**

```bash

git clone https://github.com/JesusAs2019/chemdata_ai_platform.git
cd chemdata_ai_platform
```

## Create & activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
```

## Install in editable mode

```bash
pip install -e .

```

## Run test suite (100% pass verification)

```bash
python -m pytest -v
```

## 2. **Standalone CLI Commands**

### **Contract Valuation & Sensitivity**

```bash
python -m chemdata_ai_platform.valuation --contract "Q1 Baseload Hedge" --volume 5000 --price 78.0 --rate 0.08 --bump 5.0
```

### **Regulatory Compliance Scenario Check**

python -m chemdata_ai_platform.compliance --scenario "Possible inside information in wholesale gas trading and unusual price movement before public disclosure."

### **Market Intelligence Scenario Synthesis**

python -m chemdata_ai_platform.market_intelligence --scenario "European gas prices rise after unplanned outages and increased winter demand expectations."

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

## 3. **Launching the Interactive Web Suite**

### Prompt bundle

```bash
chemdata-platform prompts
```

## Streamlit dashboard

Run the interface locally:

```bash
streamlit run src/chemdata_ai_platform/app.py
```

## 🔗 **Official Regulatory References**

ACER REMIT Portal: remitportal.acer.europa.eu

MiFID II Directive (2014/65/EU): eur-lex.europa.eu/eli/dir/2014/65

Market Abuse Regulation (MAR 596/2014): eur-lex.europa.eu/eli/reg/2014/596

CFTC Dodd-Frank Act: cftc.gov/LawRegulation/DoddFrankAct

## 🚀 **Future Roadmap & Phase 2 Expansion**

 - Hybrid semantic embeddings (FinBERT) for nuanced natural language regulatory triage.
 - Real-time regulatory feed ingestion (automated EU Official Journal & CFTC rule updates).
 - Multi-commodity option pricing models (Black-76 / Bachelier for crack and spark spreads).
 - Counterparty Credit Risk (CCR) and PFE (Potential Future Exposure) stress-testing engines.

## Other Next expansion ideas

+ scenario libraries for LNG, power, emissions, and refinery economics
+ optional FastAPI service layer
+ vector or citation-backed compliance retrieval
+ counterparty exposure and stress testing modules
+ downloadable committee memo exports

## 👨‍💻 **Engineering Leadership & Practice**

Jean Pierre Assiana — MSc Chemistry · Data Engineer & Regulated AI Solutions Architect

**Agency Portal**: https://chemdataai.com

**GitHub**: @JesusAs2019
