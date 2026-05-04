import xarray as xr
import pandas as pd
from db import insert_dataframe

def process_netcdf(file_path):
    ds = xr.open_dataset(file_path)
    df = ds.to_dataframe().reset_index()
    df = df[['LATITUDE', 'LONGITUDE', 'TIME', 'TEMP', 'PSAL']].dropna()
    insert_dataframe(df)
    return df

if __name__ == "__main__":
    process_netcdf("../data/sample.nc")
