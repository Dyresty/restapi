import requests
import json
import sys

url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'

response = requests.get(url)
#data = response.json()
#print(data)
for data in response.json()['items']:
    #print(data)
    if data['score']>=1:
        print(data['title'])
        print(data['link'])
        print(data['score'])
        print()
    else:
        print("Skipped because the criteria of score>=1 is not satisfied")
        print()    