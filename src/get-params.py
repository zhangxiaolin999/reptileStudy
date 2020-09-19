import urllib.request
import urllib.parse
import string
import ssl
ssl._create_default_https_context=ssl._create_unverified_context;


def get_method():
    url = "http://www.baidu.com/s?wd="
    name = '学习python爬虫'
    final_url = url + name
    encode_new_url =  urllib.parse.quote(final_url,safe=string.printable)
    response = urllib.request.urlopen(encode_new_url) #使用代码发送网络请求
    data =  response.read().decode()
    print(data)
    with open("file/Getparams.html","w",encoding="utf-8")as f:
        f.write(data)



get_method()