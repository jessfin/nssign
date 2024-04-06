import os
import requests
import json

# Get the session from environment variables
session = os.getenv('SESSION')

# Your cookies
cookie_str = f"session={session}"

# Now you can use requests library to send POST request
url = "https://www.nodeseek.com/api/attendance?random=true"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Cookie": cookie_str
}
response = requests.post(url, headers=headers)

data = json.loads(response.text)

print(data["message"])
