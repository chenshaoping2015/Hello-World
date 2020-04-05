# -*- coding: UTF-8 -*-
# excel说：感觉自己被操控

# excel读写库
import xlrd
import xlwt

# selenium浏览器驱动
from selenium import webdriver
import time

# 初始化Chrome()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)  # 单位秒


# 登陆
def login():
    # 我自己可用的内网ip地址
    url = "https://www.baidu.com"
    print("你的小可爱正在打开： " + url + "   请看好她!!!\n")
    driver.get(url)
    driver.find_element_by_link_text("登录").click()
    time.sleep(8)
    driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()


# excel读取
def read_xl():
    # 打开excel
    workbook = xlrd.open_workbook('C:\\Users\\stevechen\\Desktop\\login.xlsx')

    sheet = workbook.sheets()[0]  # 代表第一个页签，excel是可以有多个页签的
    nrows = sheet.nrows  # 看excel一共有多少行内容

    # 一行一行的读取内容，sheet.row_values(i)[0]代表该行的第一个单元格
    for i in range(nrows):
        sw(sheet.row_values(i)[0], sheet.row_values(i)[1])


# 转化excel读取的操作

def sw_input(b, c, d):
    if b == 'id':
        driver.find_element_by_id(c).send_keys(d)
    elif b == 'xpath':
        driver.find_element_by_xpath(c).send_keys(d)


def sw_wait(d):
    time.sleep(d / 1000)


def sw_open(d):
    time.sleep(1)


login()
read_xl()
