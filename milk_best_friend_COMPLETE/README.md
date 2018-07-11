# Milk's Best Friend
**Category:** forensic

> There's nothing I love more than oreos, lions, and winning. https://mega.nz/#!qpFlCTiZ!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y Have Fun :)
---

Pada challenge ini tidak diberikan clue yang membantu sehingga kita perlu mencari sendiri solusi untuk menyelesaikannya.

![Oreo](./oreo.jpg)

> Seperti biasa, setelah mendownload pastikan lihat jenis file dan juga _string_ yang terdapat di dalam file. Karena file gambar bisa saja disisipi file lain (_Steganografi_)

```bash
file oreo.jpg
strings oreo.jpg
```

Dengan command `file` kita tahu bahwa file gambar ini memang benar file gambar berformat **JPEG**. Namun ketika kita eksekusi command `strings` kita hanya melihat kata-kata acak yang bukan kita cari.

Selanjutnya kita coba cari tahu apakah file gambar ini telah dilakukan steganografi atau belum dengan menggunakan perintah `binwalk`. Jika belum menginstal bisa gunakan `sudo apt-get install binwalk`.
```
binwalk oreo.jpg
```

Setelah diteliti ternyata `oreo.jpg` ini telah dilakukan steganografi dan terdapat 1 file berformat RAR.
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
9515          0x252B          RAR archive data, first volume type: MAIN_HEAD
```

Maka dari itu kita _extract_ file tersembunyi itu menggunakan perintah `foremost`.
```bash
foremost -v oreo.jpg
```

Setelah diekstrak terdapat 2 file baru di folder output. 1 file asli oreo sebelum dilakukan steganografi dan 1 nya lagi berekstensi `.rar`.

Kita masuk ke folder tersebut dan _extract_ file yang ada di dalamnya.
```bash
cd output/rar
unrar x 00000018.rar
```

> Jika belum paham dengan perintah ekstraksi bisa [baca disini](https://linux.die.net/man/1/unrar).

Setelah di-_extract_ kita mendapat 1 file teks dan 1 file gambar. Gambar ini hampir sama dengan gambar yang pertama, namun ketika kita lihat _string_ yang ada di dalam gambar maka kita akan menemukan flag-nya.
```bash
cd 1
strings b.jpg
```

flag : `flag{eat_more_oreos}`