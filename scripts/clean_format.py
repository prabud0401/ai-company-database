"""Dedupe and filter data/raw.csv, then fill input/Database Format.xlsx -> output/Company_Database.xlsx."""
import argparse
from copy import copy
from datetime import date
from pathlib import Path

import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw.csv"
TEMPLATE = ROOT / "input" / "Database Format.xlsx"
OUT = ROOT / "output" / "Company_Database.xlsx"

AREAS = {  # sheet title -> (match text, Freezone / Area value)
    "Publishing City FZ": ("publishing city", "Sharjah Publishing City Free Zone"),
    "Industrial Area 3": ("industrial area 3", "Sharjah Industrial Area 3"),
}
# template columns B..J after SN, then extras K..L
COLS = ["name", "activity_no", "owner", "manager", "website", "phone",
        "email", "licence_expiry", "remarks"]
EXTRA = [("SOURCE", "source"), ("VERIFIED (Y/N)", "verified")]
FIRST_ROW = 7


def load():
    df = pd.read_csv(RAW, dtype=str).fillna("")
    df.columns = [c.strip().lower() for c in df.columns]
    for c in COLS + ["area", "source", "verified"]:
        if c not in df.columns:
            df[c] = ""
    df = df.apply(lambda s: s.str.strip())
    df["verified"] = df["verified"].replace("", "N")
    key = df["name"].str.lower() + "|" + df["phone"].str.replace(r"\D", "", regex=True)
    return df[~key.duplicated()]


def fill(ws, rows, area_name, candidate):
    for r in range(FIRST_ROW, ws.max_row + 1):  # clear template sample rows
        for c in range(1, ws.max_column + 1):
            ws.cell(r, c).value = None
    ws["C1"], ws["C2"], ws["C3"], ws["C4"] = candidate, "Sharjah", area_name, date.today().isoformat()
    for i, (title, _) in enumerate(EXTRA):
        col = 11 + i
        ws.cell(6, col, title)._style = copy(ws.cell(6, 10)._style)
        ws.cell(5, col, col)._style = copy(ws.cell(5, 10)._style)
    for n, (_, row) in enumerate(rows.iterrows(), start=1):
        r = FIRST_ROW + n - 1
        values = [n] + [row[c] for c in COLS] + [row[c] for _, c in EXTRA]
        for c, v in enumerate(values, start=1):
            ws.cell(r, c, v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="", help="Candidate name for the header")
    args = ap.parse_args()

    df = load()
    wb = openpyxl.load_workbook(TEMPLATE)
    base = wb.active
    total = 0
    for title, (match, area_name) in AREAS.items():
        rows = df[df["area"].str.lower().str.contains(match, regex=False)]
        ws = wb.copy_worksheet(base)
        ws.title = title
        fill(ws, rows, area_name, args.name)
        total += len(rows)
        print(f"{title}: {len(rows)} rows")
    wb.remove(base)
    OUT.parent.mkdir(exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {total} rows to {OUT}")


if __name__ == "__main__":
    main()
