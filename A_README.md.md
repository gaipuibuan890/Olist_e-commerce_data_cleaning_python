# Olist E-Commerce Data Cleaning
Cleans the 9 raw CSV files from the Olist Brazilian e-commerce dataset, preparing them for import into SQL.

## What it does

## Data Preview Script (`B_Preview.py`)

To get a quick overview of all datasets before diving into cleaning and analysis, 
I wrote a script to inspect the structure of each CSV file without loading full data into memory.


### For each file:

-Reads the CSV, treating blanks and placeholders (NA, null, ?, etc.) as missing
-Parses date columns into proper datetime types
-Lowercases and strips column names
-Reports columns with missing values, fills numeric nulls with 0
-Removes exact duplicate rows
-Removes IQR outliers, but only on columns explicitly configured per file
-Saves the result to cleaned/ with _cleaned added to the filename

## Key decisions
-No blanket outlier removal — numeric columns were inspected before deciding anything, not run through IQR by default.
-price / freight_value — reviewed top and bottom values; all realistic (no negatives, zeros, or impossible magnitudes). Left unmodified. Blind -IQR here would have deleted legitimate high-value orders.
-payment_value — high end (up to 13,664) is legitimate: large orders paid in installments. Found 9 rows at exactly 0 — cross-checked 
 against payment_type: 6 were vouchers (valid, no cash paid), 3 were not_defined (incomplete records, removed). No IQR applied.
-lat/lng — excluded; a coordinate far from the median is a real remote location, not an error.
-review_score — excluded; ordinal (1–5), not continuous, so IQR is meaningless.

​```bash
pip install pandas
python data_cleaning.py
​```
