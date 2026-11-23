# Dashboard Adaptation Note

## Audience

A community health board briefing group. Its members are not statisticians, and they need to decide whether to ask staff for a follow-up analysis of BMI among lower-income adults.

## Dashboard Question

In this classroom NHANES dataset, has average BMI among low-income adults age 20-80 gone up, gone down, or stayed about the same from the 1999-2000 cycle to the 2021-2023 cycle?

## Control And Visualization

- **Control or interaction:** the `selected_income` value in the `dashboard-control` chunk of `dashboard.qmd`. Valid values are `"Low Income (<1.3)"` (default), `"Middle Income"`, and `"High Income (>3.5)"`. It is changed by editing the line and re-rendering. The code is hidden in the rendered page, which states the group being shown near the top.
- **Visualization affected:** the line chart of mean BMI by NHANES cycle (`dashboard-plot`), plus the "Numbers behind the chart" table it is drawn from.
- **What changes when the control changes:** the "Income group shown" line, the chart title (`Mean BMI for <income group>`), the plotted line, the table (n and mean BMI per cycle), and the numbers quoted in "What this shows" all switch to the selected group. The cohort (adults 20-80) and the caption stay the same.

## Before And After

| Original text | Revised text | Why the revision helps |
|---|---|---|
| Chart caption: "Descriptive, unweighted classroom summary. Missing BMI, income group, cycle, and out-of-cohort ages are excluded." | Chart caption: "Each point is the average BMI of adults age 20-80 in this income group, from the classroom NHANES file. Income group uses the family income-to-poverty ratio: low is under 1.3, high is over 3.5. People missing BMI or income group are left out. This file has no 2019-2020 cycle. Unweighted and descriptive: not a U.S. population estimate, and it does not show that income causes BMI." | Board members see the chart without the code. The new caption says what a point is, explains the "<1.3" in the title, explains the gap between 2017-2018 and 2021-2023, and puts the limitation inside the figure in plain words. |

Full details are in `before-after-text.md`.

## Test Result

`quarto render assignments/assignment07-dashboard/submission/dashboard.qmd` was run from the repository root on 2026-11-23 with `selected_income` set to `"Middle Income"` and then back to `"Low Income (<1.3)"`. Both renders finished with no errors or warnings, and the title, table, and line updated each time. For the low-income default, mean BMI goes from 28.8 in 1999-2000 to 30.4 in 2021-2023. See `testing-log.md`.

## Limitation

These are unweighted, descriptive averages from a classroom copy of NHANES. They do not estimate BMI for U.S. adults and do not show that income causes BMI. This sentence appears in the chart caption and in the dashboard's Limitation section.

## Privacy Check

The preview is the chart only. It shows aggregate means per cycle, and every cycle-by-income cell has n > 1,000 (smallest 1,089), so no row-level data or small cells appear. The caption and interpretation use descriptive, non-causal wording. See `privacy-check.md`.
