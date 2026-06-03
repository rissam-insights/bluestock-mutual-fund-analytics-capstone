import pandas as pd

# 1. Load the raw NAV history file (Make sure the name matches your folder!)
nav_df = pd.read_csv('data/raw/02_nav_history.csv')

# 2. Parse dates to datetime (assuming format is DD-MM-YYYY, adjust if your CSV differs)
nav_df['date'] = pd.to_datetime(nav_df['date'], format='%d-%m-%Y', errors='coerce')

# 3. Sort by amfi_code + date
nav_df = nav_df.sort_values(['amfi_code', 'date'])

# 4. Forward-fill missing NAV for holidays/weekends
# We MUST group by amfi_code first so we don't bleed one fund's NAV into another
nav_df['nav'] = nav_df.groupby('amfi_code')['nav'].ffill()

# 5. Remove duplicates
nav_df = nav_df.drop_duplicates(subset=['amfi_code', 'date'])

# 6. Validate NAV > 0
nav_df = nav_df[nav_df['nav'] > 0]

# 7. Save to the processed folder
nav_df.to_csv('data/processed/clean_nav_history.csv', index=False)

# 8. Visual confirmation
print("🎉 Success! clean_nav_history.csv has been created in data/processed/")

# ==========================================
# PART 2: CLEANING INVESTOR TRANSACTIONS
# ==========================================

print("\n🔄 Processing 08_investor_transactions.csv...")

# 1. Load the raw transactions file
txn_df = pd.read_csv('data/raw/08_investor_transactions.csv')

# Clean the column names
txn_df.columns = txn_df.columns.str.strip().str.lower()

# Print verified columns to the terminal
print(f"📋 Verified columns in file: {list(txn_df.columns)}")

# 2. Standardise transaction_type values
txn_df['transaction_type'] = txn_df['transaction_type'].astype(str).str.strip().str.lower()
txn_map = {
    'sip': 'SIP', 
    'lumpsum': 'Lumpsum', 
    'lump sum': 'Lumpsum', 
    'redemption': 'Redemption', 
    'redempt': 'Redemption'
}
txn_df['transaction_type'] = txn_df['transaction_type'].map(txn_map).fillna('Unknown')

# 3. Validate amount_inr > 0 (🔥 Fixed to match your actual column name)
txn_df = txn_df[txn_df['amount_inr'] > 0]

# 4. Fix date formats
txn_df['transaction_date'] = pd.to_datetime(txn_df['transaction_date'], errors='coerce')

# 5. Check KYC status enum values
txn_df['kyc_status'] = txn_df['kyc_status'].astype(str).str.strip().str.capitalize()
valid_kyc = ['Verified', 'Pending', 'Rejected']
txn_df = txn_df[txn_df['kyc_status'].isin(valid_kyc)]

# 6. Save to the processed folder
txn_df.to_csv('data/processed/clean_investor_transactions.csv', index=False)

print("🎉 Success! clean_investor_transactions.csv has been created.")

# ==========================================
# PART 3: CLEANING SCHEME PERFORMANCE
# ==========================================

print("\n🔄 Processing 07_scheme_performance.csv...")

# 1. Load the raw performance file
perf_df = pd.read_csv('data/raw/07_scheme_performance.csv')

# Clean the column names to prevent any capitalization or space issues
perf_df.columns = perf_df.columns.str.strip().str.lower()

# Print verified columns to terminal
print(f"📋 Verified columns in file: {list(perf_df.columns)}")

# 2. Check expense_ratio range (0.1% – 2.5%)
# Using dynamic check based on your earlier script structure
ratio_col = 'expense_ratio_pct' if 'expense_ratio_pct' in perf_df.columns else 'expense_ratio'
perf_df = perf_df[(perf_df[ratio_col] >= 0.1) & (perf_df[ratio_col] <= 2.5)]

# 3. Validate return values are numeric
# This automatically finds any column with "return" in its name and fixes it safely
return_cols = [col for col in perf_df.columns if 'return' in col]
for col in return_cols:
    perf_df[col] = pd.to_numeric(perf_df[col], errors='coerce')

# 4. Save to the processed folder
perf_df.to_csv('data/processed/clean_scheme_performance.csv', index=False)

print("🎉 Success! clean_scheme_performance.csv has been created.")
