import pandas as pd
import datetime

def convert_dates(df):
    for col in df.columns:
        if any(hint in col.lower() for hint in ["date", "time", "at", "on"]):
            try:
                df[col] = pd.to_datetime(df[col])
            except (ValueError, TypeError):
                pass
    return df

def float_to_int(df):
    for col in df.select_dtypes("number").columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    return df
