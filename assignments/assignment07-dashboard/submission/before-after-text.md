# Before and After Text

**Element changed:** the caption of the mean BMI line chart (`dashboard-plot` chunk, `caption =` argument in `labs()`).

- **Original:** "Descriptive, unweighted classroom summary. Missing BMI, income group, cycle, and out-of-cohort ages are excluded."
- **Revised:** "Each point is the average BMI of adults age 20-80 in this income group, from the classroom NHANES file. Income group uses the family income-to-poverty ratio: low is under 1.3, high is over 3.5. People missing BMI or income group are left out. This file has no 2019-2020 cycle. Unweighted and descriptive: not a U.S. population estimate, and it does not show that income causes BMI."
- **Why it helps:** the board needs to read the chart without the code. The revised caption says what each point means, explains the "<1.3" in the chart title, explains the jump from 2017-2018 to 2021-2023, and replaces "unweighted" on its own with what that means for interpretation.
- **No analytic logic changed:** the data file, cohort filter (`Age >= 20, Age <= 80`), exclusions, `mean()` summary, grouping, and default `selected_income` are the same as the starter. The table values match the starter render exactly. The other edits are also text or display only. I removed the student instructions left over from the starter (Where this fits, Goal, Testing, Privacy-Safe Publishing, Where this goes next) and rewrote the remaining sections for the board. I also hid the code chunks, gave the table readable column names, and left-aligned the caption.
