import json

from selenium import webdriver
from time import sleep
# pip install selenium  selenium 自动化测试工具的py库
# chrome浏览器 chromedriver驱动文件，对应chrome版本号  https://registry.npmmirror.com/binary.html?path=chromedriver/
# https://chromedriver.storage.googleapis.com/index.html  https://sites.google.com/chromium.org/driver/
# macos /usr/local/bin/chromedriver win chromedriver.exe放在python.exe旁边
from selenium.webdriver.common.by import By

users = [
    {"username":"demo123","password":"demo123"},
    {"username":"demo1234","password":"demo1234"},
    {"username":"test1234","password":"test1234"},
    {"username":"1234566","password":"1234566"},
]

def main(username,password):
    url = 'http://shanzhi.spbeen.com/login/'
    cb = webdriver.Chrome()
    cb.get(url)
    sleep(1)
    # username_input = cb.find_element_by_xpath('.//input[@id="username"]')
    username_input = cb.find_element(By.ID,"username")
    username_input.send_keys(username)
    # password_input = cb.find_element_by_xpath('.//input[@id="MemberPassword"]')
    password_input = cb.find_element(By.ID,"MemberPassword")
    password_input.send_keys(password)
    sleep(2)
    submit_button = cb.find_element(By.XPATH,'.//button[@onclick="doLogin()"]')
    submit_button.click()
    sleep(2)
    # print("username:",username,"password",password)
    cookies_list = cb.get_cookies()
    # print(cookies_list)

    # with open("cookies_auto_v1.txt",'a',encoding='utf8') as file:
    #     file.write(json.dumps(cookies_list))
    #     file.write('\n')

    cookies_dict = { ck['name']:ck['value'] for ck in cookies_list}
    print(cookies_dict)
    with open("cookies_auto_v2.txt",'a',encoding='utf8') as file:
        file.write(json.dumps(cookies_dict))
        file.write('\n')

    cb.quit()
if __name__ == "__main__":
    for user in users:
        username = user["username"]
        password = user["password"]
        main(username, password)
        # break