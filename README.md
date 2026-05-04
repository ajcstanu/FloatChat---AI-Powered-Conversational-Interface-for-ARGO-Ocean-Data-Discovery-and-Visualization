# 🌊 FloatChat

### AI-Powered Conversational Interface for ARGO Ocean Data

FloatChat is an end-to-end system that enables users to explore and analyze ARGO oceanographic data using natural language. It combines NetCDF data processing, relational databases, vector search, and LLM-powered Retrieval-Augmented Generation (RAG) to make ocean data accessible to both technical and non-technical users.

---

## 🚀 Features

* 📥 **NetCDF Data Ingestion**

  * Converts ARGO `.nc` files into structured tabular data
  * Stores processed data in PostgreSQL

* 🗄️ **Hybrid Data Storage**

  * Relational DB (PostgreSQL) for structured queries
  * Vector DB (Chroma/FAISS) for semantic search

* 🧠 **RAG-based Query Engine**

  * Converts natural language → SQL queries
  * Retrieves contextual metadata using embeddings
  * Generates intelligent responses using LLMs

* 💬 **Chat Interface**

  * Ask questions like:

    * *"Show salinity profiles near the equator in March 2023"*
    * *"Compare BGC parameters in the Arabian Sea"*

* 📊 **Interactive Dashboard**

  * Geospatial visualization (Mapbox)
  * Tabular results
  * Data exploration UI using Streamlit

---

## 🏗️ Project Structure

```
FloatChat/
│── app.py                      # Streamlit frontend
│── backend/
│   ├── ingestion.py           # NetCDF → PostgreSQL
│   ├── vector_store.py        # Vector DB setup
│   ├── rag_pipeline.py        # LLM + SQL generation
│   ├── db.py                  # Database connection
│   └── utils.py
│
│── data/
│   └── sample.nc              # Sample ARGO file
│
│── requirements.txt
│── README.md
│── .env
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/FloatChat.git
cd FloatChat
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
DB_URL=postgresql://postgres:password@localhost:5432/argo_db
```

---

### 4️⃣ Setup PostgreSQL Database

* Create a database named: `argo_db`
* Ensure PostgreSQL is running

---

### 5️⃣ Run Data Ingestion

```bash
python backend/ingestion.py
```

---

### 6️⃣ Launch Application

```bash
streamlit run app.py
```

---

## 🧪 Example Queries

* Show temperature variation with depth
* Find ARGO floats near latitude 0 and longitude 70
* Compare salinity across different regions
* Retrieve recent BGC observations

---

## 🧠 Tech Stack

| Layer           | Technology        |
| --------------- | ----------------- |
| Frontend        | Streamlit, Plotly |
| Backend         | Python            |
| Data Processing | xarray, pandas    |
| Database        | PostgreSQL        |
| Vector DB       | Chroma / FAISS    |
| AI/LLM          | OpenAI GPT        |
| Visualization   | Mapbox            |

---

## 🔄 Workflow

1. **Ingestion**

   * Load NetCDF → Convert to DataFrame → Store in PostgreSQL

2. **Embedding**

   * Generate metadata → Store in vector database

3. **Query Processing**

   * User query → LLM → SQL generation

4. **Retrieval**

   * Execute SQL → Fetch results

5. **Response**

   * Combine DB + vector context → Display output

---

## ⚠️ Limitations (Current PoC)

* Basic SQL generation (no strict validation)
* No authentication layer
* Limited dataset optimization
* No PostGIS support yet
* MCP protocol not fully integrated

---

## 🔮 Future Enhancements

* ✅ FastAPI backend (production-ready API)
* ✅ PostGIS for geospatial queries
* ✅ LangChain / LlamaIndex integration
* ✅ Multi-agent query planning
* ✅ Docker deployment
* ✅ Support for satellite + buoy data

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---


---
