# OTPYRC
**Category:** cryptography

> Okay, this one is pretty easy... but not necessarily.
> d733432373937303734373666343730373937323733343b7644534
---

Pada challenge ini kita diberikan satu baris kombinasi huruf dan angka. Dari kombinasi tersebut bisa terlihat bahwa kombinasinya menyerupai kumpulan hex yang digabung karena tidak ada huruf yang selain `a-z`.

Setelah tahu bahwa itu bentuk hex, maka kita perlu membaliknya agar menjadi kata yang dapat dibaca
```python
soal = "d733432373937303734373666343730373937323733343b7644534"
balik= soal[::-1]
hasil1 = []

for i in range(len(balik) // 2):
  temp  = balik[:2]
  hasil1.append(chr(int(temp, 16)))
  balik = balik[2:]

print(hasil1)
```

Kode diatas menghasilkan keluaran :
> `['C', 'T', 'F', '{', '4', '3', '7', '2', '7', '9', '7', '0', '7', '4', '6', 'f', '7', '4', '7', '0', '7', '9', '7', '2', '4', '3', '}']`

Dari sini sudah ketahuan bahwa hasil tersebut adalah flag, selanjutnya tinggal mencari string di dalam tanda kurung.

```python
import re

soal = "d733432373937303734373666343730373937323733343b7644534"
balik= soal[::-1]
hasil1 = []

for i in range(len(balik) // 2):
  temp  = balik[:2]
  hasil1.append(chr(int(temp, 16)))
  balik = balik[2:]

print(hasil1)
exit

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
```

flag : `CTF{CryptotpyrC}`