
import subprocess
path = 'C:/Users/Administrator/Desktop/post_url/first/'
url = ' '
temp = 1
for num in range(1, 6540):
    print('推送第' + str(temp) + '条' )
    temp += 1
    urls = open(path + str(num) + '.txt', 'r+')
    line = urls.readline()
    url = line.split('/', 2)[0]
    print(line)
    if num % 31 == 0:
        urls = open(path + str(num) + '.txt', 'r+')
        url = urls.readline().split('/', 4)[2]
        print(url)
    output = subprocess.Popen('curl -H "Content-Type:text/plain" --data-binary @' + path + str(num) + '.txt "http://data.zz.baidu.com/urls?site=' + url + '&token=GCahOl36x0hNa7TA"', shell=True, stdout=subprocess.PIPE)
    print(output.stdout.readlines())
    num += 1
