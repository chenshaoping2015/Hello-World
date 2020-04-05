#coding=utf-8
from selenium import webdriver
import time
#下面四行这么写是去掉谷歌浏览器上面提示的，第二行和第三行分别对应不同的提示
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument('disable-infobars')
browser = webdriver.Chrome() #chrome_options=options
browser.maximize_window()
#输入网址
browser.get("https://www.baidu.com")
#点击登录，用下面注释的代码获取cookie，实现跳过登录，执行脚本的时候就不用这部分了
# browser.find_element_by_id("su").click()
# cookie1= browser.get_cookies()
#打印登录前的cookie
# print (cookie1)
#等待30秒，用这30秒时间完成登录操作
# time.sleep(30)
#获取登录后的cookie
# cookie2= browser.get_cookies()
#打印登录后的cookie
# print (cookie2)
#
#加入要获取的cookie，写进去
browser.add_cookie({'name':'BDUSS', 'value':'pjS0lWT3k4TzhsSGluakV1QnJ4c0d4WjhFOUdDMFg5LVFDU0tScUdLNWpCNmRlSVFBQUFBJCQAAAAAAAAAAAEAAABZwdg9Y2hlbl9zdGV2ZW4xMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGN6f15jen9eQ2'})
#刷新网站
time.sleep(3)
browser.refresh()