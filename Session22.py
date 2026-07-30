#Q1
from traceback import print_tb
import requests
session=requests.Session()
url="https://www.flipkart.com/"
response1=session.get(url)
print("first request status code:",response1.status_code)
response2=session.get(url)
print("second request status code:",response2.status_code)
print("\cookies stored")
print(session.cookies.get_dict())

#Q2
import requests
url="https://api.openweathermap.org/data/2.5/weather"
params={
    "q":"Ahmedabad",
    "appid":"your_api_key",
    "units":"metric"
}
response=requests.get(url,params=params)
data=response.json()
print("current temperature:",data["main"]["temp"],"celsius")

#Q3
import asyncio
import httpx
async def fetch_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()[:3]
async def fetch_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/users")
        return response.json()[:3]
async def main():
    posts, users = await asyncio.gather(
        fetch_posts(),
        fetch_users()
    )

    print("Posts:")
    print(posts)

    print("\nUsers:")
    print(users)
asyncio.run(main())

#Q4
import requests
def get_user_profile():
    url="https://jsonplaceholder.typicode.com/users/1"

    headers={
        "authoriztion":"bearer fake_token_123"
    }
    response=requests.get(url,headers=headers)
    data=response.json
    print("user name:",data["name"])

get_user_profile()

#Q5
from urllib.parse import urlencode

client_id = "YOUR_CLIENT_ID"
redirect_uri = "http://localhost:8000/callback"

params = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "scope": "user-read-email"
}

auth_url = "https://accounts.spotify.com/authorize?" + urlencode(params)

print("OAuth Login URL:")
print(auth_url)