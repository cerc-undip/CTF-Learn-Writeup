# Forensic 101
**Category:** forensic

Untuk menyelesaikan challenge bertipe **forensic** awali dengan cek tipe file dan strings, karena dari sini bisa saja terdapat informasi yang dapat digunakan untuk menemukan clue selanjutnya.

Cek file menggunakan terminal
```
file pic.jpg
```

Dari perintah diatas ternyata file tersebut merupakan file berjenis `JPEG Image`. Dalam kasus lain gambar bisa berjenis `ZIP`, `TAR.GZ`, `RAR`, maupun yang lain
```
pic.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 236x218, frames 3
```

Jika file dibuka tidak akan didapat informasi yang penting. Hanya terdapat gambar minion dan tulisan yang tidak berkaitan dengan challenge
```
eog pic.jpg
```
![](./pic.jpg)

> Hal terpenting ketika menyelesaikan challenge bertipe `forensic`
> dengan mengecek kata-kata yang ada di dalam file tersebut

```
strings pic.jpg
```
Dari perintah diatas kita dapatkan kata-kata yang acak. Namun pada bagian terakhir ada string yang dapat dibaca, dan itu merupakan flag-nya.
```
...
X`( 
8kF=
~9%]Tn
flag{wow!_data_is_cool}
$lqU
AG{u
Xm*CnC
@'hnQ
ax+p
bdQG
D_ O
```

flag `flag{wow!_data_is_cool}`