# ChemData AI Platform — Architecture Overview

## Objective

ChemData AI Platform is a portfolio and product foundation for energy, commodity, and capital-markets use cases. It is designed to show how deterministic economics, structured workflow logic, and compliance-aware reasoning can coexist in a single technical system.

## Core components

### 1. Data layer
A lightweight CSV-based forward curve source is included for demonstration. In a production variant, this could be replaced by API, database, vendor feed, or internal market data snapshots.

### 2. Business model layer
Pydantic models enforce simple but explicit schemas for forward points, contracts, and regulation references.

### 3. Valuation layer
The valuation engine computes monthly spreads, discounted cashflows, aggregate present value, and bumped curve sensitivity.

### 4. Compliance layer
The compliance module maps market scenarios to likely framework references using an explainable matching catalog.

### 5. Workflow layer
Prompt templates and deterministic output builders generate reusable review structures for market intelligence, risk, compliance, and investment-committee style summarisation.

### 6. Interface layer
The Streamlit dashboard turns the repository into a demonstrable mini-platform suitable for portfolio presentation, service promotion, and future productisation.

## Why this architecture is portfolio-strong

- It demonstrates both deterministic commercial logic and AI workflow design.
- It balances implementation with explainability.
- It is small enough to understand quickly, but structured enough to look product-grade.
- It supports consulting, accelerator, and digital-product positioning.
