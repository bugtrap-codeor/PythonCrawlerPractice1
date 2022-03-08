import json

import requests
from lxml import etree
from login_crypto import encrypto
from python_js_encrypto import js_encrypto

users = [
    {"username":"demo123","password":"demo123"},
    {"username":"demo1234","password":"demo1234"},
    {"username":"test1234","password":"test1234"},
    {"username":"1234566","password":"1234566"},
]

def main(username,password):
    url = 'http://shanzhi.spbeen.com/login/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36",
    }
    session = requests.session()

    get_response = session.get(url, headers=headers)
    # print(get_response,get_response.text)

    html = etree.HTML(get_response.text)
    pk = html.xpath('.//input[@id="pk"]/@value')
    pk = pk[0]
    print("公钥:", pk)

    token = html.xpath('.//input[@name="csrfmiddlewaretoken"]/@value')
    token = token[0]

    # 通过encrypto加密
    miwen_password = encrypto(pk, password)
    print("密码：", password, "\n通过encrypto加密后：", miwen_password)
    # 通过js_encrypto加密
    # miwen = js_encrypto(pk, password)
    # print("密码：", password, "\n通过js_encrypto加密后：", miwen)

    formdata = {
        'username': username,
        'password': miwen_password,
        'csrfmiddlewaretoken': token,
    }
    # print(formdata)
    # 提交后的响应数据
    post_response = session.post(url, headers=headers, data=formdata)
    # 输出首次跳转的headers信息
    print(post_response.history[0].headers)
    # 输出 返回状态码和html文本
    print(post_response, post_response.text)

    cookies_dict = session.cookies.get_dict()
    cookies_str = json.dumps(cookies_dict)
    with open("cookies_v2.txt",'a',encoding='utf8') as file:
        file.write(cookies_str)
        file.write('\n')

    # 若返回码大于400，使用wb二进制写到html中
    if post_response.status_code >= 400:
        with open('error.html', 'wb') as file:
            file.write(post_response.content)

if __name__ == "__main__":
    for user in users:
        username = user["username"]
        password = user["password"]
        main(username, password)