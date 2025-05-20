import pandas as pd
from pathlib import Path
from typing import Dict, Optional

def load_data(file_path: Path, parse_dates: Optional[list] = None) -> pd.DataFrame:
    try:
        suffix = file_path.suffix.lower()
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return pd.DataFrame()

        if suffix == '.csv':
            return pd.read_csv(file_path, parse_dates=parse_dates, low_memory=False)
        elif suffix in ['.xls', '.xlsx']:
            return pd.read_excel(file_path, parse_dates=parse_dates)
        elif suffix == '.json':
            return pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return pd.DataFrame()

def save_data(df: pd.DataFrame, file_path: Path) -> None:
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        suffix = file_path.suffix.lower()
        if suffix == '.csv':
            df.to_csv(file_path, index=False)
        elif suffix in ['.xls', '.xlsx']:
            df.to_excel(file_path, index=False)
        elif suffix == '.json':
            df.to_json(file_path, orient='records')
        else:
            raise ValueError(f"Unsupported file format: {suffix}")
        print(f"✅ Data saved to {file_path}")
    except Exception as e:
        print(f"❌ Error saving {file_path}: {e}")

def load_raw_data(data_paths: Dict[str, Path]) -> Dict[str, pd.DataFrame]:
    raw_data = {}
    for key, path in data_paths.items():
        if key.startswith("raw_"):
            raw_data[key] = load_data(path, parse_dates=["Timestamp"])
    return raw_data

def load_cleaned_data(data_paths: Dict[str, Path]) -> Dict[str, pd.DataFrame]:
    cleaned_data = {}
    for key, path in data_paths.items():
        if key.startswith("cleaned_"):
            cleaned_data[key] = load_data(path, parse_dates=["Timestamp"])
    return cleaned_data

def save_cleaned_data(datasets: Dict[str, pd.DataFrame], data_paths: Dict[str, Path]) -> None:
    for key, df in datasets.items():
        cleaned_key = key.replace("raw_", "cleaned_")
        if cleaned_key in data_paths:
            save_data(df, data_paths[cleaned_key])
        else:
            print(f"⚠️ No path found for {cleaned_key}, skipping save.")
