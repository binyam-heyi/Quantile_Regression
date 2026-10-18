# Median Quantile Regression

This repository contains a Python script that estimates median quantile
regression models for Well-Being. Unlike ordinary least squares regression,
which models the conditional mean, quantile regression estimates effects at a
selected point of the outcome distribution. This script fits the median
(quantile 0.5) to examine how job demands and job resources relate to
Well-Being.

## Models

1. `Well_Being ~ Job_Demands`
2. `Well_Being ~ Job_Demands + Job_Resources`

For each model, the script prints the statsmodels summary, pseudo R-squared,
and a coefficient table with estimates, standard errors, t-values, p-values,
and 95% confidence intervals.

## Requirements

- Python 3
- pandas
- statsmodels

Install the required packages:

```bash
python -m pip install pandas statsmodels
```

## How to run

Pass the path to a CSV file as the script's only argument. The CSV must include
these columns: `Well_Being`, `Job_Demands`, and `Job_Resources`.

From the repository folder:

```powershell
python .\quantile_regression.py "C:\path\to\your_data.csv"
```

The script reads the CSV file at the provided path. No dataset is included in
this repository.
