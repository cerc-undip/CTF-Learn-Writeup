# Solve this 111
**Category:** miscellaneous
> 01001001001000000110110001101111 01110110011001010010000001100011 01101000011010010110001101101011 01100101011011100010000001100001 01101110011001000010000001101100 01100101011011010110111101101110
> Solve this
---

Pada challenge ini kita hanya diminta untuk mengkonversi dari bentuk biner kedalam bentuk karakter/string.

Untuk menyelesaikan ini kita bisa menggunakan bahasa pemrograman Python atau jika ingin cepat bisa gunakan [Binary to Text Online](https://www.rapidtables.com/convert/number/binary-to-ascii.html).

Penjelasan kode sama dan sudah dijelaskan pada writeup sebelumnya yaitu [Double Encryption](https://github.com/cerc-undip/CTF-Learn-Writeup/tree/update/double_encryption_COMPLETE).

Buat file `script.py` dan ubah aksesnya menjadi _executable_.
```bash
touch script.py
chmod +x script.py
```

Buka dan simpan kode ini di `script.py` kemudian jalankan menggunakan `./script.py`.
```python
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
```

flag : `I love chicken and lemon`