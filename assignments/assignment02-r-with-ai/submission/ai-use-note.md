**What AI helped with:** Claude Code drafted the
Quarto file, the `dplyr` summary, the `mean_sd()` function, and the step that
saves the output table.


**How it was checked:**

- **Column names:** Every column used (`Age`, `BMI`, `IncomeGroup`) was
  checked against the `names(nhanes)` and `glimpse(nhanes)` output in the
  Inspect section.
- **Missing values:** Missingness was checked with `colSums(is.na(nhanes))`
  before summarising. Rows missing BMI or income group are dropped with
  `filter(!is.na(...))`, and `mean_sd()` uses `na.rm = TRUE` while reporting
  the non-missing `n`, so excluded values are visible instead of silently
  removed.
- **Function output:** `mean_sd(nhanes$BMI)` was checked against plain
  `mean()` and `sd()` calls on the same column, and the results match.
- **Saved output:** `output/summary_table.csv` was recomputed from the code
  and matches the saved file exactly.
- **Wording:** The summary is descriptive and unweighted (mean BMI, SD, and
  percent with BMI ≥ 30 by income group). It makes no causal or national
  population claims.
- **Rendering:** The file was rendered with `quarto render` in the Codespace to
  confirm it runs from the relative data path.
