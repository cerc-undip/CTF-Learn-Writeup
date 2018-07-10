# Taking LS
**Category:** forensic

```
Just take the Ls
https://mega.nz/#!9Mk00LxR!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8
NOTE: Problem is really only for mac users - sorry in advance - free points if you have a different operating system though :)
```

Extract file download menggunakan terminal
```
unzip The\ Flag.zip
ls -l
```

Setelah di-ekstrak, akan ada folder baru bernama `The Flag`. Masuk ke folder `The Flag`
```
cd The\ Flag
```

Setelah itu, list semua file yang ada di dalam folder `The Flag`
```
ls -l
```

Disini hanya terdapat file `The Flag.pdf`. Kita coba buka file tersebut, bisa menggunakan **gnome** maupun buka melalui **nautilus**
```
gnome-open The\ Flag.pdf
```
atau
```
nautilus ./
```

Ketika kita coba buka ternyata file tersebut di-password. Langkah selanjutnya adalah kita mencari password-nya.
Kali ini kita coba list semua file di dalam folder `The Flag` agar kita bisa melihat file yang tersembunyi.
```
ls -la
```
* `l`: menampilkan dalam bentuk list lengkap
* `a`: menampilkan semua file, termasuk file tersembunyi

Setelah mencoba perintah diatas ternyata ada 2 file dan folder baru yang tersembunyi (_tanda `.` di awal_), yaitu `.DS_Store` dan `.ThePassword`.
File `.DS_Store` bukan merupakan file yang kita cari. Kita masuk ke folder `.ThePassword`. Di dalam folder ini terdapat 1 file berekstensi `.txt` maka bisa langsung kita lihat isinya.
```
cd .ThePassword
ls -la
cat ThePassword.txt
```

Setelah melihat isi file, kita mendapatkan password yang kita inginkan. Kemudian kembali lagi ke folder sebelumnya dan kita buka lagi file pdf dengan memasukkan password yang sudah kita dapat.
```
cd ..
gnome-open The\ Flag.pdf
```

flag `ABCTF{T3Rm1n4l_is_C00l}`