# FloatChat - AI ARGO Data Chatbot

## Setup

### Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

### Frontend
cd frontend
streamlit run app.py

### Ingest Data
python ingest.py
