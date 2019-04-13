# Pumpkin Carving
**Category:** forensic
> Something seems to be wrong with the image that I tried to download for Halloween. Perhaps someone has tampered with it.
> 
> https://mega.nz/#!kTpy3JqA!9zID1eTwNRHUCxPXl191uDuKoCj1rcMWt6GtwDx5yG8
> 
> Hint: The flag is in flag{flag_value} format.
---

Pada challenge ini kita diminta untuk mencari flag yang ada di dalam gambar yang disediakan.

Silahkan download file tersebut dan buka menggunakan image viewer.
```bash
eog Pumpkin_.png
```

Ketika dibuka, terjadi error yang mengakibatkan gambar tidak bisa dilihat. Kemungkinan besar file ini telah dilakukan _steganografi_. ([Baca disini](https://id.wikipedia.org/wiki/Steganografi))

Selanjutnya kita cek jenis file ini. Karena file ini merupakan `.png` maka kita bisa sekaligus mengecek apakah terdapat _corrupt_.
```bash
file Pumpkin_.png
pngcheck Pumpkin_.png
```

Dengan perintah `pngcheck` kita tahu bahwa file `Pumpkin_.png` memang corrupt. Selanjutnya kita coba lihat data string yang dapat dibaca dari file ini.
```bash
strings Pumpkin_.png | more
```

Gotcha! Kita temukan flag-nya di bagian atas! Good job!

flag : `flag{happy_halloween!}`