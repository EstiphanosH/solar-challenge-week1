# ⚙️ Source Code – `src/` Directory

This folder contains the core backend logic for the **Solar Challenge Week 1** project. It includes modules for loading, processing, analyzing, and visualizing solar irradiance data. These modules work together to support the interactive dashboard built with Streamlit.

---

## 📁 Directory Structure

src/
    ├── __init__.py # Initializes the folder as a Python package 
    ├── analyzer.py # Performs statistical or trend analysis on solar data
    ├── loader.py # Loads solar data from CSV/Excel files
    ├── paths.py # Defines standard paths used throughout the project
    ├── processor.py # Handles data cleaning and transformation
    └── visualizer.py # Creates visualizations (e.g., time series, boxplots)

---

## 🔧 Module Descriptions

### `loader.py`
- Loads solar irradiance data from local files
- Supports CSV and Excel formats
- Ensures proper datetime parsing and column validation

### `processor.py`
- Cleans and transforms raw data
- Handles missing values, normalization, and type conversions
- Prepares data for analysis and visualization

### `analyzer.py`
- Performs data analysis such as:
  - Summary statistics
  - Trend detection
  - Grouped aggregations

### `visualizer.py`
- Generates interactive visualizations using Plotly
- Common charts include time series plots and boxplots by country

### `paths.py`
- Centralizes file and directory paths (e.g., data sources)
- Useful for managing file I/O across environments

### `__init__.py`
- Marks the `src/` directory as a package for imports

---

## 🧪 Example Usage

```python
from src.loader import load_data
from src.processor import clean_data
from src.analyzer import summarize
from src.visualizer import plot_ghi_timeseries

# Load and prepare data
df = load_data("../data/solar.csv")
df_clean = clean_data(df)
summary = summarize(df_clean)
fig = plot_ghi_timeseries(df_clean)

```
📌 Notes
Ensure src/ is in your Python path when running the app or tests.

Modules are designed to be reusable and testable.

Extend functionality by adding new analysis or visual tools to analyzer.py and visualizer.py.

📃 License
This module is part of the Solar Challenge Week 1 project and is released under the MIT License.

---







