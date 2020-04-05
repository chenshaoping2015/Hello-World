
# coding:utf-8
import requests

# 先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}  # get方法其它加个ser-Agent就可以了

s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(s.cookies)
#  添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()

c.set('.CNBlogsCookie', 'EF708ED9005D7C4B11207191F60C0793E8157C12CDBB8F2EAFD51A6E2229DD61B17999E13120396A0BA6CBB2E434F21FC94ED10538A3923B56248A89068686BCAAA7B4A3D9044FC985B366F070635473A8C5FA86')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8Nf-Z6tqUPlNrwu2nvfTJEgfJiHXHfNO5653RGJtkrsX05JK9988_kqQ1w35GaODB1TIy3ANCaCRKOZSVbvsrE8xCIXTQicOiEw2IlMbx6xpO2d3GJ5cfdLcAs_j0njjOctKDQMBingyGjHIX4tfFdZ7A8yJfQH0t0F-pTAToXvdYTXEvGt68rRq234OFnMqI_WETLJosotkPflhufeReV7zY0C_jEJu9N0gxhmbMnOAfgMEo_4JysMGOBwpGOYZAIwEbYyiELmYhAwdbqlDEhGhSJLxrWkv-p2JHv_8IvRPV6npOlLR2HMI3xoXXN-sJXXcFPgY7U5U-oXHDRMoxr4YJVrI3ib4c6SohbHakqvY4RL_2C-MgBjb_fFjkLQV1W6U_ZGoUtiX3KzLIIsO_1FVrzARulIrkGQNlS4imhj-VGWWjv_iMKDbqix6sdzIiJQ5HaMER5i9wqMsT_JFC1FjiJnmHBHKMWYG8c3g5tvLi8wPI5Ls409A4AEQkxDREDr8jBXMVsmd81iOvmw1N_6BoR7ZHbLb8Je2RaX2QAokHcU-D8gsSqvJsJFUeAtX7g	')  # 填上面抓包内容
s.cookies.update(c)
print(s.cookies)
#
# 登录成功后保存编辑内容
r1 = s.get("https://home.cnblogs.com/u/chenshaoping/followees/", headers=headers, verify=False)
# 保存草稿箱
# url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR": "FE27D343",
#         "Editor$Edit$txbTitle": "这是3111",
#         "Editor$Edit$EditorBody": "<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished": "on",
#         "Editor$Edit$Advanced$chkDisplayHomePage": "on",
#         "Editor$Edit$Advanced$chkComments": "on",
#         "Editor$Edit$Advanced$chkMainSyndication": "on",
#         "Editor$Edit$Advanced$txbEntryName": "",
#         "Editor$Edit$Advanced$txbExcerpt": "",
#         "Editor$Edit$Advanced$tbEnryPassword": "",
#         "Editor$Edit$lkbDraft": "存为草稿",
#         }
# r2 = s.post(url2, data=body, verify=False)
print(r1.text)

# print(driver.get_cookies())
# print("-------------------------")
# driver.find_element_by_link_text("账号密码登录").click()
# driver.implicitly_wait(2)
# driver.find_element_by_id("all").send_keys("you14563@163.com")
# driver.find_element_by_id("password-number").send_keys("2010080101303")
# driver.find_element_by_class_name("btn-primary").click()
# driver.implicitly_wait(2)
# print(driver.get_cookies())
