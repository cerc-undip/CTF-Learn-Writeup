# Binwalk
**Category:** forensic
```
https://mega.nz/#!4UEnAZKT!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY
```
---

Pada challenge Binwalk ini kita tidak diberikan clue sama sekali, melainkan hanya judul dan alamat file untuk didownload

Kita buka file gambar yang baru saja didownload
```
eog PurpleThing.jpeg
```

Ketika membuka file, kita mendapatkan error. Hal ini terjadi kemungkinan karena gambar sudah disisipi file yang lain (atau:_Steganografi_).

Kita akan lihat string yang ada di dalam file ini dan jenisnya.
```
strings PurpleThing.jpeg
file PurpleThing.jpeg
```

Perintah `strings` tidak menghasilkan data yang kita inginkan.

Dengan perintah `file` kita tahu bahwa sebenarnya file `PurpleThing.jpeg` bukanlah jenis file **JPEG** melainkan file **PNG**. Maka kita ubah ekstensinya menjadi `.png`.
```
mv PurpleThing.jpeg PurpleThing.png
```

setelah itu kita cek apakah file `PurpleThing.png` _corrupt_ atau tidak dengan menggunakan perinah `pngcheck`. Jika belum menginstall maka bisa gunakan perintah `sudo apt-get install pngcheck`.
```
pngcheck PurpleThing.png
```

Setelah dieksekusi ternyata file `PurpleThing.png` corrupt
```
PurpleThing.png  additional data after IEND chunk
ERROR: PurpleThing.png
```

Untuk melakukan _recovering_ kita gunakan perintah `foremost`. Jika belum menginstall bisa gunakan perintah `sudo apt-get install foremost`.
```
foremost PurpleThing.png -v
```
* `-v`: menampilkan urutan eksekusi, sehingga kita bisa lihat berapa file yang di-recover (_verbose_)

```
...
File: PurpleThing.png
Start: Sat Jan 34 22:31:28 2500
Length: 160 KB (164802 bytes)
 
Num  Name (bs=512)         Size  File Offset   Comment 

0:  00000000.png       149 KB             0     (780 x 720)
1:  00000299.png        11 KB        153493     (802 x 118)
*|
...
```

Setelah _recovering_ terdapat 1 folder `output` dan 2 file baru, satu file PurpleThing asli, dan satunya lagi adalah file gambar dengan format `.png` yang tersisip di dalam gambar `PurpleThing.png`.
* `00000000.png` merupakan file asli
* `00000299.png` merupakan file yang tersisip

```
cd output/png
eog 00000299.png
```
flag : `ABCTF{B1nw4lk_is_us3ful}`