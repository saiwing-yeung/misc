# solution for http://letsrevolutionizetesting.com/challenge

import requests

url = 'http://letsrevolutionizetesting.com/challenge'
r = requests.get(url, headers={'Accept': 'application/json'})
print(r.json())
