from sqlalchemy import create_engine
import pandas as pd

DB_URL = "postgresql://postgres:password@localhost:5432/argo_db"

engine = create_engine(DB_URL)

def insert_dataframe(df, table_name="argo_data"):
    df.to_sql(table_name, engine, if_exists="replace", index=False)

def query_sql(query):
    return pd.read_sql(query, engine)
