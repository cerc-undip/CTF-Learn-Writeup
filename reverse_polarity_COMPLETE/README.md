# Reverse Polarity
**Category:** cryptography

> I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do?

> The only thing I could get off of it was this: 
> 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101
---

Pada challenge ini kita hanya diminta untuk mengkonversi bentuk biner kedalam bentuk teks.

Untuk menyelesaikan challenge ini kita bisa menggunakan bahasa pemrograman Python atau jika ingin cepat maka bisa gunakan [Binary to Text translator online](https://www.rapidtables.com/convert/number/binary-to-ascii.html).

```bash
touch script.py
chmod +x script.py
```

Kemudian buka file `script.py` dengan text editor.
```python
#!/usr/bin/python3

baca = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"
temp = []

for i in range(16):
  temp.append(baca[:8])
  baca = baca[8:]

for i in temp:
  print(chr(int(i, 2)), end="")
```

* Kita memecah setiap 8 karakter bit kedalam list/array temp
* Sisa dari 8 karakter itu disimpan kedalam variabel `baca` agar bisa dipecah kembali
* Setiap nilai di `temp` diubah dari bentuk biner menjadi karakter (`chr()`)

flag : `CTF{Bit_Flippin}`
