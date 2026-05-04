from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []
index = faiss.IndexFlatL2(384)

def add_documents(docs):
    global documents
    embeddings = model.encode(docs)
    index.add(np.array(embeddings))
    documents.extend(docs)

def search(query, k=3):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)
    return [documents[i] for i in I[0]]
