# AI Use Note

**What AI helped with:** Claude Code  drafted the revised chart caption and rewrote the page text for the board and the submission notes.

**How it was checked:**

- **No analytic change:** `dashboard.qmd` was diffed against `dashboard-starter.qmd`. The filter and summary code is unchanged. The edits are the page text, the removed student-instruction sections, hidden code chunks, table column names, and the caption. The default render's table (n and mean BMI per cycle) matches the starter's output.
- **Caption accuracy:** each claim in the caption was checked against the code and data. The cohort is `Age >= 20, Age <= 80`. Rows missing `BMI` or `Cycle` are dropped by the filter, and rows missing income group drop out because they do not match `selected_income`. The `IncomeGroup` labels in the CSV are "Low Income (<1.3)", "Middle Income", and "High Income (>3.5)". The data have no 2019-2020 cycle.
- **Wording:** the caption, Audience Question, and notes were checked for causal words ("causes", "drives", "effect") and population claims ("U.S. adults", "prevalence"). The caption and limitation say "unweighted" and "descriptive" and say the chart does not show that income causes BMI.
- **Small cells:** the n per cycle for all three income groups was counted (minimum 1,089), so there is no small-cell issue.
- **Test:** the two renders (`"Middle Income"` and the default) were viewed as images to confirm the title, line, and caption.
- **Privacy:** the data file was not uploaded to an external AI chat. The AI ran R locally in the Codespace and saw only aggregate counts and means and the rendered chart, not individual records.
