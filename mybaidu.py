from urllib.request import urlopen

url = "https://baidu.com"
resp = urlopen(url)

with open("mybaidu.html", mode="w", encoding='utf8') as f:
    f.write(resp.read().decode("utf-8"))


print("over")