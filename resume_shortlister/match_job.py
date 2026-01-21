import faiss
import numpy as np
import pickle
from collections import defaultdict
from embeddings import get_embedding
from config import FAISS_PATH

index = faiss.read_index(f"{FAISS_PATH}/index.faiss")

with open(f"{FAISS_PATH}/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

def match_job(job_description, top_k=5):
    query_embedding = np.array(get_embedding(job_description)).astype("float32")
    faiss.normalize_L2(query_embedding.reshape(1, -1))

    scores, indices = index.search(query_embedding.reshape(1, -1), 20)

    resume_hits = defaultdict(list)

    for idx, score in zip(indices[0], scores[0]):
        hit = metadata[idx]
        hit["score"] = float(score)
        resume_hits[hit["resume_id"]].append(hit)

    ranked = sorted(
        resume_hits.items(),
        key=lambda x: max(chunk["score"] for chunk in x[1]),
        reverse=True
    )

    return ranked[:top_k]
