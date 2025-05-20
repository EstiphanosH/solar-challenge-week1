from pathlib import Path
from typing import Dict
import pandas as pd
from src.loader import load_raw_data, save_cleaned_data

def process_and_clean_data(data_paths: Dict[str, Path]) -> None:
    raw_data = load_raw_data(data_paths)
    cleaned_data = {}

    for name, df in raw_data.items():
        if df.empty:
            print(f"⚠️ Skipping empty dataset: {name}")
            continue

        print(f"🧽 Cleaning dataset: {name}...")

        numeric_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())

        if 'Cleaning' in df.columns:
            df['Cleaning'] = pd.to_numeric(df['Cleaning'], errors='coerce').fillna(0).astype(int)

        cleaned_data[name] = df

    save_cleaned_data(cleaned_data, data_paths)
