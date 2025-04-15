from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama 
from streamlit_tags import st_tags

# set up ZERO-SHOT
user_input = "How did Caravaggio create such dramatic lighting?"

candidate_labels = st_tags(
            value=["biography", "technique", "art"],
            maxtags=3,
            suggestions=["biography", "technique", "art"],
            label="",
        )


classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
classification = classifier(user_input, candidate_labels)
top_label = classification['labels'][0]
print(f"Classified as: {top_label}\n")

# documents index
documents = [
    {"text": "Caravaggio was born in 1571", "category": "biography"},
    {"text": "Caravaggio used dramatic lighting in his artworks.", "category": "technique"},
    {"text": "The painter of Narcissus is Caravaggio.", "category": "art"}
]

# set up embedding
emb_model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [doc['text'] for doc in documents]
embeddings = emb_model.encode(texts)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# find similar documents
query_embedding = emb_model.encode([user_input])
D, I = index.search(query_embedding, k=3)
print("Top 3 matched documents:")
for i in I[0]:
    print("-", texts[i])

# set up PROMPT + LLM 

llm_model = Ollama(model="llama3", base_url="http://localhost:11434") 

template = """Question: {question}

Answer: The following information can help answer your question."""
prompt = PromptTemplate.from_template(template)

# Invoke LLM with prompt
chain = prompt | llm_model
response = chain.invoke({"question": user_input})
print("\nLLM Response:\n", response)
