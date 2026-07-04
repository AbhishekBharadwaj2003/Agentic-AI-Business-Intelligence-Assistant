import pandas as pd

class CleaningAgent:

    def clean_data(self, df):

        print("Starting Data Cleaning...")

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Fill missing numeric values
        numeric_cols = df.select_dtypes(include='number').columns

        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())

        # Fill missing text values
        object_cols = df.select_dtypes(include='object').columns

        for col in object_cols:
            df[col] = df[col].fillna("Unknown")

        print("Data Cleaning Completed.")

        return df