# Photo Analysis
**Category:** miscellaneous
> You can do it, you just gotta belieeeeeeeeeeeeeeeve! 
> 
> I used the same wrap as with all my other problems.
> 
> https://mega.nz/#!MNNAhaSK!IKDHTx9oXNSa4dsn9DG_rwA08yycqc3yC4iFkQY8lvc
---

Pada challenge ini kita diberikan 1 file gambar. Mari kita buka file ini dengan image viewer.
```bash
eog dank\ trump.jpeg
```

Ketika kita lihat, gambar bagian bawah terlihat rusak dan tidak jelas. Kemungkinan gambar ini telah dilakukan _steganografi_. ([Baca disini](https://id.wikipedia.org/wiki/Steganografi))

Selanjutnya kita coba lihat data string yang dapat terlihat di file ini.
```bash
strings dank\ trump.jpeg
```

Gotcha! Di bagian bawah kita bisa menemukan flag yang kita cari.

flag : `CTF{OMG_You_Believed}`