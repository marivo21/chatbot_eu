from langchain_community.vectorstores import Redis
from redis import Redis
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


vector_store = RedisVectorStore(
    index_name="Eu-demo",
    embedding=SentenceTransformer("all-MiniLM-L6-v2"),
    redis_url="redis://localhost:6379",
)

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=False)
