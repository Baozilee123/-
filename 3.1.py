import urllib.request

# response = urllib.request.urlopen('http://www.baidu.com')   #发送网络请求
# print('响应数据类型为：',type(response))

url = 'https://www.python.org/'
response = urllib.request.urlopen(url=url)
print('响应状态码为：',response.status)
print('响应头指定信息为：',response.getheaders())
print('响应头指定信息为:',response.getheader('Accept-Ranges'))
print('Python官网HTML代d码如下：\n',response.read().decode('utf-8'))   #奇怪的事，有时能显示出来，有时候会报错：'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte