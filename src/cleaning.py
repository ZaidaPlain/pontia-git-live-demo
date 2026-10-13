"""Basic cleaning of the CSV files in data/raw/ -> data/processed/."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the sales DataFrame."""
    df = df.copy()

    # Text: strip extra whitespace and lowercase
    for col in ("product", "category"):
        df[col] = df[col].str.strip().str.lower()

    # Types
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["units"] = pd.to_numeric(df["units"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # Invalid rows: duplicates, nulls in required fields, units <= 0
    df = df.drop_duplicates()
    df = df.dropna(subset=["date", "units", "unit_price"])
    df = df[df["units"] > 0]

    df["units"] = df["units"].astype(int)
    df["amount"] = (df["units"] * df["unit_price"]).round(2)
    return df.reset_index(drop=True)


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    for path in sorted(RAW_DIR.glob("*.csv")):
        raw = pd.read_csv(path)
        out = clean(raw)
        target = PROCESSED_DIR / f"{path.stem}_clean.csv"
        out.to_csv(target, index=False)
        print(f"{path.name}: {len(raw)} rows -> {len(out)} rows ({target.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
