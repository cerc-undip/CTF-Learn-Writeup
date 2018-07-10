#!/usr/bin/python3
import requests

r = requests.get('https://ctflearn.com/header.php', headers={'user-agent': 'Sup3rS3cr3tAg3nt', 'referer': 'awesomesauce.com'})
print(r.text)
