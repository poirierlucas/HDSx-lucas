## Audit trail

1. **Loading the data**
   - **AI prompt:** "Load the NHANES equity CSV with a relative path; Marital is parsed as logical and gives warnings."
   - **Verified:** Marital and MaritalClean are text columns that are empty in the first rows, so readr guesses logical. Forcing `col_character()` removes the parse warnings, and `nrow(nhanes)` matches the 105626 rows in the file.
2. **Cohort**
   - **AI prompt:** "Filter to ages 20 to 80 inclusive and build a cohort flow table of step and n."
   - **Verified:** Checked the filter uses `>=` and `<=` instead of `>` and `<`, so age 20 and age 80 are kept. Each n was rechecked with `sum()` on the same conditions, and the counts add up from step to step.
3. **Missingness**
   - **AI prompt:** "Count missing values and percent missing for the key variables in the cohort."
   - **Verified:** The variable names match `names(nhanes)`. The counts were compared with `colSums(is.na(cohort))` and match, and the percent uses the cohort size as the denominator, not the full CSV.
4. **Table 1**
   - **AI prompt:** "Write a mean_sd() helper and a Table 1 by IncomeGroup with N, BMI mean and SD, and age mean and SD, ordered low to high income, then export it as table1.csv."
   - **Verified:** `mean_sd()` uses `sd()`, not `var()`. The low-income row was checked against plain `mean()` and `sd()` calls on that subset, and the N column sums to the Table 1 count in the cohort flow table. `table1.csv` was reread after rendering and matches the HTML table.

**What AI helped with:** Claude Code drafted `eda-note.qmd` with the cohort flow, missingness table, Table 1, and methods note, helped find and word the planted issues in `audit-note.md`, and drafted the provenance note.

**What I changed:**

- Dropped rows only for missing `BMI` or `IncomeGroup` instead of using `na.omit()`, after the check showed `na.omit()` removes the whole 2021-2023 cycle.
- Ordered and relabelled income groups Low → Middle → High with PIR cut-points instead of the default alphabetical order.
- Added a `stopifnot()` so the render fails if Table 1's N does not add up to the analysis cohort.

**How I verified the result:**

- **Cohort filter:** `Age >= 20, Age <= 80` keeps 57137 rows. The starter's `Age > 20, Age < 80` drops 993 people age 20 and 2716 age 80. NHANES top-codes age at 85 for 1999-2006 and at 80 from 2007 on, which the cohort note states.
- **Missingness:** Counted in the cohort before any rows were dropped. Missing BMI for 1009 plus missing income group for 5395, minus overlap, gives the 6286 excluded.
- **Statistics:** Low-income BMI is 29.4 with SD 7.5 using plain `mean()` and `sd()`, matching Table 1. The starter's `var()` gives 55.6 instead. The BMI means and SDs match the course worked example. Ages differ by at most 0.2 years because the worked example did not drop rows missing BMI.
- **Labels and export:** `table1.csv` is written by `write_csv()` on render and matches the HTML table.
- **Interpretation:** The methods note was checked for causal words such as "determines", "causes", and "effect of", and for population claims. It says the summaries are descriptive and unweighted and that no tests were run.
- **Rendering:** Rendered with `quarto render` from the repository root in the Codespace to confirm it runs from relative paths.
- **Privacy:** The data file was not uploaded to an external AI chat. The AI ran code locally in the Codespace and mostly saw aggregate summaries, but it did read the CSV header and two sample rows of the public-use, de-identified data to check column names.
