import pandas as pd
from typing import Dict

def analyze_data(datasets: Dict[str, pd.DataFrame]) -> None:
    for name, df in datasets.items():
        if df.empty:
            print(f"⚠️ Skipping empty dataset: {name}")
            continue

        print(f"\n🔍 Analyzing {name}...")
        print(f"\n🔹 Shape: {df.shape}")
        print(f"🔹 Columns: {df.columns.tolist()}")
        print("\n📊 Summary Statistics:")
        print(df.describe(include='all'))

        print("\n🧼 Missing Values:")
        missing = df.isna().sum()
        missing_percent = df.isna().mean() * 100
        print(missing[missing > 0])

        print("\n❗Columns with >5% missing:")
        print(missing_percent[missing_percent > 5])
