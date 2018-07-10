#!/usr/bin/python3
import requests

url = "https://ctflearn.com/post.php"

re = requests.post(url, data={'username': 'admin', 'password': '71urlkufpsdnlkadsf'})
print(re.text)
