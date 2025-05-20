# app/main.py

import pandas as pd
import streamlit as st
from utils import load_data, generate_boxplot, get_top_regions

# Set Streamlit app configuration
st.set_page_config(page_title="Global Insights Dashboard", layout="wide")

# Title
st.title("🌍 Global Health Insights Dashboard")

# Load CSVs and add a 'Country' column manually
dfs = [
    load_data("../data/processed/benin_clean.csv", country_name="Benin"),
    load_data("../data/processed/togo_clean.csv", country_name="Togo"),
    load_data("../data/processed/sierraleone_clean.csv", country_name="Sierra Leone"),
]
df = pd.concat(dfs, ignore_index=True)
df.columns = df.columns.str.strip()

# Sidebar Navigation
st.sidebar.title("📁 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Options", "Data"])

# ------------------ Home Page ------------------ #
if page == "Home":
    st.header("Welcome to the Global Health Insights Dashboard!")
    st.markdown("""
    This dashboard allows you to explore health and environmental data for selected countries.

    ### Features:
    - 📊 View GHI score distributions
    - 🎯 Filter data by country
    - 📋 Browse the full dataset

    Use the **sidebar** to navigate between sections.
    """)

# ------------------ Options Page ------------------ #
elif page == "Options":
    st.header("📊 Summary Visualizations")

    # Country Filter
    country_list = ["All Countries"] + sorted(df['Country'].unique().tolist())
    selected_country = st.sidebar.selectbox("Filter by Country", country_list)

    # Filter Data
    if selected_country == "All Countries":
        filtered_df = df
    else:
        filtered_df = df[df['Country'] == selected_country]

    # Boxplot
    st.subheader("GHI Score Distribution")
    if not filtered_df.empty:
        try:
            st.pyplot(generate_boxplot(filtered_df, column='GHI'))
        except KeyError:
            st.error("❌ Column 'GHI' not found in dataset.")
    else:
        st.warning("No data available for the selected country.")

    # Top Regions Table
    st.subheader("🏆 Top Regions by GHI Score")
    try:
        top_regions = get_top_regions(filtered_df, column='GHI', top_n=5)
        st.table(top_regions)
    except KeyError:
        st.warning("Region data not found; showing top countries only.")
        st.table(filtered_df.sort_values(by='GHI', ascending=False)[['Country', 'GHI']].head(5))

# ------------------ Data Page ------------------ #
elif page == "Data":
    st.header("📄 Full Dataset")
    st.dataframe(df)
