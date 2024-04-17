from playwright.sync_api import sync_playwright
import requests
import json
import time
import os

accounts = [
    {'username': 'username1', 'password': 'password1'},
    {'username': 'username2', 'password': 'password2'},
    {'username': 'username3', 'password': 'password3'}
]

def save_cookie(username, cookie_str):
    with open('cookie.txt', 'a') as file:
        file.write(f"{username}: {cookie_str}\n")

def load_cookies():
    cookies = {}
    if os.path.exists('cookie.txt'):
        with open('cookie.txt', 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                parts = line.split(': ')
                if len(parts) == 2:
                    username = parts[0]
                    cookie_str = parts[1]
                    cookies[username] = cookie_str
    return cookies

def remove_cookie(username):
    cookies = load_cookies()
    if username in cookies:
        del cookies[username]
        with open('cookie.txt', 'w') as file:
            for username, cookie_str in cookies.items():
                file.write(f"{username}: {cookie_str}\n")

with sync_playwright() as p:
    for account in accounts:
        cookies = load_cookies()

        if account['username'] in cookies:
            cookie_str = cookies[account['username']]
        else:
            browser = p.firefox.launch()
            page = browser.new_page()
            page.goto('https://www.nodeseek.com/signIn.html', timeout=60000)
            page.fill('#stacked-email', account['username'])
            page.fill('#stacked-password', account['password'])
            page.click('//button[@type="submit"]')
            time.sleep(60)
            cookies = page.context.cookies()
            cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            save_cookie(account['username'], cookie_str)
            browser.close()

        url = "https://www.nodeseek.com/api/attendance?random=true"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "Referer": "https://www.nodeseek.com/credit",
            "Cookie": cookie_str
        }
        response = requests.post(url, headers=headers)
        data = json.loads(response.text)
        print(f"用户名: {account['username']}")
        print(data["message"])

        if data["message"] == "USER NOT FOUND":
            remove_cookie(account['username'])
            continue
