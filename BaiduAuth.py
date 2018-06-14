from selenium import webdriver
import paramiko
import os
import time
import platform
from ftplib import FTP
from selenium.webdriver.common.action_chains import ActionChains
import random

local = os.path.normcase(os.path.abspath('.')) #项目相对路径
host = "142.234.162.79" #服务器host
root = "hentai"   #账号
password = "hentai123456" #密码
remotepath = '/www/wwwroot/xbw/' #远程提交路径
localpath = local + '/down/'    #本地上传路径
yuming = local + '/yuming/yuming.txt' #域名库文件
sysstr = platform.system()
if sysstr =="Windows":
    path = local + "/driver/chromedriver.exe"  # 谷歌控制器路径
    profile = 'C:/Users/username/AppData/Local/Google/Chrome/User Data/test_profile'
else:
    path = local + "/driver/chromedriver"  # 谷歌控制器路径
    profile = '/Users/YV/Library/Application Support/Google/Chrome/Default'

print('正在连接FTP服务器')
ftp = FTP()                         #设置变量
ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
ftp.connect(host, 24)          #连接的ftp sever和端口
ftp.login(root, password)      #连接的用户名，密码
print(ftp.getwelcome())            #打印出欢迎信息

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': localpath, 'profile.managed_default_content_settings.images': 2}
options.add_argument("--user-data-dir="+profile)
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(path, chrome_options=options)  # 打开 Chrome 浏览器
driver.implicitly_wait(10)   # seconds
driver.get("https://ziyuan.baidu.com/login/index?u=/site/index")
print('登陆成功')
driver.get("https://ziyuan.baidu.com/site/index")
cookie = driver.get_cookies()
print(cookie)
time.sleep(1)
print('点击确认添加站点')
site_add = driver.find_element_by_id('site-add-btn')
site_add.click()
time.sleep(1)
file = open(yuming)

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for url in lines:
        pass
        print('更改协议头')
        http = driver.find_element_by_xpath("//div[@id='protocolSelect']/input")
        driver.execute_script("arguments[0].value = 'http://'", http)
        print('添加url:' + url)
        sendurl = driver.find_element_by_class_name('add-site-input')
        sendurl.send_keys(url)
        urladd = driver.find_element_by_id('site-add')
        urladd.click()
        time.sleep(1)

        if driver.current_url == 'https://ziyuan.baidu.com/site/siteadd':
            print('该网站url已经提交过了')
            driver.get("https://ziyuan.baidu.com/site/siteadd")
            continue
        else:
            print('未添加过的域名')
        # print('后退浏览器')
        # driver.back()
        # print('再次点击添加网站')
        # time.sleep(2)
        # driver.find_element_by_id('site-add').click()
        print('确认域名领域')
        time.sleep(1)
        driver.execute_script("document.getElementById('check4').checked = true;")
        driver.execute_script("document.getElementById('check5').checked = true;")
        driver.execute_script("document.getElementById('check9').checked = true;")
        time.sleep(1)
        driver.find_element_by_id('sub-attr').click()
        print('开始下载验证文件')
        while 1:
            try:
                filename = os.listdir(localpath)
                print('已找到下载文件' + filename[0])
                break
            except:
                print('还没定位到本地文件')

        while 1:
            start = time.clock()
            try:
                driver.find_element_by_xpath("//dd[@id='file']/p[2]/a[1]").click()
                print('已定位到下载按钮')
                end = time.clock()
                break
            except:
                print("还未定位到下载按钮!")
        print('定位耗费时间：' + str(end - start))
        time.sleep(1)

        print('开始上传本地文件')
        bufsize = 1024  # 设置缓冲块大小
        file_handler = open(localpath + filename[0], 'rb')  # 以读模式在本地打开文件
        ftp.storbinary('STOR %s' % os.path.basename(filename[0]), file_handler, bufsize)  # 上传文件
        ftp.set_debuglevel(0)
        file_handler.close()
        while 1:
            if ftp.size(filename[0]) > -1:
                print('上传成功')
                break
            else:
                print("还未上传成功，请等待!")
        time.sleep(5)
        my_file = localpath + filename[0]
        if os.path.exists(my_file):
            print('删除本地下载文件')
            os.remove(localpath + filename[0])
        else:
            print('文件没有删除')
            print('开始验证服务器文件')
        driver.find_element_by_id('verifySubmit').click();
        while 1:
            start = time.clock()
            try:
                driver.find_element_by_id("dialog").click()
                print('验证成功')
                end = time.clock()
                break
            except:
                print("正在验证中，请等待!")
        driver.get("https://ziyuan.baidu.com/site/siteadd");
ftp.quit()
print('FTP关闭')
