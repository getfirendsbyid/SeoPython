# -*- coding=utf-8 -*-
import random
# 所有域名生成要推送的内页 2000条
urls = open('url/9_220.txt', "r+")
post_url = open('url/9_220_post_url.txt', 'w+')
temp = 0
for url in urls:
    indexs = open('url/index.txt', "r+")
    for index in indexs:
        print(index)
        for num in range(66666, 68666):
            post_url.write('www.' + url.strip('\n') + '/' + index.strip('\n') + '20180608' + str(random.randint(10000, 99999)) + '.html\n')
            print('www.' + url.strip('\n') + '/' + index.strip('\n') + '20180606' + str(random.randint(10000, 99999)) + '.html\n')
print('程序结束')
