import pandas as pd
from converters import convert_dates, float_to_int
import os
import psutil
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process a CSV file")

    parser.add_argument("filepath", help="Path to file")

    args = parser.parse_args()

    filepath = args.filepath
    
    print("Welcome to csv-converter!")

    filesize = os.path.getsize(filepath)
    available_ram = psutil.virtual_memory().available

    if filesize > available_ram * 0.2:
        raise("File is too large")
    else:
    

        df = pd.read_csv(filepath)
        df = df.convert_dtypes()

        df = convert_dates(df)

        df = float_to_int(df)


    return df.to_parquet("./files/account_opened")

if __name__ == "__main__":
    main()



"""
If you want to skip pandas entirely, PyArrow has its own CSV reader (pyarrow.csv.read_csv) and can write Parquet directly via pyarrow.parquet.write_table(). 
This is faster and uses less memory for straightforward conversions.
"""
