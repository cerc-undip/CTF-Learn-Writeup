# Exif
**Category:** forensic
> If only the password were in the image?
> https://mega.nz/#!QDZGiLSZ!fkkhBJuBBtBKGsLTDiF2NuLihP2WRd97Iynd3PhWqRw
> 
> You could really "own" it with exif
---

Pada challenge ini kita diminta untuk mencari flag dari gambar yang disediakan. Di judul juga sudah diberikan clue untuk menggunakan Exif (Exchangeable Image File). ([Baca disini](https://en.wikipedia.org/wiki/Exif)).

> Exif cukup sering digunakan untuk mencari informasi di dalam file gambar

Oke, kita akan melihat informasi EXIF ini di terminal dengan perintah `exiftool`. Jika belum menginstal silahkan gunakan `sudo apt-get install exiftool`.
```bash
exiftool Computer-Password-Security-Hacker\ -\ Copy.jpg | more
```

Dengan perintah diatas kita dapat mengetahui semua informasi EXIF yang ada di dalam gambar ini. Pada baris `Owner Name` terdapat flag yang kita cari.

flag : `flag{3l1t3_3x1f_4uth0r1ty_dud3br0}`