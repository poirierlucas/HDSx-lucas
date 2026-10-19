"""Reusable pandas helpers for the Assignment 4 parity analysis."""

import pandas as pd


def summarize_bmi_by_income_gender(data: pd.DataFrame) -> pd.DataFrame:
    complete_cases = data.dropna(subset=["BMI", "IncomeGroup", "Gender"])
    return (
        complete_cases.groupby(
            ["IncomeGroup", "Gender"], observed=True, sort=True
        )["BMI"]
        .agg(
            n="count",
            mean_bmi="mean",
            median_bmi="median",
            sd_bmi="std",
        )
        .reset_index()
    )
