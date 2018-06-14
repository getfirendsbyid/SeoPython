# 顶级域名加前缀
file1 = open('9.txt', 'r+')
file2 = open('www_all_9.txt', 'w+')

for line in file1:
    print(line)
    file2.write('www.' + line)
    pres = open('news_pre.txt', 'r+')
    for pre in pres:
        print(pre.strip('\n') + '.' + line)
        file2.write(pre.strip('\n') + '.' + line)