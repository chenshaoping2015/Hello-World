# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get('http://www.sahitest.com/demo/php/fileUpload.htm')
driver.find_element_by_id('file').click()
time.sleep(1)

os.system('D:\\upfile.exe "D:\\baidu.py"')  # 这里可以对传参进行参数化，我们可以通过py脚本来控制所要上传的文件了

time.sleep(3)
driver.quit()