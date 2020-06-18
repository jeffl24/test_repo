import requests
import json
import pandas as pd
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999


total_results = []
page_num = 1
username = '7e86d45b24d9a3da5da72a93a8210f34'
password = '3ddc548cff03ffd7d064c7e2fa7f3431'
shop = 'paulas-choice-singapore'
api_version = '2020-04'
resource = 'orders'
since_id = 2277025054785


url = f'https://paulas-choice-singapore.myshopify.com/admin/api/2020-04/orders.json?limit=50&since_id={since_id}'
page_info = ['dummy']

while len(page_info) > 0 :   
    print(f"requesting page {page_num}: {url}")
#     print(next_page)
    result = requests.get(url, auth=(username, password))
#     print(result.headers)
    data = result.json()
    total_results = total_results + data['orders']
    result_headers = result.headers
    page_info = re.findall(r', <(.+?)>(?=; rel="next")', str(result_headers))
    print("page_info: \n",page_info)
    print(len(page_info))
    if len(page_info) > 0:
        url = page_info[0] 
        print("overriden url: ", url)
#         print("page_info :", page_info[0])
    else: break
    page_num += 1

# pd.DataFrame.from_dict(total_results)
with open('since_2277025054785_191569954497.json', 'w') as file:
    json.dump(total_results, file)