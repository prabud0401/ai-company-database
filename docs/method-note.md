# Method note

## Goal
Build a company database, in the given format, of companies doing one or more activities from the oil business activities masterlist in two areas of Sharjah: Sharjah Publishing City Free Zone and Sharjah Industrial Area 3.

## AI tool and approach
- **AI used:** Google Gemini (web search enabled).
- I searched one activity group at a time for each area, using a fixed prompt (see `prompts/03-collect.md`). The prompt asks Gemini to:
  - search public directories and registries,
  - return only companies located in the target area,
  - map each company to an activity number from the masterlist,
  - give the source link for every row,
  - leave a field blank rather than invent it.
- Keyword groups run for Industrial Area 3: fuel/diesel (1), lubricants (2), petroleum products (3), storage (4).

## Sources tried
- **SEDD licence search** (sedd.ae, Sharjah's official licence lookup): returned no results for the names tested, so no licence-verified data could be pulled from it.
- **Public directories that Gemini surfaced:** 2GIS, Yellow Pages UAE, Wikimapia, Yandex Maps, oil and gas directories, dubiki, company websites, and a UAE company details PDF.

## Filtering and checks (done by me)
- Dropped rows with no phone number.
- Dropped companies outside the oil masterlist (for example, an industrial gases supplier).
- Dropped candidates I couldn't confirm were in the target area. All 4 candidates from the "petroleum products" search were rejected; the first run returned nothing.
- Corrected activity numbers where Gemini had spread codes to cover every activity, so each company gets the code that matches its actual business.
- Removed duplicates by company name plus phone.
- `scripts/clean_format.py` writes the cleaned data into the provided `Database Format.xlsx` template, one sheet per area. I added SOURCE and VERIFIED columns.

## Result
- **Industrial Area 3:** 7 companies.
- **Publishing City Free Zone:** 0 companies. The search stopped before this area was covered because Gemini's usage limit was reached.

## Limitations
- **Not licence-verified:** the VERIFIED column is N for every row, because the SEDD lookup returned nothing. Phone numbers come from public listings, not from the licence.
- **Manager names:** found for only 2 companies, both from non-registry sources, and noted in REMARKS.
- **Next steps with more time or access:** a paid registry (NER, the Sharjah Chamber member directory), the SPCFZ company directory for Publishing City, and a direct licence check with SEDD.
