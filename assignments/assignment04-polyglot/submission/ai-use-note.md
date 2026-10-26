**What AI helped with:** Claude Code drafted the
Quarto file, the R summary function, the pandas translation in
`translation.ipynb`, `helpers.py`, and the parity table.


**How it was checked:**

- **Same question:** Both versions summarise BMI by `IncomeGroup` and `Gender`
  with the same statistics (count, mean, median, and sample SD). pandas
  `std()` and R `sd()` both use the n - 1 denominator.
- **Same filters and missingness:** Both drop rows missing `BMI`,
  `IncomeGroup`, or `Gender` (`filter(!is.na(...))` in R, `dropna(subset=...)`
  in pandas). Both keep 87,647 of 105,626 rows.
- **Matching results:** The group labels, group sizes, and rounded mean,
  median, and SD were compared in `parity-table.csv`, and every row matches.
  The notebook `assert`s this so a mismatch would stop it.
- **Rendering:** The Quarto file was rendered with `quarto render` and the
  notebook was run from the repository root in the Codespace to confirm both
  work from relative paths.
