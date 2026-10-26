All three issues come from the flawed starter plot (`flawed-plot-code.R`) and are corrected in `corrected-plot.png`.

**1. No age filter (Correctness)**
- Subtitle says "Adults age 20-80", but children are included
- Children pull the means down, especially in the low-income group
- Fix: filter to `Age >= 20` and label the plot "adults 20+"

**2. Y-axis cut to 24-28 with no note (Design)**
- Makes a difference of about 1 BMI unit look much larger
- Fix: wider 25-32 axis, and the caption states it starts at 25

**3. Causal title: "Low income drives rising obesity" (Interpretation)**
- Data are descriptive and unweighted, so they can't show cause or U.S. population values
- Fix: descriptive title, and a caption that says "descriptive and unweighted"
