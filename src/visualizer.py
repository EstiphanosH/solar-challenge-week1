from pathlib import Path
from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(datasets: Dict[str, pd.DataFrame], output_paths: Dict[str, Path]) -> None:
    for name, df in datasets.items():
        if df.empty:
            print(f"⚠️ Skipping visualizations for empty dataset: {name}")
            continue

        print(f"📈 Creating visualizations for {name}...")

        dataset_key = name.split('_')[1]  # e.g. 'togo' from 'cleaned_togo'
        figures_path = output_paths['figures'] / dataset_key
        figures_path.mkdir(parents=True, exist_ok=True)

        plot_histogram(df, 'GHI', figures_path)
        plot_time_series(df, 'Timestamp', 'GHI', figures_path)
        plot_scatter(df, 'RH', 'Tamb', figures_path)
        plot_scatter(df, 'RH', 'GHI', figures_path)
        plot_bubble(df, 'GHI', 'Tamb', 'RH', figures_path)

def plot_histogram(df: pd.DataFrame, column: str, output_path: Path) -> None:
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=20, edgecolor='black')
    plt.title(f'{column} Distribution')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(output_path / f'{column}_hist.png')
    plt.close()

def plot_time_series(df: pd.DataFrame, time_col: str, value_col: str, output_path: Path) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(df[time_col], df[value_col])
    plt.title(f'{value_col} Over Time')
    plt.xlabel(time_col)
    plt.ylabel(value_col)
    plt.grid(True)
    plt.savefig(output_path / f'{value_col}_timeseries.png')
    plt.close()

def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, output_path: Path) -> None:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(f'{x_col} vs {y_col}')
    plt.savefig(output_path / f'{x_col}_vs_{y_col}.png')
    plt.close()

def plot_bubble(df: pd.DataFrame, x: str, y: str, size: str, output_path: Path) -> None:
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x], df[y], s=df[size], alpha=0.5, c='orange', edgecolors='w')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{x} vs {y} (Bubble = {size})')
    plt.savefig(output_path / f'{x}_vs_{y}_bubble_{size}.png')
    plt.close()
