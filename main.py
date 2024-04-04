from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import time

# 创建一个新的浏览器实例
driver = webdriver.Firefox()

# 打开登录页面
driver.get('https://www.nodeseek.com/signIn.html')

# 找到邮箱输入框并输入数据
email_field = driver.find_element(By.ID, 'stacked-email')
email_field.send_keys('jess')

# 找到密码输入框并输入数据
password_field = driver.find_element(By.ID, 'stacked-password')
password_field.send_keys('xjlxjl123')

# 找到登录按钮并点击
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

# 等待10秒，让JavaScript有足够的时间设置cookie
time.sleep(10)

# 获取cookies
cookies = driver.get_cookies()

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
driver.quit()