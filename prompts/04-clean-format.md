# Step 5 – Clean and format

Run `python scripts/clean_format.py --name "Your Name"`.
It loads data/raw.csv, removes duplicates (same name and phone), and drops rows outside the two areas. It then fills a copy of input/Database Format.xlsx: one sheet per area, with the header fields (Candidate Name, Emirate, Freezone / Area, Date) and the 10 columns from row 7. The Source and Verified columns go after REMARKS. The result is saved to output/Company_Database.xlsx.
