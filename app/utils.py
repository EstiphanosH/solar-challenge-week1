import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ----------------------------
# Data Loading
# ----------------------------
def load_data(path, country_name=None):
    df = pd.read_csv(path)
    if country_name:
        df['Country'] = country_name
    df.columns = df.columns.str.strip()  # Clean column names
    return df


# ----------------------------
# Visualizations
# ----------------------------
def generate_radiation_boxplot(df, column='GHI'):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='Country', y=column, palette='Set2', ax=ax)
    ax.set_title(f'{column} Distribution by Country')
    ax.set_ylabel(column)
    ax.set_xlabel('Country')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def generate_investment_boxplot(df, column='ROI'):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='Country', y=column, palette='Set1', ax=ax)
    ax.set_title(f'{column} Distribution by Country')
    ax.set_ylabel(column)
    ax.set_xlabel('Country')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_time_series(df, columns=['GHI', 'DNI', 'DHI', 'Tamb'], title='Radiation Over Time'):
    df = df.copy()
    if 'Timestamp' not in df.columns:
        return px.line(title="❌ 'Timestamp' column not found")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df = df.dropna(subset=['Timestamp'])
    fig = px.line(df, x='Timestamp', y=columns, title=title)
    return fig


# ----------------------------
# Analytics / Filtering
# ----------------------------
def recommend_investments(df, sector=None, country=None, max_risk=None, min_roi=None):
    filtered = df.copy()
    if sector and sector != 'All':
        filtered = filtered[filtered['Sector'] == sector]
    if country and country != 'All':
        filtered = filtered[filtered['Country'] == country]
    if max_risk is not None:
        filtered = filtered[filtered['Risk'] <= max_risk]
    if min_roi is not None:
        filtered = filtered[filtered['ROI'] >= min_roi]
    return filtered.sort_values(by='ROI', ascending=False).head(10)

def get_top_projects(df, column='ROI', top_n=5):
    columns_to_show = ['Project', 'Country', 'Sector', 'ROI', 'Risk']
    available_columns = [col for col in columns_to_show if col in df.columns]
    return df.sort_values(by=column, ascending=False).head(top_n)[available_columns]

def get_top_regions(df, column='GHI', top_n=5):
    if 'Region' in df.columns:
        return df.sort_values(by=column, ascending=False)[['Region', 'Country', column]].head(top_n)
    else:
        return df.sort_values(by=column, ascending=False)[['Country', column]].head(top_n)
