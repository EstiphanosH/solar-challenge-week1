# 🌞 Solar Dashboard App

This directory contains the core code for the **Solar Challenge Week 1** interactive dashboard, which visualizes solar irradiance data using Streamlit and Plotly. The app is designed for exploring trends in solar energy measurements with country-level filtering and time series plots.

---

## 📁 Folder Contents

app/

  ├── main.py # Main Streamlit application

  └── utils.py # Utility functions for data loading and plotting

---

## 🧪 Expected Input Data

The app works with solar measurement datasets CSV file typically located in the `../data/` folder. A valid dataset should include the following columns:

- `datetime`: Timestamps of solar measurements
- `ghi`: Global Horizontal Irradiance (in W/m²)
- `country`: Country name or location label

---

## 🚀 Running the App

### 1. Navigate to the `app/` directory

```bash
cd app
```
### 2. Install Dependencies (from project root)
```bash
pip install -r ../requirements.txt
```
### 3. Launch the Streamlit App
```bash
streamlit run main.py
```
## 🛠️ Tech Stack

Streamlit – for building the web UI

Plotly – for creating responsive, interactive charts

Pandas – for handling and transforming tabular data

## 🧩 Code Overview

  main.py
    Handles Streamlit layout and interactivity
    Loads data and displays visualizations
    Calls reusable logic from utils.py


  utils.py
    Contains functions for:
    Reading and cleaning solar data
    Creating Plotly plots (e.g., time series, boxplots)
    Filtering by country


## 📌 Notes
Make sure the dataset is available in the expected location (../data/) before running the app.

Customize or extend the app by adding new plots or filters in main.py and helper functions in utils.py.


## 📃 License
This project is part of the Solar Challenge series and is licensed under the MIT License.

Let me know if you'd like to include demo screenshots, a Streamlit Cloud deployment badge, or links to sample data.










Tools


