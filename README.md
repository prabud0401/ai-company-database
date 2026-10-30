# AI-assisted UAE company database (Sharjah)

A recruitment skills task: use AI tools to build a database of oil-related businesses located in **Sharjah Publishing City Free Zone** and **Sharjah Industrial Area 3**, including manager names and registered telephone numbers as per government licence, sourced from public registries and directories.

## Tools
- Antigravity CLI (`agy`) / Claude (AI-assisted search, extraction and cleaning)
- Python, pandas, openpyxl

## Method
1. Set up the Antigravity CLI (`agy`) and sign in with Google
2. Understand the input files; group activities into 5–8 keywords
3. Build the source list
4. Collect companies per keyword and area into `data/raw.csv` (spot-check 1 in 5 rows)
5. Clean, dedupe and map to the required format → `output/Company_Database.xlsx`
6. Fill managers and licence phones from SEDD/SPC lookups ("Not public" if not found)
7. Write the method note
8. Review, then submit

Full details: [docs/plan.md](docs/plan.md)

## Structure
```
docs/       plan.md, sources.md, method-note.md
prompts/    ready-to-use AI prompts (01–04)
scripts/    clean_format.py
input/      task input files (not committed)
data/       raw.csv (collected rows)
output/     final Excel database
```

## Quick start
```bash
pip install -r requirements.txt
python scripts/clean_format.py
```

## Results
TODO
