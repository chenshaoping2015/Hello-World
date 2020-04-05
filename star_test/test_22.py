# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
time.sleep(5)
upload.send_keys('D:\\baidu.py') # send_keys
time.sleep(5)
print(upload.get_attribute('value'))# check value

driver.quit()

