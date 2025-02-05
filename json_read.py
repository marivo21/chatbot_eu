import json
from pathlib import Path
from pprint import pprint


file_path= ' dati_europeana ' # inserire nome dati
data = json.loads(Path(file_path).read_text())

pprint(data)
