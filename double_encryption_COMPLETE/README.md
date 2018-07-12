# Double Encryption
**Category:** cryptography
> 0101101001101101011110000110100001011010001100110111010000110101011000100011001101010101011011100110001101101101010101010110011101011001010100110100001001101010011000100011001000111001011100110100100101000111010100100011000101011010010001110101011000111001

> Good Luck
---

Untuk menyelesaikan ini kita perlu mengubah bentuk biner tersebut menjadi karakter/teks. Kita bisa akan selesaikan challenge ini menggunakan bahasa pemrograman Python, atau jika ingin cepat bisa gunakan [Binary to Text online](https://www.rapidtables.com/convert/number/binary-to-ascii.html).

Oke, kita buat file `script.py` dan ubah menjadi _executable_, kemudian buka filenya.
```bash
touch script.py
chmod +x script.py
```

Untuk pertama kita membuat 2 variabel: `soal` untuk menyimpan pesan biner dan `hasil_temp` untuk menyimpan setiap 8 bit pesan kedalam list/array.

```python
#!/usr/bin/python3
soal = "0101101001101101011110000110100001011010001100110111010000110101011000100011001101010101011011100110001101101101010101010110011101011001010100110100001001101010011000100011001000111001011100110100100101000111010100100011000101011010010001110101011000111001"
hasil_temp = []

for i in range(len(soal) // 8):
  hasil_temp.append(soal[:8])
  soal = soal[8:]

print(hasil)
```

Selanjutnya kita ubah tiap 8 bit tersebut menjadi karakter ASCII.

| Dari | Menjadi | Perintah |
|---|---|---|
| biner  | desimal | int(var_biner, 2) |
| desimal| ASCII   | chr(var_desimal)  |


```python
#!/usr/bin/python3
soal = "0101101001101101011110000110100001011010001100110111010000110101011000100011001101010101011011100110001101101101010101010110011101011001010100110100001001101010011000100011001000111001011100110100100101000111010100100011000101011010010001110101011000111001"
hasil_temp = []

for i in range(len(soal) // 8):
  hasil_temp.append(soal[:8])
  soal = soal[8:]

hasil = ""

for j in range(len(hasil_temp)):
  temp = chr(int(hasil_temp[j], 2))
  hasil += temp

print(hasil)
```

Setelah dijalankan, ternyata pesan biner ini menghasilkan pesan lain dalam bentuk Base64. Selanjutnya kita akan _decode_ pesan ini menggunakan library python `base64`. Jika belum terinstal bisa gunakan `sudo pip install base64` atau `sudo pip3 install base64`.

```python
#!/usr/bin/python3
import base64

soal = "0101101001101101011110000110100001011010001100110111010000110101011000100011001101010101011011100110001101101101010101010110011101011001010100110100001001101010011000100011001000111001011100110100100101000111010100100011000101011010010001110101011000111001"

hasil_temp = []

for i in range(len(soal) // 8):
  hasil_temp.append(soal[:8])
  soal = soal[8:]

hasil = ""

for j in range(len(hasil_temp)):
  temp = chr(int(hasil_temp[j], 2))
  hasil += temp

hasilAkhir = base64.b64decode(hasil).decode('utf-8')
print(hasilAkhir)
```

Terakhir, jalankan program tersebut `./script.py` dan kita akan mendapatkan flag yang kita inginkan.

flag : `flag{you're a cool dude}`