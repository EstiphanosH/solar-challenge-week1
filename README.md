# ☀️ Solar Data Analysis & Dashboard — Week 1 Challenge

This project is part of the Solar Challenge Week 1. It involves data cleaning, exploratory data analysis (EDA), cross-country solar potential comparison, and a visual dashboard built using Streamlit. The analysis focuses on three West African countries: **Benin**, **Sierra Leone**, and **Togo**, using solar radiation metrics such as GHI, DNI, and DHI.

---

## 📌 Project Goals

- Clean and preprocess solar datasets from multiple countries.
- Perform EDA and visualize environmental and solar metrics.
- Identify and handle missing values and outliers.
- Conduct statistical comparisons between countries.
- Build an interactive Streamlit dashboard for solar potential analysis.

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Pandas, NumPy, SciPy**
- **Matplotlib, Seaborn, Plotly**
- **Streamlit**
- **YData-Profiling**
- **scikit-posthocs** (optional for post-hoc tests)

---

---

## 🚀 Setup Instructions

Follow the steps below to set up and run the dashboard locally:

### 1. Clone the Repository

```bash
git clone https://github.com/EstiphanosH/solar-challenge-week1.git
cd solar-challenge-week1
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: .\venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the Streamlit App
```bash
streamlit run app.py
```
📊 Features
      Data Cleaning & Profiling
      
      Detect and impute missing values (median)
      
      Identify and remove outliers using Z-score
      
      Exploratory Data Analysis
      
      Correlation heatmaps
      
      Time series plots
      
      Scatter and bubble charts
      
      Country Comparison
      
      Boxplots of GHI, DNI, and DHI
      
      Kruskal–Wallis test for statistical comparison
      
      Insightful markdown summaries
      
      Interactive Streamlit Dashboard
      
      Country-based filtering
      
      Plot toggles
      
      Clean UI for non-technical users

    📈 Sample Visualizations
    GHI Boxplot by Country	Time Series Plot (GHI)


📌 Future Improvements
    Add post-hoc statistical testing (e.g., Dunn's test)
    
    Improve input validation and exception handling in the dashboard
    
    Add map-based visualizations of solar metrics
    
    Unit tests for modular code components

🪪 License
This project is licensed under the MIT License.

🙌 Acknowledgements
10 academy

Open-source contributors and dataset providers

✨ Author
Estiphanos H.
🔗 [github.com/EstiphanosH]

