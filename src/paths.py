from pathlib import Path
import sys
from typing import Dict

def get_repo_root() -> Path:
    """
    Returns the root of the repository by searching upward for a known file or folder.
    Works reliably in both Jupyter notebooks and scripts.
    """
    current_path = Path.cwd() if 'ipykernel' in sys.modules else Path(__file__).resolve().parent

    for parent in [current_path] + list(current_path.parents):
        if (parent / ".git").exists() or (parent / "data").exists() or (parent / "src").exists():
            return parent

    raise RuntimeError("Repository root not found. Make sure you're inside the project directory.")

def get_data_paths(dataset_file: str) -> Dict[str, Path]:
    """
    For a dataset filename (e.g., 'togo-dapaong_qc.csv'),
    returns a dict with 'raw' and 'cleaned' Path objects.
    """
    root = get_repo_root()
    dataset_name = Path(dataset_file).name
    return {
        'raw': root / 'data' / 'raw' / dataset_name,
        'cleaned': root / 'data' / 'cleaned' / f'cleaned_{dataset_name}'
    }

def get_output_paths() -> Dict[str, Path]:
    root = get_repo_root()
    return {
        'figures': root / 'reports' / 'figures'
    }

def ensure_directories_exist(paths: Dict[str, Path]) -> None:
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
