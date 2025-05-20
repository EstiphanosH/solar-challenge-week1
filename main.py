from pathlib import Path
from src.paths import get_data_paths, get_output_paths, ensure_directories_exist
from src.processor import process_and_clean_data
from src.analyzer import analyze_data
from src.visualizer import create_visualizations
from src.loader import load_cleaned_data

def main():
    print("\n🚀 Starting data analysis pipeline...")

    dataset_files = [
        "togo-dapaong_qc.csv",
        "sierraleone-bumbuna.csv",
        "benin-malanville.csv"
    ]

    data_paths = {}
    for file in dataset_files:
        key = Path(file).stem.split("-")[0].lower()
        paths = get_data_paths(file)
        data_paths[f"raw_{key}"] = paths['raw']
        data_paths[f"cleaned_{key}"] = paths['cleaned']

    output_paths = get_output_paths()

    # Make sure output and cleaned directories exist
    ensure_directories_exist({**data_paths, **output_paths})

    print("\n📂 Step 1: Loading, preprocessing, and cleaning data...")
    process_and_clean_data(data_paths)

    print("\n📊 Step 2: Performing data analysis...")
    cleaned_datasets = load_cleaned_data(data_paths)
    analyze_data(cleaned_datasets)

    print("\n📈 Step 3: Creating visualizations...")
    create_visualizations(cleaned_datasets, output_paths)

    print("\n✅ Data analysis pipeline completed successfully.")

if __name__ == "__main__":
    main()
