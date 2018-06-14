# -*- coding=utf-8 -*-
urls = open('url/9_150_post_url.txt', "r+")
temp = 0
num = 1
file = open('first/' + str(num) + '.txt', 'w+')
for url in urls:
    if temp < 2000:
        print(url.strip('\n') + '\t' + str(temp) + '\n')
        file.write(url)
        temp += 1
    else:
        print(url.strip('\n') + '\t' + str(temp) + '\n')
        temp = 1
        num += 1
        print('first/' + str(num) + '.txt', 'w+')
        file = open('first/' + str(num) + '.txt', 'w+')
        file.write(url)
        print('新增1个')