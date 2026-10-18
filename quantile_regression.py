"""
======================================================================
Median Quantile Regression Analysis
======================================================================

Author: Binyam Heyi

Purpose:
--------
This script runs median quantile regression for models predicting
Well-Being.

Quantile regression estimates the relationship between predictors and
the median of the outcome rather than only estimating the conditional
mean. This makes it useful for examining effects that may differ across
the distribution of Well-Being scores.

Models:
-------
1. Job Demands -> Well-Being
2. Job Demands + Job Resources -> Well-Being

The script prints median quantile regression results, pseudo R-squared,
and a coefficient table containing B, standard error, t-value, p-value,
and 95% confidence intervals.

How to Run:
-----------
1. Open Command Prompt or PowerShell.

2. Run the script by providing the complete path to the CSV file:

    python "C:\\Users\\266510\\Desktop\\DSRT930\\Living\\qauntile_regression.py" "C:\\Users\\266510\\Desktop\\DSRT930\\Living\\Q6_Q29_with_Constructs_Updated.csv"

3. Required packages can be installed using:

    pip install pandas statsmodels

Note:
-----
A CSV file path must be supplied as a command-line argument.
The CSV file must contain Well_Being, Job_Demands, and Job_Resources
columns.

======================================================================
"""

import sys
from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf

def run_quantile_regression(df, formula, label):
    """
    Runs median quantile regression and prints the model results.
    """
    print(f"\n{'='*70}\n{label}\n{'='*70}")

    # --- Median quantile regression (q=0.5 = the median) ---
    qr_model = smf.quantreg(formula, data=df).fit(q=0.5)
    print("\n-- Quantile Regression (median, q=0.5) Results --")
    print(qr_model.summary())
    print("Pseudo R-squared:", qr_model.prsquared)

    # --- Extract just B, SE, t, p, 95% CI for reporting ---
    ci = qr_model.conf_int()
    print("\n-- Quantile Regression Coefficient Table --")
    for name in qr_model.params.index:
        b = qr_model.params[name]
        se = qr_model.bse[name]
        t = qr_model.tvalues[name]
        p = qr_model.pvalues[name]
        lower, upper = ci.loc[name]
        print(f"{name:<15} B={b:.4f}  SE={se:.4f}  t={t:.2f}  p={p:.4g}  95% CI=[{lower:.3f}, {upper:.3f}]")

def main():
    if len(sys.argv) != 2:
        print("Error: No CSV file path was provided.")
        print()
        print("Usage:")
        print(
            r'  python quantile_regression.py "path\to\your_data.csv"'
        )
        sys.exit(1)

    data_path = Path(sys.argv[1])
    if not data_path.is_file():
        print(f"Error: CSV file not found at:\n{data_path}")
        print("\nPlease verify that the file path is correct.")
        sys.exit(1)

    df = pd.read_csv(data_path)

    # Run the two median quantile regression models.
    run_quantile_regression(df, 'Well_Being ~ Job_Demands', 'Job Demands alone -> Well-Being')
    run_quantile_regression(df, 'Well_Being ~ Job_Demands + Job_Resources', 'Combined (RQ3) -> Well-Being')


if __name__ == '__main__':
    main()