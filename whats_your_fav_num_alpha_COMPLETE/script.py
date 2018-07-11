#!/usr/bin/python3

soal = "¥¦§¸ªßØÌÉÃÊÐÅËá"
hasil = ""

for karakter in soal:
  temp = ord(karakter) - 100
  hasil += chr(temp)

print(hasil)
