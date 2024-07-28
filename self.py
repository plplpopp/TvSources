import requests

url = "http://godiptv.dns.navy:1024/tv/getVideoConfigByPath/txt/IAI8931N44NE79D1/2/heightlow/y/ipv46/全部"

r = requests.get(url)
r.encoding = "utf-8"

new = []

if r.status_code == 200:
    line = r.text.split("\n")
    for li in line:    
        if "更新时间" in li:
            break
        else:
            new.append(li)
with open("./self.txt", "w", encoding="utf-8") as file:
        for i in new:
            file.write(i + "\n")
