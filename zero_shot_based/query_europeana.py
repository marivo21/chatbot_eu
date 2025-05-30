import requests
import re
API_KEY = '-'

BASE_URL = 'https://api.europeana.eu/record/v2/search.json'

r = requests.get("https://api.europeana.eu/record/v2/search.json?wskey=-&query=caravaggio")


response = r.json()

descriptions = [
    re.sub('\n+', ' ', 
        ' '.join(response['items'][i]['dcDescriptionLangAware']['en'])
    ) for i in range(len(response['items'])) 
        if 'dcDescriptionLangAware' in response['items'][i] and 
        'en' in response['items'][i]['dcDescriptionLangAware']
]

print(descriptions[:100]) 
