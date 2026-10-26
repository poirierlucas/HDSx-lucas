**What AI helped with:** Claude Code drafted the
Quarto file, the `ggplot2` code, the audit table, and the caption.


**How it was checked:**

- **Column names:** Every column used (`Cycle`, `BMI`, `Age`, `IncomeGroup`)
  was checked against the CSV header. The `IncomeGroup` levels were checked
  with `table()` before relabelling them with PIR cut-points.
- **Flawed-plot claims:** The audit claims were checked by computing them, not
  by assuming them. The `min_age` column in the reproduced flawed summary shows
  children were included, and the summary table shows the low-income mean was
  the lowest, not the highest, in the flawed version.
- **Scale:** The y-axis (25-32) is wider than the data range (about 27.5-31
  including intervals) and is stated in the subtitle and caption.
- **Wording:** The title, subtitle, caption, and interpretation were checked
  for causal words ("drives", "causes") and population claims ("American
  adults"). Each one says "unweighted" and "descriptive".
- **Rendering:** The file was rendered with `quarto render` in the Codespace to
  confirm it runs from relative paths and regenerates `corrected-plot.png`.
- **Privacy:** The data file was not uploaded to an external AI chat. The AI
  ran code locally in the Codespace and mostly saw aggregate summaries, but it
  did read the CSV header and two sample rows (public-use, de-identified data)
  to check column names.
