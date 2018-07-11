#!/usr/bin/python3

soal = "êööòõ¼±±åñæçòçð°ëñ±ðëåîçø´²±è÷îî±øûÛÓüÉ±"

hasil = ""

for karakter in soal:
  temp = ord(karakter) - 130
  hasil += chr(temp)

print(hasil)
