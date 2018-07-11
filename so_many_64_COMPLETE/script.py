#!/usr/bin/python3
import base64

f = open('flag.txt', 'r')
hasil = f.read()

while True:
  hasil = base64.b64decode(hasil).decode('utf-8')

  if '{' in hasil:
    print(hasil)
    break
