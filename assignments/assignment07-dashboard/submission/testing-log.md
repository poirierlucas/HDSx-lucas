# Testing Log

- **Date tested:** 2026-11-23
- **Command:** `quarto render assignments/assignment07-dashboard/submission/dashboard.qmd`, run from the repository root in the Codespace. Output: `assignments/assignment07-dashboard/submission/dashboard.html`.
- **Values tried:**
  1. `selected_income <- "Middle Income"`: rendered with no errors or warnings. The "Income group shown" line and chart title read "Middle Income", the table and line changed (mean BMI 29.0 in 1999-2000, 30.3 in 2021-2023), and the caption was unchanged.
  2. `selected_income <- "Low Income (<1.3)"` (default, submitted): rendered with no errors or warnings. The "Income group shown" line and chart title read "Low Income (<1.3)", mean BMI went from 28.8 in 1999-2000 to 30.4 in 2021-2023, and n per cycle ranged from 1,089 to 1,817.
- **Result:** pass. The title, table, and plot updated with the control. The caption still names the dataset, exclusions, and limitation. `dashboard-preview.png` is the chart taken from the final default render.
