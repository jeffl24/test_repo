import requests
import json

url = 'https://api.tradegecko.com/variants'
bearer = {'Authorization': 'Bearer f4855aebc4a92c0d6a09f07b105bcbae81afbaf8cb1344f47a5b5c45cf8f4c1e'}

# convert data to json format
variants_request = requests.get(url, headers=bearer)