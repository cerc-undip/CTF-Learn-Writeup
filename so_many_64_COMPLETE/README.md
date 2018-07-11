# So Many 64s
**Category:** cryptography 

> Help! My friend stole my flashdrive that had the flag on it. When he gave it back the flag was changed! Can you help me decrypt it? https://mega.nz/#!UcYQEArA!H9WxSdG1O7eVcCm0dffggNB0-dBemSpBAXiZ0OXJnLk
---

Pada challenge ini sudah diberikan clue pada judul, yaitu **64** yang menandakan bahwa kita perlu menggunakan bentuk encoding dari **Base64** (Baca [disini](https://en.wikipedia.org/wiki/Base64)).

> Pengunaan Base64 sangat sering di challenge CTF. Maka dari itu diperlukan pemahaman dasar tentang bentuk encoding ini.

Setelah selesai mendownload mari kita buka file tersebut. Karena ekstensi file ini `.txt` maka kita bisa langsung membacanya.
```
cat flag.txt
```

Ketika dibaca, file ini terdiri dari banyak sekali karakter. Sekumpulan karakter ini adalah hasil dari encoding **Base64**. Bisa dengan mudah ditebak dari simbol "sama dengan" (=) di akhir.
```
...ZIZEZaU2JGcFdWRlZTY2xCUlBUMD0=
```

Saat dihitung, file ini memiliki 288956 karakter
```
cat flag.txt | wc -c
```

Untuk menyelesaikan ini kita bisa menggunakan bash script ataupun dengan bahasa pemrograman Python. Tetapi sebelum itu mari kita telaah lagi file `flag.txt` ini dengan men-`decode` karakternya dengan **Base64 decoding**.
```
cat flag.txt | base64 -d
```

Setelah di-_decode_ ternyata hasilnya adalah dalam bentuk Base64 juga. Tetapi jika diperhatikan, hasil decode ini berbeda dengan file decode aslinya. Mari kita coba decode sekali lagi.
```
cat flag.txt | base64 -d | base64 -d
```

Dan memang benar, ketika di-_decode_ kedua kalinya ternyata menghasilkan bentuk Base64 yang berbeda. Bisa dipastikan ini adalah bentuk rekursif Base64 (berulang-ulang).

Jika kita menulis perintah secara manual maka akan memakan waktu sangat banyak, karena kita tidak tahu berapa kali pesan ini di-_encoding_. Maka dari itu dalam writeup ini kita akan menggunakan bahasa pemrograman Python, namun saya sertakan juga penyelesaian dalam bentuk _bash script_.

Langsung saja kita buat file python dan ubah aksesnya menjadi _executable_. Kemudian buka file-nya.
```
touch script.py
chmod +x script.py
```

Untuk bisa men-_decode_ base64 kita perlu menambahkan library base64. Jika belum terinstal maka gunakan perintah `sudo pip install base64`. Karena kita sudah punya file pesan encoding-nya, maka kita akan membaca dari file-nya saja.

```python
#!/usr/bin/python3
import base64

f = open('flag.txt', 'r')
hasil = f.read()

print(hasil)
```

Simpan kemudian jalankan dengan `./script.py`. Dalam program ini kita baru membaca file asli dari pesan yang di-_encoding_. Ketika pesannya muncul sesuai dengan file aslinya, maka bisa kita lanjutkan.

Untuk men-_decode_ pesan kita gunakan _method_ dari library `base64` yaitu `b64decode()`.

```python
#!/usr/bin/python3
import base64

f = open('flag.txt', 'r')
hasil = f.read()
hasil = base64.b64decode(hasil)

print(hasil)
```

Kode diatas baru men-_decode_ satu kali, maka dari itu kita buat perulangan agar program bekerja otomatis. Ketika hasil decoding-nya memiliki karakter `{` (_karakter yang ada di dalam flag biasanya terdiri dari kurung kurawal_) maka kita akan menghentikan program dan menampilkan hasilnya.
```python
#!/usr/bin/python3
import base64

f = open('flag.txt', 'r')
hasil = f.read()

while True:
  hasil = base64.b64decode(hasil).decode('utf-8')

  if '{' in hasil:
    print(hasil)
    break
```
* `.decode('utf-8')`: mengkonversi dari bentuk bytes (hasil decoding) menjadi string.

Setelah program dijalankan maka, Gotcha! Kita menemukan flag-nya!



flag : `ABCTF{pr3tty_b4s1c_r1ght?}`