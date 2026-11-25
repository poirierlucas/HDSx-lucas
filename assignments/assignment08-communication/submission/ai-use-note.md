# AI Use Note

**What AI helped with:** Claude Code (running locally in the Codespace) drafted the slide wording in `slides.qmd`, the plain-language summary, the source note, and this note. It also added the three-group comparison table to the takeaway slide.

**How it was checked:**

- **Numbers:** every number in the deck and summary was checked against a fresh R summary of `nhanes_equity_v6.csv` using the Assignment 7 cohort (age 20-80, non-missing BMI, cycle, and income group). Low income goes from 28.8 to 30.4, middle from 29.0 to 30.3, and high from 27.9 to 29.2. The smallest cell is 1,089 adults. The low-income values match the A7 dashboard and testing log.
- **No new findings:** the deck uses the A7 figure unchanged. The only new evidence is the first-vs-last table, which uses the same filter and unweighted mean as `dashboard.qmd`. It was added so the takeaway does not suggest that the rise is only in lower-income adults.
- **Wording:** the slides and summary were checked for causal words ("causes", "drives", "because of") and population claims ("U.S. adults"). Each one says the results are unweighted and descriptive and do not show cause. A note about the y-axis not starting at 0 was added under the figure so the slope is not overread.
- **Source:** the citation is the course's existing `cdc-nhanes` entry in `references.bib`. No new sources were added.
- **Privacy:** no data were uploaded to an external AI chat. The assistant saw only aggregate counts and means.
