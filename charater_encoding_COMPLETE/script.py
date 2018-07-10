#!/usr/bin/python3

soal = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
soal = soal.split(" ")
hasil = ""

for i in soal:
  temp = int(i, 16)
  hasil += chr(temp)

print(hasil)
