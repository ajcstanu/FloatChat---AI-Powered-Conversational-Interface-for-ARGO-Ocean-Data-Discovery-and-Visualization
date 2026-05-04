from fastapi import FastAPI
from models import QueryRequest
from db import query_sql
from rag import search

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FloatChat Backend Running"}

def nl_to_sql(query):
    if "salinity" in query.lower():
        return "SELECT * FROM argo_data LIMIT 100"
    elif "temperature" in query.lower():
        return "SELECT * FROM argo_data LIMIT 100"
    else:
        return "SELECT * FROM argo_data LIMIT 50"

@app.post("/chat")
def chat(req: QueryRequest):
    sql = nl_to_sql(req.query)
    data = query_sql(sql)
    context = search(req.query)

    return {
        "sql": sql,
        "rows": data.head(10).to_dict(),
        "context": context
    }
