import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

print("CSV Files Found:")

print(files)

for file in files:

    if file.endswith(".csv"):

        print("\n"+"="*50)

        print("FILE:", file)

        path = os.path.join(
            folder_path,
            file
        )

        df = pd.read_csv(path)

        print("Shape:")

        print(df.shape)

        print("\nData Types:")

        print(df.dtypes)

        print("\nFirst 5 Rows:")

        print(df.head())

        print("\nMissing Values:")

        print(df.isnull().sum())