# RAG-based Chatbot 👾 

This project is a Retrieval-Augmented Generation (RAG) chatbot that uses the LLaMA 3.2-3B language model and an embedding system based on FAISS, developed by Meta.

## 📌Key Features 

➡️1.Document Retrieval: The chatbot retrieves documents from data sourced via the Europeana API.
➡️2.In-Memory Storage: Utilizes an in-memory database built with Redis for fast and efficient data management.
➡️3.LangChain Integration: Implements LangChain to build the pipeline (via Hugging Face pipeline), manage prompts, and store vectors using Redis Vector Store.



## 📂 Project Structure

📦 repo-name  
├── europeana_data.json   # JSON dataset with data from Europeana  
├── main.py               # Main script to run the chatbot  
├── requirements.txt      # Required libraries  
├── vector_database.py    # Vector database implementation  
└── README.md  



## 🚀 Installation

Follow these steps to set up the project and run the chatbot locally.

1. Clone the Repository
First, clone the repository to your local machine:

```
git clone https://github.com/marivo21/chatbot_eu
cd repo-name
```
2. Install Dependencies
Install all required packages from requirements.txt:

```
pip install -r requirements.txt
```

3. Set up Redis
Install langchain-redis and running the Redis docker container.

```
docker run -p 6379:6379 redis/redis-stack-server:latest
```
