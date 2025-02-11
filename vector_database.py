import json
import sqlite3
from pathlib import Path
from pprint import pprint
from langchain_community.document_loaders import JSONLoader

file_path = 'dati_europeana.json'  

data = json.loads(Path(file_path).read_text())

conn = sqlite3.connect(":memory:")  # database in memory
cursor = conn.cursor()

# set up table
cursor.execute('''
    CREATE TABLE documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        creator TEXT,
        timestamp TEXT,
        rights TEXT,
        language TEXT
    )
''')
conn.commit()

def metadata_func(record: dict) -> dict:
    language = record.get("language")

   
    if language and language not in ["en", "it"]: 
        return None # return only ita and eng

    return {
        "title": record.get("title"),
        "creator": record.get("creator"),
        "timestamp": record.get("timestamp"),
        "rights": record.get("rights"),
        "language": language
    }


loader = JSONLoader(
    file_path=file_path,        
    jq_schema='.items[]',       
    metadata_func=metadata_func
)

data = loader.load()  # Carica i dati dal file JSON

# insert data into database
for record in data:
    metadata = record.metadata
    cursor.execute("INSERT INTO documents (title, creator, timestamp, rights, language) VALUES (?, ?, ?, ?, ?)",
                   (metadata["title"], metadata["creator"], metadata["timestamp"], metadata["rights"], metadata["language"]))

conn.commit()  # Salviamo le modifiche

# print data to test
cursor.execute("SELECT * FROM documents LIMIT 5")
rows = cursor.fetchall()

print("\nDati salvati nel database:")
for row in rows:
    pprint(row)

# close database 
# conn.close()
