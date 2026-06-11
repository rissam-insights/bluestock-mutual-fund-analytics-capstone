import pandas as pd

# Load fund master file

df = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# Show columns

print("\nColumns:")

print(df.columns)

# Fund Houses

print("\nUnique Fund Houses:")

if "fund_house" in df.columns:

    print(
        df["fund_house"].unique()
    )

# Categories

print("\nUnique Categories:")

if "category" in df.columns:

    print(
        df["category"].unique()
    )

# Sub Categories

print("\nUnique Sub Categories:")

if "sub_category" in df.columns:

    print(
        df["sub_category"].unique()
    )

# Risk Categories

print("\nUnique Risk Categories:")

if "risk_category" in df.columns:

    print(
        df["risk_category"].unique()
    )