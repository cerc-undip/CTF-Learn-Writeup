# Character Encoding
**Categori:** cryptography
> In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D
---

Pada challenge ini kita diminta untuk men-_decode_ karakter yang tertera. Namun sebelum bisa men-_decode_ kita perlu tahu teknik _decoding_ apa yang dipakai di dalam soal.

Kita melihat susunan karakter `41 42 43 54 46 7B ...` dimana hanya terdapat angka dan huruf yang terdiri dari A sampai F saja. Ini merupakan encoding karakter **ASCII**. Untuk menyelesaikannya kita gunakan bahasa pemrograman Python.

```
touch script.py
chmod +x script.py
```

Buka file `script.py` menggunakan text editor.

```
#!/usr/bin/python3

soal = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
soal = soal.split(" ")
hasil = ""

for i in soal:
  temp = int(i, 16)
  hasil += chr(temp)

print(hasil)
```

* `soal = soal.split(" ")`: memasukkan setiap karakter yang dipisahkan dengan spasi kedalam variabel soal. Tipe data soal sekarang adalah _list_ (_array_ dalam bahasa pemrograman lain)
* `for i in soal:`: akan mengakses setiap nilai di variabel soal dan memasukkannya kedalam variabel `i`
* `int(i, 16)`: konversi dari _hex_ ke _integer_
* `chr(temp)`: konversi dari _integer_ ke _character_

Setelah program dijalankan. Gotcha! kita dapat flag-nya.

flag : `ABCTF{45C11_15_U53FUL}`