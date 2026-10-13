from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from chemdata_ai_platform.compliance import compliance_report
from chemdata_ai_platform.market_intelligence import market_intelligence_pack
from chemdata_ai_platform.models import FixedPriceContract
from chemdata_ai_platform.valuation import (
    curve_sensitivity,
    load_forward_curve_csv,
    price_fixed_contract,
)


@st.cache_data
def get_curve():
    return load_forward_curve_csv("data/sample_forward_curve.csv")


def main():
    st.set_page_config(page_title="ChemData AI Platform", layout="wide")
    st.title("ChemData AI Platform")
    st.caption("Energy, commodities, and capital-markets tooling for valuation, workflow design, and compliance-aware review.")

    tab1, tab2, tab3 = st.tabs(["Valuation Engine", "Compliance Checker", "Market Intelligence Pack"])

    with tab1:
        st.subheader("Deterministic valuation")
        col1, col2, col3 = st.columns(3)
        with col1:
            contract_name = st.text_input("Contract name", value="Q1 Baseload Hedge")
            volume = st.number_input("Monthly volume (MWh)", min_value=1.0, value=5000.0, step=500.0)
        with col2:
            fixed_price = st.number_input("Fixed price (USD/MWh)", min_value=1.0, value=78.0, step=1.0)
            discount_rate = st.number_input("Annual discount rate", min_value=0.0, max_value=1.0, value=0.08, step=0.01)
        with col3:
            bump = st.number_input("Curve bump (USD/MWh)", value=5.0, step=1.0)

        curve = get_curve()
        contract = FixedPriceContract(
            name=contract_name,
            monthly_volume_mwh=volume,
            fixed_price_usd_per_mwh=fixed_price,
            annual_discount_rate=discount_rate,
        )
        valuation = price_fixed_contract(contract, curve)
        sensitivity = curve_sensitivity(contract, curve, bump)

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Average forward", valuation["average_forward_price"])
        metric2.metric("Undiscounted value", valuation["total_undiscounted_value"])
        metric3.metric("MTM PV", valuation["mark_to_market_pv"])

        st.write("### Sensitivity")
        st.json(sensitivity)

        df = pd.DataFrame(valuation["cashflows"])
        st.dataframe(df, use_container_width=True)

        fig = px.bar(df, x="month", y="present_value", title="Present value by month")
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Compliance Scenario Checker")
        st.caption("Deterministic regulatory triage mapped to ACER REMIT, MAR, MiFID II, and CFTC Dodd-Frank.")
        
        scenario = st.text_area(
            "Scenario text",
            value="A trader receives non-public information about an unplanned outage at a major European gas facility and enters positions in wholesale gas contracts before the outage is publicly disclosed.",
            height=130,
        )
        
        from chemdata_ai_platform.compliance import check_compliance_scenario
        
        if scenario:
            result = check_compliance_scenario(scenario)
            
            if result.is_flagged:
                st.warning(f"⚠️ **{result.summary}**")
                
                # Display detailed Clause expanders with clickable official links
                for cit in result.citations:
                    with st.expander(f"📌 {cit.framework} — {cit.clause}: {cit.title}", expanded=True):
                        st.markdown(f"**Regulatory Rationale:** {cit.rationale}")
                        st.markdown(f"**Official Rulebook Reference:** [{cit.reference_url}]({cit.reference_url})")
            else:
                st.info(f"ℹ️ {result.summary}")
            
            with st.expander("Raw Triage JSON Payload"):
                st.json(result.model_dump())

    with tab3:
        st.subheader("Market intelligence pack")
        intel_text = st.text_area(
            "Market scenario",
            value="European power prices rise after nuclear outages and colder weather expectations increase winter demand.",
            height=150,
        )
        pack = market_intelligence_pack(intel_text)
        st.json(pack)


if __name__ == "__main__":
    main()
