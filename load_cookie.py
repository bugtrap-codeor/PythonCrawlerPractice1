import requests
import json

# with open("cookies_auto_v2.txt",'r',encoding='utf8') as file:
with open("cookies_v2.txt",'r',encoding='utf8') as file:
    cookie_list = file.readlines()

# session = requests.session() # 不要在一个session中装载多个账号信息
for cookie_str in cookie_list:
    cookie_dict = json.loads(cookie_str)
    session = requests.session()
    session.cookies = requests.utils.cookiejar_from_dict(cookie_dict)
    response = session.get("http://shanzhi.spbeen.com/index/")
    print(response,response.text)