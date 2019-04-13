# Hat on my HEAD
**Category:** forensic
> A Tip of the Hat to anyone who can solve this.
> 
> https://mega.nz/#!lKZ2VaiY!DkGHSZZh6msYsvP_iuHDryQdRO-pd7b6qhbWb_f4noY
---

Pada challenge ini kita diminta untuk mencari flag yang ada di gambar yang sudah disediakan.

Karena file tersebut beresktensi `.png` mari kita cek dulu apakah file ini terdapat _corrupt_ atau tidak.
```bash
pngcheck whitehat.png
```
> whitehat.png:  CORRUPTED by text conversion
> ERROR: whitehat.png

Setelah di-_run_ ternyata file ini _corrupt_. Karena file ini corrupt perlu dilakukan _recovering_. Tetapi sebelum itu kita coba untuk melihat string yang ada pada file ini.
```bash
strings whitehat.png | more
```

Ternyata dengan melihat string kita menemukan flag yang kita cari tanpa melakukan _recovering_ datanya. Tetapi jika kalian ingin mencoba _recovering_ silahkan saja.
```bash
foremost -v whitehat.png
```

Ternyata ketika proses _recovering_ tidak terdapat data apapun didalamnya. Kemungkinan file ini corrupt karena ditambahkan string flag.

flag : `Cyber{M'Lady}`