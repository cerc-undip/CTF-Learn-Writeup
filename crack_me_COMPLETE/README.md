# Crack Me
**Category:** binary exploitation
> I forgot the secret code to my program can you help me find it?
> https://mega.nz/#!x2xwQS7S!-Id_VR5BDMQv3MEVo89zxA51LWlkQQHy8r7WBBN45CI
---

Challenge kali ini berkategori **Binary Exploitation** yang artinya kita perlu melakukan teknik _reverse engineering_ terhadap program agar kita mendapatkan informasi yang kita inginkan. ([Baca disini](https://en.wikipedia.org/wiki/Reverse_engineering))

Namun dalam menyelesaikan challenge **Crack Me** kita tidak perlu melakukan **reverse engineering** terhadap program melainkan kita bisa menyelesaikannya seperti pada challenge berkategori **Forensic**.

Download file dan lihat jenis file-nya
```bash
$ file crackme.exe
crackme.exe: PE32 executable (console) Intel 80386, for MS Windows
```

Dari sini kita tahu bahwa format file ini adalah **PE32** yang bisa dijalankan melalui sistem console Windows. Tentu kita tidak perlu menjalankannya melalui OS Windows. Mari kita lihat informasi string yang ada di dalamnya.
```bash
strings crackme.exe | more
```

Ketika kita _scroll_ informasi string kita dapat melihat beberapa kalimat yang akan ditampilkan oleh program ketika dijalankan. Namun ada sebuah string berawalan `flag` yang dimana itu adalah flag yang kita cari.

flag : `flag{h4ck3rm3n_4ss3mbl3}`