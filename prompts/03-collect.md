# Step 4 – Collect (run once per keyword group and area)

Search public business directories and registries (SEDD licence search, Sharjah Chamber directory, the area's own portal, Yellow Pages, 2GIS, company websites) for companies doing **[keyword]** activities in **[area]** (Sharjah Publishing City Free Zone, or Sharjah Industrial Area 3).

For each company, give:
- name: company name as licensed
- activity_no: matching number(s) from input/Oil Business Activities Masterlist UAE.xlsx (for example `4` or `4;14`)
- owner: owner name, only if publicly listed
- manager: manager name as per licence
- website
- phone: registered telephone number as per licence
- email: company email
- licence_expiry: licence expiry date (YYYY-MM-DD) if shown
- remarks: anything worth noting
- area: Sharjah Publishing City Free Zone or Sharjah Industrial Area 3
- source: URL where the details were found
- verified: Y if you confirmed the details on an official registry, otherwise N

Rules: don't invent anything. Leave a field blank if it's unknown. Use only public business listings.
Output CSV rows with the header
`name,activity_no,owner,manager,website,phone,email,licence_expiry,remarks,area,source,verified`
and append them to data/raw.csv (write the header only if the file is new).
