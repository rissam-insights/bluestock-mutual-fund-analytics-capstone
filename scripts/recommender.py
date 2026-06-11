import pandas as pd

# Load data
fund_master = pd.read_csv("data/processed/01_fund_master_clean.csv")
sharpe_df = pd.read_csv("data/processed/sharpe_ratio_report.csv")

# Merge
recommender_df = fund_master.merge(
    sharpe_df[['amfi_code', 'Sharpe_Ratio']],
    on='amfi_code',
    how='left'
)

# User input
risk_input = input("Enter Risk Appetite (Low/Moderate/High): ")

# Recommendations
recommendations = (
    recommender_df[
        recommender_df['risk_category']
        .str.contains(risk_input, case=False, na=False)
    ]
    .sort_values('Sharpe_Ratio', ascending=False)
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(
    recommendations[
        ['scheme_name', 'risk_category', 'Sharpe_Ratio']
    ]
)