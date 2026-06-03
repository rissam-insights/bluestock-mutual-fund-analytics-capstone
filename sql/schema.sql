-- ==========================================
-- DIMENSION TABLES 
-- ==========================================

-- 1. Fund Dimension
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);

-- 2. Date Dimension
CREATE TABLE dim_date (
    date_id TEXT PRIMARY KEY, -- Stores dates as 'YYYY-MM-DD'
    year INTEGER,
    month INTEGER,
    day INTEGER,
    is_weekend BOOLEAN
);

-- ==========================================
-- FACT TABLES (Data & Metric Tables)
-- ==========================================

-- 3. NAV History Fact Table
CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_id TEXT,
    nav REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

-- 4. Investor Transactions Fact Table
CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (transaction_date) REFERENCES dim_date(date_id)
);

-- 5. Scheme Performance Fact Table
CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    expense_ratio_pct REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 6. AUM Fact Table
CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    aum_crores REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);