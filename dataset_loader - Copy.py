from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent


def load_sensor_dataset(filename):
    """Load and inspect a CSV sensor dataset."""

    # Only allow CSV files inside the project's data folder.
    data_dir = (PROJECT_DIR / "data").resolve()
    path = (data_dir / filename).resolve()

    if path.parent != data_dir:
        raise ValueError("Dataset must be inside the data folder.")

    if not path.is_file() or path.suffix.lower() != ".csv":
        raise FileNotFoundError("CSV dataset not found in data folder.")

    data = pd.read_csv(path)

    if data.empty:
        raise ValueError("Dataset is empty.")

    return {
        "filename": path.name,
        "rows": len(data),
        "columns": data.columns.tolist(),
        "preview": data.head(10).astype(object)
            .where(pd.notna(data.head(10)), None)
            .to_dict(orient="records")
    }