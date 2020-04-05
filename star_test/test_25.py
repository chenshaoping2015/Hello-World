# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

#download.default_directory：设置下载路径
#profile.default_content_settings.popups：设置为 0 禁止弹出窗口

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit()