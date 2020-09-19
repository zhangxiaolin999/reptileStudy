import urllib.request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context;

def load_data():
    url = "http://www.baidu.com/"
    # get请求
    response = urllib.request.urlopen(url)
    data = response.read()
    str_data = data.decode()
    print(str_data)
    with open("file/baidu.html", "w", encoding="utf-8")as f:
        f.write(str_data)


load_data()


