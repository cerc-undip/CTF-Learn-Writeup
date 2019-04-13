#!/usr/bin/python3
import re

soal = "d733432373937303734373666343730373937323733343b7644534"
balik= soal[::-1]
hasil1 = []

for i in range(len(balik) // 2):
  temp  = balik[:2]
  hasil1.append(chr(int(temp, 16)))
  balik = balik[2:]

hasil2 = "".join(hasil1)
hasilTemp = hasil2.split('{')[1]
hasilTemp = hasilTemp.split('}')[0]

hasil3 = ""

for j in range(len(hasilTemp) // 2):
  temp = hasilTemp[:2]
  hasil3 += chr(int(temp, 16))
  hasilTemp = hasilTemp[2:]

hasil4 = re.sub('\{.*?\}', '{'+ hasil3 +'}', hasil2)
print(hasil4)
