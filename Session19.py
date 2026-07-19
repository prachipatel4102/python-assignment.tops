#Q1
from fastapi.datastructures import Headers
from fastapi import params
import json
from requests import get
from fastapi import responses
import requests
url="https://jsonplaceholder.typicode.com/posts"
responses=requests.get(url)
posts=responses.json()
for post in posts[:5]:
    print(post["title"])

#Q2
import json
restaurent={
    "name":"Pizza Hut",
    "location":"Ahmedabad",
    "cuisines":["pizza","italian","fast food"],
    "ratings":4.5
}
json_data=json.dumps(restaurent,indent=4)
print(json_data)

#Q3
import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"My playlist",
    "userid":1,
    "body":"MY favorite songs"
}
response=requests.post(url,json=data)
print("status code:",response.status_code)
print("response:")
print(response.json())

#Q4
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, params={"userId": 2})

posts = response.json()

for post in posts:
    print(post["id"])

#Q5
import requests
url="https://jsonplaceholder.typicode.com/posts"
Headers={
    "Authorization":"bearer my_token_123"
}
response=requests.get(url,headers=Headers)
print("status code:",response.status_code)