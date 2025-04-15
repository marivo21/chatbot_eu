import json
import redis
from langchain_core.documents import Document
from langchain_community.vectorstores import Redis


redis_client = redis.Redis(host="localhost", port=6379, decode_responses=False) # connettersi a redis
embedding_model = SentenceTransformer("all-MiniLM-L6-v2") # modello embedding

# creazione documenti
documents = []
ids = []

for item in dati_europeana:
    doc = Document(
        page_content=f"{item['title']} - {item['description']}",
        metadata={"author": item.get("author", "Unknown"), "date": item.get("date", "Unknown")}
    )
    documents.append(doc)
    ids.append(item["id"])

# cercare documenti simili
query = "Who is Orazio Gentileschi?"
results = vector_store.similarity_search(query, k=2)
