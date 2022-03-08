import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

users = [
    {"username":"demo123","password":"demo123"},
    {"username":"demo1234","password":"demo1234"},
    {"username":"test1234","password":"test1234"},
    {"username":"1234566","password":"1234566"},
]
# 程序将预处理的内容处理好后 - 等待用户处理 - 用户处理的同时,程序一直监听 - 直到用户直接关闭了浏览器，程序监听异常，继续往下执行
def wait_cookie(browser):
    num=1
    while True:
        try:
            cookies_list = browser.get_cookies()
            cookies_dict = {ck['name']: ck['value'] for ck in cookies_list}
            print(num, cookies_dict)
        except:
            with open("cookies_half_auto.txt", 'a', encoding='utf8') as file:
                file.write(json.dumps(cookies_dict))
                file.write('\n')
            break
        sleep(3)
        num += 1

        # browser.quit()

def main(username,password):
    url = 'http://shanzhi.spbeen.com/login/'
    cb = webdriver.Chrome()
    cb.get(url)
    sleep(1)

    # 程序可以主动处理的部分都交给程序去做
    username_input = cb.find_element(By.ID,"username")
    username_input.send_keys(username)
    password_input = cb.find_element(By.ID,"MemberPassword")
    password_input.send_keys(password)
    sleep(2)

    # 若登录的时候，弹出行为验证框，则登录还未成功，拿不到已登录的cookies
    # submit_button = cb.find_element(By.XPATH,'.//button[@onclick="doLogin()"]')
    # submit_button.click()
    # sleep(2)

    wait_cookie(cb)

if __name__ == "__main__":
    for user in users:
        username = user["username"]
        password = user["password"]
        main(username, password)
        # break