import requests
from lxml import etree
from login_crypto import encrypto
from python_js_encrypto import js_encrypto

url = 'http://shanzhi.spbeen.com/login/'
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36",
    "Cookie": "_ga=GA1.2.2137233700.1646625095; _gid=GA1.2.1215266905.1646625095; csrftoken=F4njHhlPe8XOk1lbwz7h0TGaqqGFqZsEs2J2CcYKDm8jZS4xoZkNDwZZfJApqbSd; _gat=1"
}

get_response = requests.get(url, headers=headers)
# print(get_response,get_response.text)

html = etree.HTML(get_response.text)
pk = html.xpath('.//input[@id="pk"]/@value')
pk = pk[0]
print("公钥:", pk)

token = html.xpath('.//input[@name="csrfmiddlewaretoken"]/@value')
token = token[0]

username = '1234566'
password = '1234566'
# 通过encrypto加密
miwen_password = encrypto(pk, password)
print("密码：", password, "\n通过encrypto加密后：", miwen_password)
# 通过js_encrypto加密
miwen = js_encrypto(pk, password)
print("密码：", password, "\n通过js_encrypto加密后：", miwen)

formdata = {
    'username': username,
    'password': miwen_password,
    'csrfmiddlewaretoken': token,
}
# print(formdata)
# 提交后的响应数据
post_response = requests.post(url, headers=headers, data=formdata)
# 输出首次跳转的headers信息
print(post_response.history[0].headers)
# 输出 返回状态码和html文本
print(post_response, post_response.text)

# 若返回码大于400，使用wb二进制写到html中
if post_response.status_code >= 400:
    with open('error.html', 'wb') as file:
        file.write(post_response.content)
