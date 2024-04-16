import requests
import json

# Your cookies
cookies = [
    "session=a78d8cdbb42df588",
 #  "session=84a78d8",
 #   "session=2684a78d8",  // 修改session后面的值，如果需要多用户请删除前面#
]

# Now you can use requests library to send POST request
url = "https://www.nodeseek.com/api/attendance?random=true"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Referer": "https://www.nodeseek.com/credit"
}

for cookie in cookies:
    headers["Cookie"] = cookie
    response = requests.post(url, headers=headers)

    data = json.loads(response.text)

    print(data["message"])
    
