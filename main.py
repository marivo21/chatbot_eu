import torch 
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate # prompt 
import numpy as np # embeddings
import faiss
from sentence_transformers import SentenceTransformer
# da qui non sono stati ancora costruiti nel codice
from langchain_text_splitters import RecursiveCharacterTextSplitter #chunk



# set up llm
llm_model_name = "meta-llama/Llama-3.2-3b"  # configurazione modello llama 
tokenizer = AutoTokenizer.from_pretrained(llm_model_name) # tokenizer
model = AutoModelForCausalLM.from_pretrained(llm_model_name, device_map="auto") # distribuire il modello su GPU o CPU in base alla disponibilità

#set up pipeline
pipel = pipeline(
    "text generation",
    tokenizer = tokenizer,
    model = llm_model_name,
    max_new_tokens = 30,
    temperature = 0.6  
    )
llm_model_name = HuggingFacePipeline(pipeline=pipel)

# set up prompt 
template = """Question: {question}

Answer: The follow informations can give a reply to your answer."""
prompt = PromptTemplate.from_template(template)
chain = prompt | llm_model_name
question = """When does baroque begin? 
Who's the painter of the paint Narcissus?"""
print(chain.invoke({"question": question}))

# set up FAISS - NON COMPLETO
emb_model = SentenceTransformer("all-MiniLM-L6-v2") # embedding con 384 dimensioni
embeddings = emb_model.encode(texts) # restituisce una matrice NumPy

dimension = embeddings.shape[1] # la dimensione del vettore di embedding
index = faiss.IndexFlatL2(dimension) # distanza tra i vettori 
index.add(embeddings)
