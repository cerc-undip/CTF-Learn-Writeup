# Git is Good
**Category:** forensic

> The flag used to be there. But then I redacted it. Good Luck. https://mega.nz/#!C483DAYB!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc
---

Pada judul sudah terpampang dengan jelas apa yang akan kita lakukan di challenge ini, yaitu menggunakan **git**. Jika belum menginstal silahkan download dan install git [disini](https://git-scm.com/downloads)

_Extract_ file yang baru kita download. Setelah itu akan muncul semua informasi file apa saja yang di-_extract_
```
unzip gitIsGood.zip
cd gitIsGood
ls -la
```

Ketika masuk ke folder `gitIsGood` disitu terdapat 1 file `flag.txt` dan 1 folder `.git` yang menandakan bahwa folder ini adalah _repository_ git. Kita coba baca isi file `flag.txt`.
```
cat flag.txt
```

Ketika `flag.txt` dibaca, ada tulisan flag. Tetapi ini bukanlah flag yang kita cari, karena flag tersebut sudah diedit (_redacted_).

Dengan **git** kita bisa melihat _history_ pengeditan pada repository dengan perintah `log`.
```
git log
```

Dari sini kita bisa lihat _history_ pengeditan yang pernah dilakukan serta tanggal dan keterangannya. Dari sini juga kita tahu bahwa file `flag.txt` telah diedit 3 kali.

Untuk melihat detail perubahannya kita bisa menggunakan _option_ `-p` (_patch_).
```
git log -p
```

Gotcha! Kita bisa melihat flag sebelum dilakukan perubahan.

flag : `flag{protect_your_git}`
