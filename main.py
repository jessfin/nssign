from playwright.sync_api import sync_playwright
import requests
import json
import time

with sync_playwright() as p:
    # 创建一个新的浏览器实例
    browser = p.firefox.launch()

    # 打开新的页面
    page = browser.new_page()

    # 打开登录页面
    page.goto('https://www.nodeseek.com/signIn.html')

    # 找到邮箱输入框并输入数据
    page.fill('#stacked-email', 'jess', timeout=60000)

    # 找到密码输入框并输入数据
    page.fill('#stacked-password', 'xjlxjl123', timeout=60000)

    # 找到登录按钮并点击
    page.click('//button[@type="submit"]')

    # 等待10秒，让JavaScript有足够的时间设置cookie
    time.sleep(60)

    # 获取cookies
    cookies = page.context.cookies()

    # 转换cookies为headers中的"Cookie"字段可以使用的格式
    cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

    # 现在你可以使用requests库发送POST请求
    url = "https://www.nodeseek.com/api/attendance?random=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Cookie": cookie_str
    }
    response = requests.post(url, headers=headers)

    data = json.loads(response.text)

    print(data["message"])

    # 关闭浏览器实例
    browser.close()
