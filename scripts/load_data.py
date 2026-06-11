import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {

"fund_master":
"data/raw/01_fund_master.csv",

"nav_history":
"data/processed/clean_nav_history.csv",

"transactions":
"data/processed/clean_investor_transactions.csv",

"performance":
"data/processed/clean_scheme_performance.csv",

"aum":
"data/raw/03_aum_by_fund_house.csv"

}

for table,file in files.items():

    print(
        f"Loading {table}"
    )

    df = pd.read_csv(
        file
    )

    df.to_sql(

        table,

        engine,

        if_exists="replace",

        index=False

    )

    count = pd.read_sql(

        f"SELECT COUNT(*) as cnt FROM {table}",

        engine

    )

    print(

        count

    )

print(

"Database Loading Complete"

)