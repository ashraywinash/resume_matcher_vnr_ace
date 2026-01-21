import os
import faiss
import numpy as np
import pickle
from embeddings import get_embedding
from utils import extract_text_from_pdf, chunk_text
from config import EMBEDDING_DIM, FAISS_PATH, CHUNK_SIZE

os.makedirs(FAISS_PATH, exist_ok=True)

index = faiss.IndexFlatIP(EMBEDDING_DIM)
metadata = []

resume_folder = "resumes/"

for resume_file in os.listdir(resume_folder):
    if not resume_file.endswith(".pdf"):
        continue

    resume_id = resume_file
    text = extract_text_from_pdf(os.path.join(resume_folder, resume_file))
    chunks = chunk_text(text, CHUNK_SIZE)

    for chunk_id, chunk in enumerate(chunks):
        embedding = np.array(get_embedding(chunk)).astype("float32")
        faiss.normalize_L2(embedding.reshape(1, -1))

        index.add(embedding.reshape(1, -1))

        metadata.append({
            "resume_id": resume_id,
            "chunk_id": chunk_id,
            "text": chunk
        })

    print(f"✅ Ingested {resume_id}")

faiss.write_index(index, f"{FAISS_PATH}/index.faiss")
with open(f"{FAISS_PATH}/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)
