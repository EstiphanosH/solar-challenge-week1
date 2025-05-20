# ☀️ Solar Data Analysis: Benin, Togo, Sierra Leone

This repository contains a series of Jupyter notebooks that perform **exploratory data analysis (EDA)** on solar irradiance and weather datasets from **Benin**, **Togo**, and **Sierra Leone**. The analysis is structured in two main stages:

---

## 1. Country-Specific EDA

For each country (**Benin**, **Togo**, **Sierra Leone**), there is a dedicated notebook that:

- Loads and inspects the raw solar and weather data.
- Explores data quality by checking for missing values and outliers.
- Cleans the data (imputing missing values, handling outliers).
- Visualizes key variables such as solar irradiance (GHI, DNI, DHI), temperature, wind, and humidity.
- Examines relationships between variables (e.g., correlation heatmaps, scatterplots).
- Saves a cleaned version of the dataset for further analysis.

These notebooks help understand the unique solar resource characteristics and data quality issues for each country.

---

## 2. Cross-Country Comparison

After cleaning, the datasets from all three countries are combined in a comparison notebook that:

- Merges the cleaned data and adds a country label.
- Compares key solar metrics (GHI, DNI, DHI) across countries using boxplots and summary tables.
- Performs statistical testing (Kruskal–Wallis test) to determine if differences in solar potential are significant.
- Highlights key findings, such as which country has the highest or most stable solar resources.
- Provides visual summaries (e.g., bar charts of average GHI) to support investment and planning decisions.

---

## 📊 Outputs

- Cleaned datasets for each country (`../data/processed/`)
- Plots and summary statistics (`../plots/`, `../data/processed/summary_statistics.csv`)
- Key insights for solar energy potential and recommendations for each country

---

## 🚀 How to Use

1. Run the country-specific EDA notebooks to clean and explore each dataset.
2. Run the comparison notebook to analyze and visualize differences between countries.
3. Use the outputs to inform solar project development and policy decisions.

---

## 📝 Notes

- The EDA process ensures data quality and provides actionable insights for solar energy planning in West Africa.
- For details on each step, see the individual notebooks in this directory.