# Plan (≈3–4 hours)

1. **Set up the AI CLI** – install the Antigravity CLI (`agy`), sign in with Google, and run it in the repo folder. Put the input files in `input/`.
2. **Understand the input files** – read the format and activities masterlist; group activities into 5–8 search keywords. Prompt: `prompts/01-understand-files.md`.
3. **Build the source list** – save to `docs/sources.md`. Prompt: `prompts/02-sources.md`.
4. **Collect companies** – per keyword and area, append rows to `data/raw.csv`. Spot-check 1 in 5 rows manually. Prompt: `prompts/03-collect.md`.
5. **Clean and format** – dedupe, filter to the 2 areas, map to the required format, add `Source` and `Verified (Y/N)` columns → `output/Company_Database.xlsx`. Prompt: `prompts/04-clean-format.md` or `scripts/clean_format.py`.
6. **Fill managers and licence phones** – use the SEDD / SPC licence lookups. If none found, write "Not public" – never guess.
7. **Write the method note** – `docs/method-note.md`: tools, sources, counts, verification.
8. **Review, then submit** – check against the required format before sending.

Aim for 30–50 well-sourced rows rather than hundreds of unverified ones.
