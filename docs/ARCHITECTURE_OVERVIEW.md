# ChemData AI Platform — Architecture Overview & Technical Specification

**Target Audience:** Institutional Investors, Technical Contractors, Recruiters, and Compliance Officers  
**Platform Scope:** Enterprise-grade, 5-layer institutional architecture supporting energy, commodities, and capital markets trading desks with deterministic valuation engines, programmatic compliance triage, and real-time market intelligence.

---

## 1. Executive Objective & System Topology

The **ChemData AI Platform** is designed to demonstrate how deterministic contract economics, structured workflow logic, and compliance-aware reasoning coexist in a single production system.

The platform implements a strict bottom-up data isolation and execution pattern to guarantee deterministic outputs, strict schema enforcement, and complete auditability.

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐ │ 5-LAYER SYSTEM STACK │ ├─────────────────────────────────────────────────────────────────────────────────────────────────┤ │ Layer 05: Operator Surface │ Multi-tab Streamlit Suite & PDF Audit Exporter │ │ Layer 04: Workflow Orchestration │ Audience-aware scenario formatting (CRO / Desk / Committee) │ │ Layer 03: Deterministic Engines │ Forward Curve Cashflow Discounting & Sensitivity Bumping │ │ Layer 02: Compliance Triage │ Citation-aware mapping (ACER REMIT, MAR, MiFID II, CFTC) │ │ Layer 01: Reference Data │ Pydantic v2 schemas & immutable audit records │ └─────────────────────────────────────────────────────────────────────────────────────────────────┘

---

## 2. Layer-by-Layer Technical Specification

### Layer 01: Reference Data & Schemas (Foundation)

* **Core Responsibility:** Data ingestion, strict type validation, and immutable data ledgering.
* **Tech Stack Components:** `Pydantic v2`, `Apache Arrow / Parquet / CSV`, `SQLite / PostgreSQL`.
* **Implementation Detail:** Extends Pydantic v2 `BaseModel` schemas to enforce strict typing on complex power and commodity forward curves, trade tickets, and historical settlement data. Every change or calculation state generates an audit trail, ensuring complete data lineage from the root layer.

### Layer 02: Compliance Triage

* **Core Responsibility:** Contextual matching and citation mapping against global regulatory frameworks.
* **Tech Stack Components:** `Deterministic Keyword Triage`, `Regex Engines`, `Regulatory Knowledge Catalog`.
* **Implementation Detail:** Maps semantic parameters of trade exceptions and scenario stresses directly to official regulatory rulesets including **ACER REMIT**, **MiFID II**, **MAR**, and **CFTC Dodd-Frank**, isolating potential compliance breaches before trade execution.

### Layer 03: Deterministic Valuation Engines

* **Core Responsibility:** Mathematical execution of contract economics, discounting, and risk parameters without heuristic drift.
* **Tech Stack Components:** `NumPy`, `SciPy`, `Pandas`.
* **Implementation Detail:** Pure, stateless functions execute forward-curve cash flow discounting and financial sensitivity bumping (Delta, $/MWh parallel shift). By design, these engines avoid ML-based approximation to maintain zero-variance repeatability for internal auditors and regulators.

### Layer 04: Workflow Orchestration

* **Core Responsibility:** Contextual formatting, event-driven state compilation, and persona-based message routing.
* **Tech Stack Components:** `Jinja2`, `Pydantic Workflow Models`.
* **Implementation Detail:** Translates complex mathematical structures into targeted outputs for distinct organizational stakeholders (customized risk metrics for the CRO, granular trading telemetry for the Front Office Desk, or high-level risk summaries for the Investment Committee).

### Layer 05: Operator Surface (Top-Layer Delivery)

* **Core Responsibility:** Human-in-the-loop interactive control, visualization, and dynamic report generation.
* **Tech Stack Components:** `Streamlit Framework`, `Plotly`, `PDF Verification Exporters`.
* **Implementation Detail:** A high-performance multi-tab dashboard enabling real-time scenario simulation, contract stress-testing, and compliance evaluation. Compiles Layers 01–04 into verifiable audit summaries suitable for internal sign-off and regulatory submission.

---

## 3. Why This Architecture is Institutionally Strong

* **Balances Determinism with Workflow Design:** Mathematical calculations remain 100% deterministic and auditable, while AI/heuristics are isolated to workflow summarization and prompt scaffolding.
* **Audit-Proof & Citation-Aware:** Explicitly references authoritative regulatory frameworks (REMIT Art. 3/5, MAR Art. 8/12, MiFID II RTS 6, Dodd-Frank Title VII).
* **Modular & Replaceable:** Data sources (CSV to Live API) and storage layers can be swapped without touching the valuation math or compliance engines.
* **Commercially Ready:** Serves as the technical engine supporting consulting advisory, accelerator products, and enterprise digital tooling.

---

## 4. Contractor Onboarding & Codebase Standards

To maintain institutional code quality and compliance readiness, all development must strictly adhere to the following guidelines:

1. **Zero-Variance Math:** All calculation pathways in Layer 03 must remain completely deterministic. No stochastic processes or heuristic approximations are permitted unless explicitly isolated under statistical testing structures.
2. **Strict Type Validation:** All external data models must map directly to Layer 01 Pydantic models. Dynamic typing on core trade models will fail CI/CD validation.
3. **Comprehensive Logging:** Every calculation, user action, and scenario mutation must trigger structured logs that feed directly into the audit layer.
