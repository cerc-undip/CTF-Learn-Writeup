# Privacy Matters
**Category:** programming

> The URL that has the flag got corrupted again... here it is: êööòõ¼±±åñæçòçð°ëñ±ðëåîçø´²±è÷îî±øûÛÓüÉ±
---

Solusi dan langkah penyelesaian challenge ini hampir sama dengan [What's Your Favorite Number of the Alpha](https://github.com/cerc-undip/CTF-Learn-Writeup/tree/update/whats_your_fav_num_alpha_COMPLETE).

Pada challenge ini kita diberikan kumpulan karakter yang tidak bisa dibaca. Untuk memecahkannya kita perlu mengetahui algoritma _encoding_ yang dipakai untuk membuat karakter "_unreadable_" itu.

Clue dari soal yang dapat membantu adalah `The URL that has the flag ...`. Ini berarti kumpulan karakter tersebut adalah kumpulan karakter yang membentuk suatu URL

URL terdiri dari kata `http` atau `https` pada awalnya (Baca [disini](https://en.wikipedia.org/wiki/URL)), sehingga kita bisa mencoba untuk decoding karakter tersebut menggunakan bahasa pemrograman Python. Karena bahasa ini menyediakan konversi dari karakter ASCII ke desimal.

Kita jalankan interpreter Python versi 3.
```bash
python3
```

Kita coba konversi 4 karakter awal dari karakter menjadi desimal.

```python
>>> ord('ê')
234
>>> ord('ö')
246
>>> ord('ö')
246
>>> ord('ò')
242
```

Perhatikan ada 2 kali karakter `ö`. Kemungkinan besar membentuk kata `http` ataupun `https`.

Selanjutnya kita coba konversi karakter `http` menjadi desimal.
```python
>>> ord('h')
104
>>> ord('t')
116
>>> ord('t')
116
>>> ord('p')
112
```

Oke, dari sini kita coba cocokkan algoritmanya.

| Encoded | Desimal(Enc) | Decoded | Desimal(Dec) |
|---------|--------------|---------|--------------|
| ê       | 234          | h       | 104          |
| ö       | 246          | t       | 116          |
| ö       | 246          | t       | 116          |
| ò       | 242          | p       | 112          |

Ternyata proses decodingnya adalah adalah dengan mengurangi 130 dari angka desimal dari ASCII. Atau bisa kita modelkan seperti ini:
> decode(kar) = desimal(kar) - 130

Kita bisa mencoba satu-satu seperti pada contoh sebelumnya. Tetapi agar efisien kita gunakan perulangan pada Python.
```python
>>> soal = "êööòõ¼±±åñæçòçð°ëñ±ðëåîçø´²±è÷îî±øûÛÓüÉ±"
>>> hasil = ""
>>> 
>>> for karakter in soal:
...     temp = ord(karakter) - 130
...     hasil += chr(temp)
... 
>>> print(hasil)
```

Setelah di-_decode_ ternyata menghasilkan suatu URL. Kemudian kita langsung saja buka url yang tertera.
```
https://codepen.io/niclev20/full/vyYQzG/
```

Pada website Codepen, kita buka Editor View untuk melihat source code project tersebut. Pada kolom HTML, disitulah flag yang kita cari. Mantap!

flag : `ABCTF{harder_this_time}`