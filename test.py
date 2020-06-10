import requests
import json

url = 'https://api.tradegecko.com/variants'
bearer = {'Authorization': 'Bearer f4855aebc4a92c0d6a09f07b105bcbae81afbaf8cb1344f47a5b5c45cf8f4c1e'}

# convert data to json format
variants_request = requests.get(url, headers=bearer).text
variants_json = json.loads(variants_request)

# Start with an empty list
total_results = []

# Grab the search results
print("Downloading the original search results")
response = requests.get(url, headers=bearer)
data = response.json()

# Store the first page of resultsd
total_results = total_results + data['results']

# While data['next'] isn't empty, let's download the next page, too
while data['next'] is not None:
    print("Next page found, downloading", data['next'])
    response = requests.get(data['next'])
    data = response.json()
    # Store the current page of results
    total_results = total_results + data['results']

print("We have", len(total_results), "total results")