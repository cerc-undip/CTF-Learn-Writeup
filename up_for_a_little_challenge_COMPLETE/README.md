# Up For A Little Challenge?
**Category:** forensic

> https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0 You Know What To Do ...
---

Challenge ini tidak memberikan clue apapun dan beranggapan bahwa kita tahu apa yang kita lakukan. Oke mari kita buka file `Begin Hack.jpg` yang baru didownload
```bash
eog Begin\ Hack.jpg
```

![](./Begin Hack.jpg)

Setelah dibuka dengan _image viewer_ tidak ada keterangan yang berarti dan hanya gambar biasa.

Selalu perhatikan untuk file yang bertipe gambar pasti sudah dilakukan Steganografi, yaitu pesan disembunyikan di dalam gambar ([Baca disini](https://id.wikipedia.org/wiki/Steganografi)). Untuk itu kita perlu mengecek informasi apa saja yang ada di dalam gambar ini dalam bentuk _string_ (karakter yang bisa dibaca oleh manusia).
```bash
strings Begin\ Hack.jpg | more
```

Perhatikan beberapa kata yang bisa dibaca ketika kita _scroll_. Disitu terdapat satu URL, buka URL itu dan download file yang ada.

> https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg

Extract file tersebut
```bash
unzip Up\ For\ A\ Little\ Challenge.zip
```

Setelah di-_extract_ kita mendapat ada 2 folder yaitu `Did I Forget Again?` dan `__MACOSX`. Folder yang akan kita jelajah adalah `Did I Forget Again?`, sedangkan folder `__MACOSX` adalah folder yang otomatis dibuat ketika membuat arsip menggunakan komputer Mac. ([Baca disini](https://gotoes.org/sales/Zip_Mac_Files_For_PC/What_Is__MACOSX.php))
```
cd Did\ I\ Forget\ Again\?
ls -la
```

Disini ada 1 file gambar dan 1 file tersembunyi dengan ekstensi `cerb4`. Jika kita buka file `Loo Nothing Becomes Useless ack.jpg` tidak akan ada informasi yang disediakan, begitu juga ketika kita melihat string dari gambar ini.
```bashi
eog Loo\ Nothing\ Becomes\ Useless\ ack.jpg
strings eog Loo\ Nothing\ Becomes\ Useless\ ack.jpg
```

Kali ini kita coba telaah apa itu file .Processing.cerb4
```
file .Processing.cerb4
```

Setelah dilihat, ternyata jenis file ini adalah **Zip**. maka dari itu kita perlu mengubah/menambah ekstensi `.zip` di belakang nama file. Kemudian lakukan _extracting_.
```bash
mv .Processing.cerb4 .Processing.cerb4.zip
unzip .Processing.cerb4.zip
```

Saat mencoba meng-_extract_ file ini, kita diminta untuk memasukkan password. Lalu dimana kita bisa mendapat password-nya?

Oke, sekarang kita kembali lagi ke file yang pertama dan lihat lagi bahwa disitu terdapat password yang dapat digunakan untuk meng-_extract_ file tadi.
```
cd ..
strings Begin\ Hack.jpg | more
```

> Nothing Is As It Seems

Kemudian kita extract file `.Processing.cerb4.zip` dengan password yang telah kita dapat. Terakhir, kita buka file yang telah di-_extract_.
```
cd Did\ I\ Forget\ Again\?
unzip .Processing.cerb4.zip
eog skycoder.jpg
```

Gotcha! Kita dapat flag-nya! Ada di pojok kanan bawah.

flag : `flag{hack_complete}`
