# Table 1 Audit Note

All issues come from `planted-error-starter.qmd` and are corrected in `eda-note.qmd`. Counts were computed from the CSV, not assumed.

## Cohort

The intended cohort is participants age 20-80 inclusive. It is implemented in `eda-note.qmd` as `filter(Age >= 20, Age <= 80)`, giving n = 57137, followed by dropping only rows missing `BMI` or `IncomeGroup`, giving n = 50851 for Table 1.

## Missingness

`Cycle`, `Age`, `Gender`, `Race`, `BMI`, `PIR`, and `IncomeGroup` were checked for missingness within the age 20-80 cohort before any summaries. BMI is missing for 1009 rows, 1.8%, and `PIR`/`IncomeGroup` for 5395 rows, 9.4%. The others have no missing values.

## Planted Issues

**1. Correctness: Age filter excludes ages 20 and 80**
- `filter(Age > 20, Age < 80)` uses strict inequalities, but the text says age 20-80 inclusive
- Silently drops 993 people age 20 and 2716 age 80, so the table does not describe the cohort the text claims
- Fix: `filter(Age >= 20, Age <= 80)`, with the decision stated before results and a cohort flow table showing each n

**2. Reproducibility: Hard-coded personal file path**
- `candidate_paths` starts with `C:/Users/analyst/Documents/...` and quietly uses whichever path happens to exist
- The absolute path only works on one person's computer, and the fallback list hides which file was actually read
- Fix: read one relative path from the repository root, `examples/nhanes-equity/data/nhanes_equity_v6.csv`, and let it fail loudly if the file is missing

**3. Interpretation: "Statistically significant ... income determines BMI"**
- No test was run, so "statistically significant" is unsupported
- Descriptive, unweighted means cannot show that income causes BMI, since age, sex, and other factors differ across groups
- Fix: describe the sample differences only, and state that the summaries are descriptive, unweighted, and non-causal, with no tests run

**4. Stewardship: False provenance comment**
- The comment says "Data downloaded fresh from the NHANES website last week"
- The file is actually a cached, prepared classroom snapshot, `nhanes_equity_v6`, derived from CDC/NCHS public-use files, so the data can't be traced or cited correctly
- Fix: state the real source, version, and classroom-use boundary in the methods note and `provenance-stewardship-note.md`

**5. Correctness: Variance reported as SD**
- Table 1 uses `var(BMI)` and `var(Age)` in columns labelled "mean (SD)"
- Variance is SD squared, so the spread is badly overstated, with low-income BMI showing 55.6 instead of 7.5
- Fix: use `sd()` in a `mean_sd()` helper and check one row against plain `mean()` and `sd()` calls


