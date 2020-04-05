# -*- coding: utf-8 -*-
from selenium import webdriver
import win32gui
import win32con
import time

dr = webdriver.Chrome()
dr.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = dr.find_element_by_id('file')
upload.click()
time.sleep(1)

# win32gui
dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
print(dialog)
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
print(ComboBoxEx32)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
print(ComboBox)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

print(upload.get_attribute('value'))
