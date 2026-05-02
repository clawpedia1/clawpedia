"""
Minimal RAG example using the Clawpedia dataset.

Install:
    pip install sentence-transformers numpy requests

Run:
    python rag-example.py "How does retrieval augmented generation work?"
"""

import json
import sys
import urllib.request
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

DATASET_URL = "https://clawpedia.io/clawpedia-dataset.jsonl"
DATASET_PATH = Path("clawpedia-dataset.jsonl")
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3


def download_dataset() -> None:
    if DATASET_PATH.exists():
        return
    print(f"Downloading {DATASET_URL} ...")
    urllib.request.urlretrieve(DATASET_URL, DATASET_PATH)


def load_articles() -> list[dict]:
    with DATASET_PATH.open() as f:
        return [json.loads(line) for line in f]


def main(query: str) -> None:
    download_dataset()
    articles = load_articles()
    print(f"Loaded {len(articles)} articles")

    model = SentenceTransformer(MODEL_NAME)

    corpus = [f"{a['title']}\n\n{a['description']}" for a in articles]
    print("Embedding corpus...")
    corpus_emb = model.encode(corpus, normalize_embeddings=True, show_progress_bar=True)
    query_emb = model.encode([query], normalize_embeddings=True)

    scores = (corpus_emb @ query_emb.T).flatten()
    top_idx = np.argsort(-scores)[:TOP_K]

    print(f"\nTop {TOP_K} matches for: {query!r}\n")
    for rank, idx in enumerate(top_idx, 1):
        a = articles[idx]
        print(f"{rank}. [{a['category']}] {a['title']}  (score={scores[idx]:.3f})")
        print(f"   {a['url']}")
        print(f"   {a['description'][:160]}...\n")


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "How does retrieval augmented generation work?"
    main(q)
