from selenium import webdriver
import os

#chrome浏览器配置文件地址
profile_dir = r'C:\Users\stevechen\AppData\Local\Google\Chrome\User Data'
# 加载配置
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('user-data-dir='+os.path.abspath(profile_dir))
# 启动浏览器配置
driver = webdriver.Chrome(chrome_options=chrome_option)
driver.maximize_window()
driver.implicitly_wait(2)  # 单位秒
driver.get("https://home.cnblogs.com/u/chenshaoping/followees/")

# url = "https://home.cnblogs.com/u/chenshaoping/followers/"
# driver.get(url)
# driver.implicitly_wait(2)  # 单位秒