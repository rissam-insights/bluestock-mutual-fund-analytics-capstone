import pandas as pd

# Load files

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

print("Fund Master Columns:")

print(
    fund_master.columns
)

print("\nNAV History Columns:")

print(
    nav_history.columns
)

# Extract AMFI codes

fund_codes = set(
    fund_master["amfi_code"]
)

nav_codes = set(
    nav_history["amfi_code"]
)

# Compare codes

missing_codes = fund_codes - nav_codes

print("\nTotal Fund Codes:")

print(
    len(fund_codes)
)

print("\nTotal NAV Codes:")

print(
    len(nav_codes)
)

print("\nMissing Codes Count:")

print(
    len(missing_codes)
)

print("\nSample Missing Codes:")

print(
    list(missing_codes)[:10]
)