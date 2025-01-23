import torch 
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate # prompt 
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
    temperature = 0.7,
    max_new_tokens = 30,
    temperature = 0.6 # cercare che livello di temperature adatto 
    )
llm_model_name = HuggingFacePipeline(pipeline=pipel)

# set up prompt - NON COMPLETO
template = """Question: {question}

Answer: The follow informations can give a reply to your answer."""
prompt = PromptTemplate.from_template(template)
chain = prompt | llm_model_name
question = "..."
print(chain.invoke({"question": question}))
