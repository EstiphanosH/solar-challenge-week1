import streamlit as st
import pandas as pd

from utils import (
    load_data,
    plot_time_series,
    generate_investment_boxplot,
    generate_radiation_boxplot,
    get_top_regions,
    get_top_projects,
    recommend_investments,
)

# Page config
st.set_page_config(page_title="Solar Investment Insights", layout="centered")
st.title("🔆 Solar Radiation Analysis Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "Solar Radiation Insights", "Investment Explorer"]
selected_page = None
for page in pages:
    if st.sidebar.button(page):
        selected_page = page

if selected_page is None:
    selected_page = "Home"

# Load data once
benin_df = load_data("../data/processed/benin_clean.csv", country_name="Benin")
togo_df = load_data("../data/processed/togo_clean.csv", country_name="Togo")
sierra_df = load_data("../data/processed/sierraleone_clean.csv", country_name="Sierra Leone")
all_df = pd.concat([benin_df, togo_df, sierra_df], ignore_index=True)

# ----------------------------------
# 1. Home Page with Explanation & Time Series
# ----------------------------------
if selected_page == "Home":
    st.header("Welcome to the Solar Radiation Analysis Dashboard")

    st.markdown("""
    This dashboard helps stakeholders evaluate **solar radiation patterns** across selected countries
    to determine optimal locations for renewable energy investments.

    ### Features:
    - 🌞 **Solar Radiation Time Series**: Understand radiation trends over time.
    - 📈 **Investment Explorer**: Filter projects based on ROI and risk.
    - 🌍 **GHI Distribution**: Compare potential regions for investment.
    """)

    st.subheader("📊 Solar Radiation Over Time")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Benin")
        st.plotly_chart(plot_time_series(benin_df, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Benin Radiation"), use_container_width=True)

    with col2:
        st.markdown("#### Togo")
        st.plotly_chart(plot_time_series(togo_df, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Togo Radiation"), use_container_width=True)

    with col3:
        st.markdown("#### Sierra Leone")
        st.plotly_chart(plot_time_series(sierra_df, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title="Sierra Leone Radiation"), use_container_width=True)

# ----------------------------------
# 2. Solar Radiation Insights Page
# ----------------------------------
elif selected_page == "Solar Radiation Insights":
    st.header("🌍 Global Solar Radiation Distribution")

    countries = ["All Countries"] + sorted(all_df['Country'].unique())
    selected_country = st.selectbox("Select Country", countries)

    filtered_df = all_df if selected_country == "All Countries" else all_df[all_df["Country"] == selected_country]

    st.subheader("📈 GHI Distribution")
    if not filtered_df.empty:
        st.pyplot(generate_radiation_boxplot(filtered_df, column="GHI"))
    else:
        st.warning("No data for selected country.")

    st.subheader("🏆 Top Regions by GHI")
    try:
        st.table(get_top_regions(filtered_df, column='GHI', top_n=5))
    except KeyError:
        st.warning("Region data not available.")
        st.table(filtered_df.sort_values(by='GHI', ascending=False)[['Country', 'GHI']].head(5))

# ----------------------------------
# 3. Investment Explorer
# ----------------------------------
elif selected_page == "Investment Explorer":
    st.header("💼 Investment Opportunities")

    investment_df = load_data("../data/processed/investments_clean.csv")

    st.sidebar.subheader("Filter Investments")
    sector_options = ["All"] + sorted(investment_df["Sector"].dropna().unique())
    country_options = ["All"] + sorted(investment_df["Country"].dropna().unique())

    selected_sector = st.sidebar.selectbox("Sector", sector_options)
    selected_country = st.sidebar.selectbox("Country", country_options)
    max_risk = st.sidebar.slider("Maximum Risk", 0.0, 1.0, 0.5)
    min_roi = st.sidebar.slider("Minimum ROI", 0.0, 1.0, 0.3)

    filtered_investments = recommend_investments(
        investment_df,
        sector=selected_sector,
        country=selected_country,
        max_risk=max_risk,
        min_roi=min_roi
    )

    st.subheader("📊 ROI Distribution")
    st.pyplot(generate_investment_boxplot(investment_df, column='ROI'))

    st.subheader("🌟 Top Projects")
    if not filtered_investments.empty:
        st.dataframe(get_top_projects(filtered_investments))
    else:
        st.warning("No matching projects. Try different filters.")
