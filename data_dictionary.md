# Data Dictionary

## fund_master

| Column       | Data Type | Description             |
| ------------ | --------- | ----------------------- |
| amfi_code    | INTEGER   | Unique AMFI scheme code |
| fund_house   | TEXT      | Mutual fund company     |
| scheme_name  | TEXT      | Fund scheme name        |
| category     | TEXT      | Fund category           |
| sub_category | TEXT      | Fund sub category       |

---

## nav_history

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | INTEGER   | Scheme code     |
| date      | DATE      | NAV date        |
| nav       | FLOAT     | Net asset value |

---

## investor_transactions

| Column           | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| investor_id      | INTEGER   | Investor identifier        |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr       | FLOAT     | Transaction amount         |
| kyc_status       | TEXT      | KYC verification status    |

---

## scheme_performance

| Column            | Data Type | Description       |
| ----------------- | --------- | ----------------- |
| return_1yr_pct    | FLOAT     | One year return   |
| return_3yr_pct    | FLOAT     | Three year return |
| return_5yr_pct    | FLOAT     | Five year return  |
| expense_ratio_pct | FLOAT     | Expense ratio     |

---

Source:

Raw CSV files from internship dataset.
