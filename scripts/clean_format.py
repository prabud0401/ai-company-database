"""Dedupe and filter data/raw.csv, write output/Company_Database.xlsx."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw.csv"
OUT = ROOT / "output" / "Company_Database.xlsx"
AREAS = ("publishing city", "industrial area 3")


def main():
    df = pd.read_csv(RAW, dtype=str).fillna("")
    df.columns = [c.strip().lower() for c in df.columns]
    df["_key"] = df["name"].str.lower().str.strip() + "|" + df["phone"].str.replace(r"\D", "", regex=True)
    df = df.drop_duplicates("_key").drop(columns="_key")
    df = df[df["area"].str.lower().apply(lambda a: any(x in a for x in AREAS))]
    if "verified" not in df.columns:
        df["verified"] = "N"
    OUT.parent.mkdir(exist_ok=True)
    df.to_excel(OUT, index=False)
    print(f"Wrote {len(df)} rows to {OUT}")


if __name__ == "__main__":
    main()
