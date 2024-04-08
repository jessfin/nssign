from playwright.sync_api import sync_playwright
import requests
import json
import time

accounts = [
    {'username': 'jess', 'password': 'xjlxjl123'},
    {'username': 'username2', 'password': 'password2'},
    {'username': 'username3', 'password': 'password3'}   #参照此示例可以继续添加需要签到的账号
]

with sync_playwright() as p:
    for account in accounts:

        browser = p.firefox.launch()

        page = browser.new_page()

        page.goto('https://www.nodeseek.com/signIn.html')

        page.fill('#stacked-email', account['username'])

        page.fill('#stacked-password', account['password'])

        page.click('//button[@type="submit"]')

        time.sleep(60)

        cookies = page.context.cookies()

        cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

        url = "https://www.nodeseek.com/api/attendance?random=true"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "Cookie": cookie_str
        }
        response = requests.post(url, headers=headers)

        data = json.loads(response.text)

        print(f"用户名: {account['username']}")
        print(data["message"])

        browser.close()
        
