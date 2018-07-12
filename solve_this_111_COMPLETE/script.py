#!/usr/bin/python3

soal = "01001001001000000110110001101111 01110110011001010010000001100011 01101000011010010110001101101011 01100101011011100010000001100001 01101110011001000010000001101100 01100101011011010110111101101110"
soal = "".join(soal.split(" "))
hasil_temp = []

for i in range(len(soal) // 8):
  hasil_temp.append(soal[:8])
  soal = soal[8:]

hasil = ""

for j in hasil_temp:
  temp = int(j, 2)
  hasil += chr(temp)

print(hasil)
