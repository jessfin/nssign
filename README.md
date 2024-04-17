# nodeseek自动签到
 nodeseek自动获取随机鸡腿

## 4月16日更新 
现以可用
 
## 使用方法
将username和password改成自己的
```
git clone https://github.com/jessfin/nssign
cd nssign
```
```
pip install -r requirements.txt
playwright install firefox
```
如果安装firefox报错请执行`debian/ubuntu`
```
apt install libxcb-shm0 libx11-xcb1 libxrandr2 libxcomposite1 libxcursor1 libxdamage1 libxfixes3 libxi6 libgtk-3-0 libgdk-pixbuf2.0-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libglib2.0-0 libasound2 libxrender1
```
###测试运行

```
python3 main.py
```

自己设置定时任务
