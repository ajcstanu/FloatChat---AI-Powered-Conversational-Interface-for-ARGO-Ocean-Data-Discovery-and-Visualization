import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000/chat"

st.title("🌊 FloatChat - ARGO Data Explorer")

query = st.text_input("Ask your question:")

if st.button("Submit"):
    response = requests.post(API_URL, json={"query": query}).json()

    st.subheader("Generated SQL")
    st.code(response["sql"])

    df = pd.DataFrame(response["rows"])

    st.subheader("Data Preview")
    st.write(df)

    if not df.empty:
        fig = px.scatter_mapbox(
            df,
            lat="LATITUDE",
            lon="LONGITUDE",
            color="TEMP",
            zoom=2,
            mapbox_style="open-street-map"
        )
        st.plotly_chart(fig)

    st.subheader("RAG Context")
    st.write(response["context"])
