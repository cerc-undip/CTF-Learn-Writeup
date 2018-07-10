# POST Practice
**Categori:** web
```
These website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe these is still some way to authenticate? https://ctflearn.com/post.php
```
---

Clue dari challenge ini sangat jelas, yaitu mengirimkan request dengan motode `POST`. Pertama, kita cari tahu dahulu isi dari alamat url `https://ctflearn.com/post.php`

Challenge ini dapat diselesaikan dengan `bash script` maupun bahasa pemrograman Python. Namun dalam contoh ini menggunakan `bash script`.
```
curl https://ctflearn.com/post.php
```

Dengan mengeksekusi perintah diatas, kita mengirimkan request dengan method `GET` ke alamat `https://ctflearn.com/post.php`. Response dari web menyertakan _credential_ yang dapat kita gunakan untuk menembus web ini.

Selanjutnya kita mengirim request dengan metode `POST` dengan _credential_ yang sudah kita dapatkan,
```
curl https://ctflearn.com/post.php -d username=admin -d password=71urlkufpsdnlkadsf
```
* `-d username=admin`: mengirim data username dengan nilai `admin`
* `-d password=71urlkufpsdnlkadsf`: mengirim data password dengan nilai `71urlkufpsdnlkadsf`

> Dalam bahasa pemrograman PHP sama saja dengan `$_POST['username'] = "admin"`, `$_POSt['password'] = "71urlkufpsdnlkadsf"`

Setelah perintah dieksekusi maka kita akan mendapatkan flag yang kita cari.

flag : `flag{p0st_d4t4_4ll_d4y}`