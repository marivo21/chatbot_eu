import json
from pathlib import Path
from pprint import pprint
from langchain_community.document_loaders import JSONLoader


file_path = 'dati_europeana.json'  


data = json.loads(Path(file_path).read_text())
pprint(data)

# Funzione per estrarre i metadati
def metadata_func(record: dict, metadata: dict) -> dict:
    language = record.get("language") 

    
    if language and language not in ["en", "it"]:
        return None 

   
    metadata["title"] = record.get("title")
    metadata["creator"] = record.get("creator")
    metadata["timestamp"] = record.get("timestamp")
    metadata["rights"] = record.get("rights")
    metadata["language"] = language  

    return metadata


loader = JSONLoader(
    file_path=file_path,        
    jq_schema='.items[]',       
    metadata_func=metadata_func # Funzione per i metadati
)

data = loader.load()

pprint(data)
