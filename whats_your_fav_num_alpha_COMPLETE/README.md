# What's Your Favorite Number of the Alpha
**Category:** programming

> The flag accidentally got changed into something else. Here is the flag: ¥¦§¸ªßØÌÉÃÊÐÅËá If it helps, I think the first letter was an A (capitalized)... Title is supposed to be "What's Your Favorite Number of the Alphabet, got cut off :(
---

Pada challenge ini kita langsung diberikan flag-nya, hanya saja dalam bentuk yang tidak bisa dibaca. Kita diharuskan untuk mengubah bentuk itu menjadi bentuk yang bisa dibaca.

Di soal juga diberikan clue bahwa huruf pertama adalah huruf `A` kapital.

| Dari | Menjadi |
|------|---------|
| ¥    | A       |

Kita akan coba menyelesaikan challenge ini menggunakan bahawa pemrograman Python karena bahasa ini menyediak konversi dari karakter ASCII menjadi desimal (_ASCII to Decimal_) sehingga kita bisa melihat algoritma yang dipakai untuk membuat rangkaian hurufnya.

Langsung saja jalankan Python3 interpreter
```
python3
```

Kita coba ubah karakter pertama soal menjadi desimal
```python
>>> ord('¥')
165
```
Ternyata didapat bahwa karakter `¥` memiliki angka desimal 165. Kemudian kita coba dengan karakter A.
```python
>>> # karakter -> desimal
>>> ord('A')
65
>>> # sebaliknya (desimal -> karakter)
>>> chr(65)
'A'
```

Nah, dari sini kita tahu bahwa algoritma yang dipakai untuk _decoding_ adalah dengan mengurangi 100 dari angka desimal dari ASCII. Atau bisa kita modelkan seperti ini:
> decode(kar) = desimal(kar) - 100

Kita bisa mencoba satu-satu seperti pada contoh sebelumnya. Tetapi agar efisien kita gunakan perulangan pada Python.
```php
>>> soal = "¥¦§¸ªßØÌÉÃÊÐÅËá"
>>> hasil = ""
>>> for karakter in soal:
...   temp = ord(karakter) - 100
...   hasil += chr(temp)
...
>>> print(hasil)
```

Gotcha! Kita dapat flag-nya!

flag : `ABCTF{the flag}`